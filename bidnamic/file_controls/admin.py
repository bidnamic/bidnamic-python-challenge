from django.contrib import admin
from file_controls.models import Campaign, AdGroup, SearchTerm
# Register your models here.


class AdminCampaign(admin.ModelAdmin):
    list_display = ('id', 'structure_value', 'status')


admin.site.register(Campaign, AdminCampaign)


class AdminAdGroup(admin.ModelAdmin):
    list_display = ('id', 'campaign', 'alias', 'status')


admin.site.register(AdGroup, AdminAdGroup)


class AdminSearchTerm(admin.ModelAdmin):
    list_display = ('id', 'ad_group', 'campaign', 'click', 'cost')
    search_fields = ('search_term',)


admin.site.register(SearchTerm, AdminSearchTerm)
