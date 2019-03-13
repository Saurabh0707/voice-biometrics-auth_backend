from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from backendApp import views

admin.autodiscover()
router = routers.DefaultRouter()

urlpatterns = [
    # url(r'^api/client/(?P<username>[\w-]+)/$', views.ClientDetail.as_view()),
    # url(r'^api/client/(?P<pk>[\w-]+)/$', views.ClientDetail.as_view()),
    # url(r'^api/client/$', views.ClientList.as_view()),
    url(r'^api/user/(?P<pk>[\w-]+)/$', views.UserDetail.as_view()),
    url(r'^api/user/$', views.UserList.as_view()),      
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]