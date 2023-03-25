from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from product.serializers import ProductSerializer
from product.models import Product
from datetime import datetime

from product.models import Product #check syntax
import random #used to generate random numbers

class PopulateDatabaseWithDummyData(APIView):
    """
    PopulateDatabaseWithDummyData
    """
    def get(self, request):

        #creating placeholder personas to randomly insert into newly created product object
        product_names = ["Initiative","Project","Enterprise","Solution"]
        product_owners = ["Bob","Bill","Buck","Brent"]
        developers = ["Mark","Robert","Frank","Chris"]
        scrum_masters = ["Alexander","Alfred","Aaron","Anthony"]
        methodologies = ["Waterfall","Agile","Kanban","Scrum"]

        #complete and check syntax (pseudocode)

        for i in range(5):

            #TODO : Currently the developer list required is simplified to just -one- developer name. Must find a way around this
            product_data = {
                "product_name" : product_names[random.randint(0,len(product_names)-1)] + str(i),
                "product_owner_name" : product_owners[random.randint(0,len(product_owners)-1)],
                "developer_name" : developers[random.randint(0,len(developers)-1)],
                "scrum_master_name" : scrum_masters[random.randint(0,len(scrum_masters)-1)],
                "start_date" : datetime.now(),
                "methodology" : methodologies[random.randint(0,len(methodologies)-1)]
            }

            print("product data to insert into db : ", product_data)

            serializer = ProductSerializer(data=product_data)
            serializer.is_valid(raise_exception=True)
            serializer.save() #this should insert the product into the database, to verify run /product/

        return Response({"Status":"Completed Execution of PopulateDatabaseWithDummyData"})


# Respond w/ Status = 200 to show server application is healthy
class HealthCheck(APIView):
    """
    HealthCheck
    """
    def get(self, request):

        return Response({"Status":"Completed Execution of PopulateDatabaseWithDummyData"})
