from django.urls import path  ,include

# ------------------- ----- ------ ------ ------ ---- to get token 
from rest_framework.authtoken.views import obtain_auth_token
# ------------------- ----- ------ ------ ------ ---- to get token

#from api import views 
from api import restviews
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('StreamApi',restviews.StreamApi, basename="StreamApi")
router.register('watchApi', restviews.WatchApi ,basename= "watchApi")
router.register('RewviewApi', restviews.RewviewApi ,basename= "RewviewApi")

urlpatterns = [
    #####################-- NORMAL METHODS --####################################
    #path('movie_list/', views.movie_list ,name= "list_items"),
    #path('movie_details/<int:id>/', views.movie_details_id ,name= "item_details"),
    #path('delete_movie/<int:id>/', views.delete_movie_id ,name= "delete_item"),
    #path('create_movie/', views.create_movie_id ,name= "create_item"),
    #path('update_movie/<int:id>/', views.update_movie_id ,name= "update_item"),
    #####################-- REST FRAMEWORK --####################################
    #path('movie_list_rest/', restviews.movie_list_rest ,name= "movie_list_rest"),
    #path('movie_list_pk/<int:id>', restviews.movie_rest_pk ,name= "movie_list_rest"),
    path('modelviewset/', include(router.urls)),
    path('stream/<int:pk>/reviewList/',restviews.ReviewList.as_view() ,name="review-list"),
    path('stream/<int:pk>/reviewCreate/',restviews.ReviewCreate.as_view() ,name="review-list"),
  

    # to return response include token by using login 
    path('login/',obtain_auth_token), # -- POST --
    #{"username":"Admin","password":"Django123"}
    path('regestration/',restviews.regestration), 
    path('logout/',restviews.logout ,name="log_out"), 
  ]    
