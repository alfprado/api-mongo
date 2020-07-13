from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('authors', views.author_list),
    path('authors/<int:pk>', views.author_detail),
    path('news', views.news_list),
    path('news/<int:pk>', views.news_detail),
    path('admin/', admin.site.urls),
]