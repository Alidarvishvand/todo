from django.urls import path
from django.views.generic import TemplateView
from .views import IndexTemplate,PostListView
from .views import remove

urlpatterns = [
    # path('',index,name='index'),
    path('', IndexTemplate.as_view(template_name="index.html"), name='index'),
    path('postlist/',PostListView.as_view(template_name="blog/post_list.html"), name='post'),
    path('del/<str:item_id>',remove, name="del"),
]