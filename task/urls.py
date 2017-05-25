from django.conf.urls import url
from task import views

# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^all$', views.all_task, name="all_task"),
    url(r'(?P<id>[-\d]+)$', views.task, name="task"),
]
