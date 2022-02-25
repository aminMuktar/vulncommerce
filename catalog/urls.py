from django import views
from django.urls import path
from . import views



urlpatterns = [
    # category
    path('category/',views.CategoryApiView.categoryList,name='Category'),
    path('category/detail/<int:pk>/',views.CategoryApiView.categoryDetail,name='Detail'),
    path('category/create/',views.CategoryApiView.categoryCreate,name='Create'),
    path('category/update/<int:pk>',views.CategoryApiView.categoryUpdate,name='Update'),
    path('category/delete/<int:pk>',views.CategoryApiView.categoryDelete,name='Delete'),

    # product
    path('product/',views.ProductApiView.productList,name='Product'),
    path('product/detail/<int:pk>/',views.ProductApiView.productDetail,name='Detail'),
    path('product/create/',views.ProductApiView.productCreate,name='Create'),
    path('product/update/<int:pk>',views.ProductApiView.productUpdate,name='Update'),
    path('product/delete/<int:pk>',views.ProductApiView.productDelete,name='Delete'),
]