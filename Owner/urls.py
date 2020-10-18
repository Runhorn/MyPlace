from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from MyPlace import settings
from django.conf.urls.static import static
from . import views

app_name = 'owner'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)