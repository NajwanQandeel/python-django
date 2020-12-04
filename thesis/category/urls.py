from django.urls import path
from category.views import CategoryList

app_name='category'


urlpatterns=[
    path('',CategoryList.as_view())
 ]
