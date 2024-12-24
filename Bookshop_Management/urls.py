from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar  # Corrected import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookapp.urls')),
    path('auth', include('App_login.urls')),
]

# Add Django Debug Toolbar URLs only when in DEBUG mode
if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),  # Add the debug toolbar URLs to the pattern list
    ] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files
