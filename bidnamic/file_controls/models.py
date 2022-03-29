from django.db import models
# Create your models here.


class Campaign(models.Model):
    structure_value = models.CharField(max_length=250, null=True, blank=True, verbose_name="Structure Value")
    status = models.CharField(max_length=250, null=True, blank=True, verbose_name="Status")

    class Meta:
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'

    def __str__(self):
        return str(self.id)


class AdGroup(models.Model):
    campaign = models.ForeignKey(Campaign, null=True, blank=True, on_delete=models.SET_NULL,
                                 verbose_name="Connected Campaign")
    alias = models.CharField(max_length=250, null=True, blank=True, verbose_name="Alias")
    status = models.CharField(max_length=250, null=True, blank=True, verbose_name="Status")

    class Meta:
        verbose_name = 'AdGroup'
        verbose_name_plural = 'AdGroups'

    def __str__(self):
        return str(self.id)


class SearchTerm(models.Model):
    date = models.DateField(null=True, blank=True, verbose_name='Date')
    ad_group = models.ForeignKey(AdGroup, null=True, blank=True, on_delete=models.SET_NULL,
                                 verbose_name="Connected Ad Group")
    campaign = models.ForeignKey(Campaign, null=True, blank=True, on_delete=models.SET_NULL,
                                 verbose_name="Connected Campaign")
    click = models.IntegerField(null=True, blank=True, verbose_name="Click Amount")
    cost = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name="Cost")
    conversion_value = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2,
                                           verbose_name="Conversion Value")
    conversion = models.IntegerField(null=True, blank=True, verbose_name="Conversion")
    search_term = models.CharField(max_length=250, null=True, blank=True, verbose_name="Search Term")

    class Meta:
        verbose_name = 'Search Term'
        verbose_name_plural = 'Search Terms'

    def __str__(self):
        return str(self.id)
