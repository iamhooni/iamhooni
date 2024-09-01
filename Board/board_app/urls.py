from django.urls import path
from . import views
#from . views import *

# Create your views here.
urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post/<int:id>', views.detail, name='detail'),
    path('post/edit/<int:id>', views.Edit, name='edit'),
    path('post/delete/<int:id>', views.Delete, name='delete'), 
]
