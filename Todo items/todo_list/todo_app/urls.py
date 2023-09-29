
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.homePage),
    path('deleteItem/<slug:id>',views.delete)
]