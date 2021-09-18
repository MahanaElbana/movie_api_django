
## #from api.models import Movie
## from django.http import JsonResponse 
## import json

## #####################-- NORMAL METHODS --####################################
## # GET method
## def movie_list(request):
#    movie = Movie.objects.all()
#    data  = {'movies':list(movie.values())} 
#    return JsonResponse(data)
## 
## # retrive method
## def movie_details_id(request ,id):
#    '''   get(pk=id)     or    get(id=id)   '''
#    movie = Movie.objects.get(pk=id) # return object
#    #print(movie)
#    data  = {'name':movie.name,'description':movie.description,'active':movie.active} 
#    return JsonResponse(data)   
#
## # DELETE method
## def delete_movie_id(request ,id):
#    '''   get(pk=id)     or    get(id=id)   '''
#    movie = Movie.objects.get(pk=id) # return object
#    try :
#     if 'TRIPLEM' in json.loads(request.body):
#       movie.delete()
#       return JsonResponse({movie.name:"deleted"}) 
#    except: return JsonResponse({"Autherization":"enter your password"}) 
## 
## # POST method
## def create_movie_id(request):
#   
#    '''   get(pk=id)     or    get(id=id)   '''
#    movie = Movie() # return object
#    data = json.loads(request.body) # decode or parse 
#    if "name" in data and "description" in  data and "active" in data:
#        movie.name =data["name"]
#        movie.description =data["description"]
#        movie.active =data["active"]
#        movie.save()
#        dataMovie = {
#            'name':movie.name,'description':movie.description,'active':movie.active
#            } 
#        return JsonResponse(dataMovie) 
#    
#    return JsonResponse({"error !":"all data required"})      
## 
## # Update method
### def update_movie_id(request ,id):
#   
#    '''   get(pk=id)     or    get(id=id)   '''
#    movie = Movie.objects.get(pk=id) # return object
#    data = json.loads(request.body) # decode or parse 
#    
#    if "name" in data and "description" in  data and "active" in data:
#        movie.name =data["name"]
#        movie.description =data["description"]
#        movie.active =data["active"]
#        movie.save()
#        dataMovie = {
#            'name':movie.name,'description':movie.description,'active':movie.active
#            } 
#        return JsonResponse(dataMovie) 
#    
#    return JsonResponse({"error !":"all data required"})
