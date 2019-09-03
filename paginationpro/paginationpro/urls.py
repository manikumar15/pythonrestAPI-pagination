from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from paginationapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('paginationapp.urls')),
]

