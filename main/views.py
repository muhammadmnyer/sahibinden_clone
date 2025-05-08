from django.http import HttpResponse,JsonResponse
from .models import Categories,Subcategories,Products,SubcategoriesChildParentRelation
from . import utils
import json

def fetch_categories_info(request):

    if request.method == "GET":
        response = {
            "categories":[]
        }
    
        
        for category in Categories.objects.all():

            response['categories'].append({

                "category_id":category.category_id,
                "category_name":category.category_name,
                "subcategories":[]
                
                })


            for subcategory in Subcategories.objects.filter(category=category):
                response['categories'][-1]['subcategories'].append(utils.subcategories_json_builder(subcategory))

        
        return JsonResponse(response)
    return HttpResponse(status=405)

def fetch_products(request):
    params = request.GET
    category_path = params.get('category_path',None)
    products  = Products.objects.filter(path=category_path)
    
    return JsonResponse([product.toJson() for product in products],safe=False)



