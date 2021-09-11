from django.urls import path
from api import views 
from api import restviews
urlpatterns = [
    #####################-- NORMAL METHODS --####################################
    path('movie_list/', views.movie_list ,name= "list_items"),
    path('movie_details/<int:id>/', views.movie_details_id ,name= "item_details"),
    path('delete_movie/<int:id>/', views.delete_movie_id ,name= "delete_item"),
    path('create_movie/', views.create_movie_id ,name= "create_item"),
    path('update_movie/<int:id>/', views.update_movie_id ,name= "update_item"),
    #####################-- REST FRAMEWORK --####################################
    path('movie_list_rest/', restviews.movie_list_rest ,name= "movie_list_rest"),
    path('movie_list_pk/<int:id>', restviews.movie_rest_pk ,name= "movie_list_rest"),
]    
