from django.urls import path

from .views import *

urlpatterns = [
    path('',  research_list, name='research-index'),

]
app_name = 'research'
