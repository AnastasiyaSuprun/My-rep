from django.conf import settings
from django.conf.urls.static import static

from mainapp.views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('owners-list/', owners_list, name='owners'),
    path('pets-list/', pets_list, name='pets'),
    path('shelters-list/', shelters_list, name='shelters'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('sign-up/', sign_up, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
