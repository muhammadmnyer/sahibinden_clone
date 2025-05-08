from . import views
from django.urls import path


urlpatterns = [
    path('categories/',views.fetch_categories_info),
    path('products/',views.fetch_products),
]
