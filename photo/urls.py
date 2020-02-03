from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^images/(\d+)', views.images, name = 'images'),
    url(r'^locations/(\d+)', views.display_by_location, name = 'display_by_location'),
    url(r'^category/(\d+)', views.display_by_category, name = 'display_by_category'),
    url(r'^search/', views.search_image, name = 'search_image')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
