import csv
import io
import logging
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from filecontrols.models import Campaign, AdGroup, SearchTerm
# Create your views here.
logger = logging.getLogger('django')


class ReadCSVFileView(View):
    template_name = 'read-csv-file.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        campaign_file = request.FILES.get('campaign', None)
        if campaign_file:
            csv_datas = self.get_file(campaign_file)
            dublicate = set()
            exists = set()
            for row in csv_datas:
                if row[0] not in dublicate and row[0] not in exists:
                    try:
                        Campaign.objects.create(id=row[0], structure_value=row[1], status=row[2])
                        dublicate.add(row[0])
                    except IntegrityError:
                        logger.warning('Integrity Error Campaign ID {}'.format(row[0]))
                        exists.add(row[0])
            if Campaign.objects.all().exists() and Campaign.objects.all().count() != len(exists):
                messages.success(request, 'Campaign CSV file upload to database successfully')

        adgroup_file = request.FILES.get('adgroup', None)
        if adgroup_file:
            csv_datas = self.get_file(adgroup_file)
            dublicate = set()
            exists = set()
            for row in csv_datas:
                if row[0] not in dublicate and row[0] not in exists:
                    try:
                        campaign = Campaign.objects.get(id=row[1])
                        AdGroup.objects.create(id=row[0], campaign=campaign, alias=row[2], status=row[3])
                        dublicate.add(row[0])
                    except ObjectDoesNotExist:
                        logger.warning('Campaign Object Does Not Exists ID {}'.format(row[1]))
                    except IntegrityError:
                        logger.warning('Integrity Error Ad Group ID {}'.format(row[0]))
                        exists.add(row[0])
            if AdGroup.objects.all().exists() and AdGroup.objects.all().count() != len(exists):
                messages.success(request, 'Ad Group CSV file upload to database successfully')

        search_terms_file = request.FILES.get('search_terms', None)
        if search_terms_file:
            csv_datas = self.get_file(search_terms_file)
            for row in csv_datas:
                try:
                    ad_group = AdGroup.objects.get(id=row[1])
                    campaign = Campaign.objects.get(id=row[2])
                    SearchTerm.objects.create(date=row[0], ad_group=ad_group, campaign=campaign, click=row[3],
                                              cost=row[4], conversion_value=row[5], conversion=row[6],
                                              search_term=row[7])
                except AdGroup.ObjectDoesNotExist:
                    logger.warning('Ad Group Object Does Not Exists ID {}'.format(row[1]))
                except Campaign.ObjectDoesNotExist:
                    logger.warning('Campaign Object Does Not Exists ID {}'.format(row[2]))
            if SearchTerm.objects.all().exists():
                messages.success(request, 'Search Term CSV file upload to database successfully')
        return HttpResponseRedirect(reverse('filecontrols:read-csv-files'))

    def get_file(self, file):
        csv_file = io.StringIO(file.read().decode())
        csv_datas = csv.reader(csv_file)
        next(csv_datas)
        return csv_datas

