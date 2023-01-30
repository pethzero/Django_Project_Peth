"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including anot  her URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'rapper', RapperViewSet)
router.register(r'blog', BlogViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^home/', home, name='home'),
    url(r'^login/', login, name='login'),
    url(r'^logout/',logout, name='logout'),
    url(r'^check_login/', check_login, name='check_login'),
    url(r'^loginv1/',loginv1, name='loginv1'),

     url(r'^loginv1/',loginv1, name='loginv1'),
    # url(r'^home/', home, name='home'),
    # url(r'^simple_upload/', simple_upload, name='simple_upload'),
    # url(r'^model_form_upload/', model_form_upload, name='model_form_upload'),
    url(r'^blog/(?P<pk>\d+)$', blog_detail, name='blog'),
    url(r'^profile/', profile, name='profile'),
    # #API
    # url(r'^api', include(router.urls)),
    # url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^apitest', apitest, name='apitest'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
