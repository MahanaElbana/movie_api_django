from .models import Movie
from django.contrib import admin
# Register your models here.

admin.site.register(Movie)

"""
url :- 
 - Endpoint
 - data body 
 - header statuscode
 - metthod CRED
pillow 
watchmat --> project
watchlist-app --> api
python manage.py runserver 8899
"""
"""       
                          serialization           dictionary
 python_cmplex_dataType   =============>  (python native data type)    ===>  json 

           parse          dictionary          De-serialization
 json    =========> (python native data type) ==============> python_cmplex_dataType
"""
'''
types of serializetion :- 
  1] serializers.Serializer
  2] serializers.ModelSerializer

types of views :- 
  1] function based views 
      @api_view

  2] class based views 
      ApiView 
        generic views
        mixins
        viewSets
        concrete class view

 Working with API :-        
        DRF(django rest framework) Browsable API
        postman
        httpie
        thunder client   ==> package in vscode ==> from extensions
https://pypi.org/project/httpie-django-auth/
'''