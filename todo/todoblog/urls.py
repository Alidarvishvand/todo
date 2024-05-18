from django.urls import path
from django.views.generic import TemplateView
from .views import index,remove

urlpatterns = [
    path('',index,name='index'),
    path('', TemplateView.as_view(template_name="index.html")),
    path('del/<str:item_id>',remove, name="del"),
]