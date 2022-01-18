#
from django.conf import settings
from django.conf.urls.static import static
#from django import urls
from django.conf import settings
#from django.conf.urls import url
from django.conf.urls.static import static
#from django.conf.urls import urls
#from django.views.static import serve
#
from django import contrib
from django.contrib import admin
from django.urls import path, include

from todo.settings import MEDIA_ROOT, MEDIA_URL

#

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^uploads/(?<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


