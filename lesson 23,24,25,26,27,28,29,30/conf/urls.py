
from django.contrib import admin
from django.urls import path, include
from conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += i18n_patterns(
    path('', include('shop.urls'))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)