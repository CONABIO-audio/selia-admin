from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include('selia_admin.urls')),
    url(r'^autocomplete/', include(('irekua_autocomplete.urls', 'irekua_autocomplete')))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
