from django.conf import settings
from django.conf.urls.static import static

from mainapp.views import *
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('owners-list/', owners_list, name='owners'),
    path('pets-list/', pets_list, name='pets'),
    path('pets-list/add-pet/', add_pet, name='add_pet'),
    path('shelters-list/', shelters_list, name='shelters'),
    path('auth/', include('authentication.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
