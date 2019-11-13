from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', include('selia_admin.urls')),
    url(r'^autocomplete/', include(('irekua_autocomplete.urls', 'irekua_autocomplete')))
]
