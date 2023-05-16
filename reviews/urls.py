from django.urls import path
from . import views


app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category_type>', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('product_detail/<int:data_id>', views.product_detail, name='product_detail'),
    path('create/<int:data_id>/', views.create, name='create'),
    path('detail/<int:data_id>/delete/', views.product_delete, name='product_delete'),
    path('detail/<int:data_id>/delete/<int:review_pk>/', views.product_delete, name='review_delete'),
    path('update/<int:data_id>/', views.product_update, name='product_update'),
    path('detail/<int:data_id>/update/<int:review_pk>/', views.review_update, name='review_update'),
    path('detail/<int:data_id>/detail/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('detail/<int:data_id>/like/<int:review_pk>/', views.review_like, name='review_like'),
]
