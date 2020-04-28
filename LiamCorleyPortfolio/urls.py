#LIAM CORLEY \\ 2020
#Project urls

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    #host/portfolio -> Portfolio App
    path('portfolio/', include('Portfolio.urls')),
    #host/ -> Portfolio App
    path('', include('Portfolio.urls')),
    #host/admin -> Django Admin
    path('admin/', admin.site.urls),
]

#Add static and media paths
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)