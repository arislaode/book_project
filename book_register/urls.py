
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.book_form, name='book_insert'),
    path('<int:id>/', views.book_form, name='book_update'),
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
    path('list/', views.book_list, name='book_list'),
    path('review/', views.review_form, name='review'),
    path('review-list/', views.review_list, name='review_list'),
    path('api/order/', views.review_list, name='review_list')
]