#model class that stores Roas values of all search term

from django.db import models
from search_terms.models import Search_Terms

# Create your models here.

class Roas(models.Model):
    search_id = models.ForeignKey(
        Search_Terms,
        on_delete= models.CASCADE
    )
    search_term= models.TextField()
    total_cost= models.IntegerField()
    total_conversion_value= models.IntegerField()
    roas= models.FloatField()

    class Meta:
        ordering= ['-roas']