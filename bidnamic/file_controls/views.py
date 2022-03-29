import logging
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import View
from file_controls.models import Campaign, AdGroup, SearchTerm
from file_controls.extra_functions import get_file

logger = logging.getLogger('django')


class ReadCSVFileView(View):

    template_name = 'read-csv-file.html'

    def get(self, request):
        """
        Open upload file page.
        Args:
            request: None
        Returns:
            Render file upload template
        """
        return render(request, self.template_name, {})

    def post(self, request):
        """
        Try to get files from request. If exists, file send to get_file function and return as _csv.reader format. 
        Returned object controlled for duplicate and add to database.
        Args:
            request: {FILES}, None
        Returns:
            File upload template
        """
        campaign_file = request.FILES.get('campaign', None)
        csv_datas = get_file(campaign_file)
        if campaign_file and csv_datas:
            duplicate_data = set()
            exists = set()
            for row in csv_datas:
                if row[0] not in duplicate_data and row[0] not in exists:
                    try:
                        Campaign.objects.create(id=row[0], structure_value=row[1], status=row[2])
                        duplicate_data.add(row[0])
                    except IntegrityError:
                        logger.warning(f'Integrity Error Campaign ID {row[0]}')
                        exists.add(row[0])
            if Campaign.objects.all().exists() and Campaign.objects.all().count() != len(exists):
                messages.success(request, 'Campaign CSV file upload to database successfully')

        adgroup_file = request.FILES.get('adgroup', None)
        csv_datas = get_file(adgroup_file)
        if adgroup_file and csv_datas:
            duplicate_data = set()
            exists = set()
            for row in csv_datas:
                if row[0] not in duplicate_data and row[0] not in exists:
                    try:
                        campaign = Campaign.objects.get(id=row[1])
                        AdGroup.objects.create(id=row[0], campaign=campaign, alias=row[2], status=row[3])
                        duplicate_data.add(row[0])
                    except Campaign.DoesNotExist:
                        logger.warning(f'Campaign Object Does Not Exists ID {row[1]}')
                    except IntegrityError:
                        logger.warning(f'Integrity Error Ad Group ID {row[0]}')
                        exists.add(row[0])
            if AdGroup.objects.all().exists() and AdGroup.objects.all().count() != len(exists):
                messages.success(request, 'Ad Group CSV file upload to database successfully')

        search_terms_file = request.FILES.get('search_terms', None)
        csv_datas = get_file(search_terms_file)
        if search_terms_file and csv_datas:
            for row in csv_datas:
                try:
                    ad_group = AdGroup.objects.get(id=row[1])
                    campaign = Campaign.objects.get(id__=row[2])
                    SearchTerm.objects.create(date=row[0], ad_group=ad_group, campaign=campaign, click=row[3],
                                              cost=row[4], conversion_value=row[5], conversion=row[6],
                                              search_term=row[7])
                except AdGroup.DoesNotExist:
                    logger.warning(f'Ad Group Object Does Not Exists ID {row[1]}')
                except Campaign.DoesNotExist:
                    logger.warning(f'Campaign Object Does Not Exists ID {row[2]}')
            if SearchTerm.objects.all().exists():
                messages.success(request, 'Search Term CSV file upload to database successfully')
        return HttpResponseRedirect(reverse('file_controls:read-csv-files'))

