from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category_type>', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('product_detail/<int:data_id>', views.product_detail, name='product_detail'),
    path('detail/<int:data_id>/delete/', views.product_delete, name='product_delete'),
    path('create/<int:data_id>/', views.create, name='create'),
    # path('update/<int:data_id>/', views.product_update, name='product_update'),
    path('review_delete/<int:review_pk>/', views.review_delete, name='review_delete'),
    path('review_update/<int:review_pk>/', views.review_update, name='review_update'),
    path('review_detail/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('review_like/<int:review_pk>/', views.review_like, name='review_like'),
    path('comment_create/<int:review_pk>/', views.comment_create, name='comment_create'),
    path('comment_like/<int:review_pk>/<int:comment_pk>', views.comment_like, name='comment_like'),
    path('comment_delete/<int:review_pk>/<int:comment_pk>', views.comment_delete, name='comment_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
