from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from MyPlace import settings
from django.conf.urls.static import static
from . import views

app_name = 'Estates'

urlpatterns = [
    url(r'^$', views.estate_list, name='list'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)