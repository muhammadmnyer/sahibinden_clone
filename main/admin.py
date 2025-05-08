from django.contrib import admin
from .models import Categories,Subcategories,Products,SubcategoriesChildParentRelation
from .admin_forms import ProductAdminForm

class CategoriesView(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')  
    search_fields = ('category_name',)
    

class SubcategoriesView(admin.ModelAdmin):
    list_display = ('subcategory_id','subcategory_name','category',)
    list_filter = ('category',)
    
    

class ProductsView(admin.ModelAdmin):
    
    form = ProductAdminForm 
    list_display = ('product_id','product_name','product_description','product_price','product_external_info','image','path')
    search_fields = ('product_name',)

    
class SubcategoriesChildParentRelationView(admin.ModelAdmin):
    list_display = ('id','parent','child')
    list_filter = ('parent','child')



admin.site.register(Categories, CategoriesView)
admin.site.register(Subcategories, SubcategoriesView)
admin.site.register(Products, ProductsView)
admin.site.register(SubcategoriesChildParentRelation,SubcategoriesChildParentRelationView)