from django.urls import path

from .views import *

urlpatterns = [
    path('',  ResearchIndex.as_view(), name='research-index'),
    path('article_detail/<int:pk>/', ResearchPostDetail.as_view(), name='research-detail'),

]
app_name = 'research'
