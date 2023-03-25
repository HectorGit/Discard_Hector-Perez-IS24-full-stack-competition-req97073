from django.db import models

from django.contrib.postgres.fields import ArrayField

from datetime import datetime


# Create your models here.

# A SAMPLE SCHEMA GIVEN IS : 
    # {
    #     productId: VALUE,
    #     productName: VALUE,
    #     productOwnerName: VALUE,
    #     Developers: [
    #      "NAME_1",
    #      "NAME_2",
    #      "NAME_3",
    #      "NAME_4",
    #      "NAME_5"
    #     ],
    #     scrumMasterName: VALUE,
    #     startDate: "YYYY/MM/DD",
    #     methodology: VALUE
    # }

class Product(models.Model):
    #id will be auto-generated by django upon new insertion
    product_name = models.CharField(max_length=50)
    product_owner_name = models.CharField(max_length=50)
    #TODO : Find a way to have multiple developer names. In postgres, ArrayField can be used, but since I'm using the default sqlite database, that is not allowed
    developer_name = models.CharField(max_length=50)
    scrum_master_name = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=datetime.now) #check syntax
    methodology = models.CharField(max_length=50)

    #check syntax
    def __str__(self):
            return self.product_name + self.start_date