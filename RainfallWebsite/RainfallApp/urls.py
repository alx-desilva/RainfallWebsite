from django.urls import path
from . import views

app_name = "RainfallApp"

urlpatterns = [
    # Create a path object defining the URL pattern to the index view
    path(route='', view=views.index, name='index'),
    path(route='use/', view=views.calculation_page, name='use'),
    path(route='login/', view=views.login_request, name='login'),
    path(route='signup/', view=views.registration_request, name='registration'),
    path(route='logout/', view=views.logout_request, name='logout'),
    #path(route='create/', view=views.create_equation, name='create'),"""
]