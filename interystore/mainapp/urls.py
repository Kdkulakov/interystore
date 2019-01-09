from django.urls import path, re_path
from mainapp.views import products, detail, contacts, main
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', main, name='main'),
    re_path(r'^detail/$', detail, name='detail'),
    re_path(r'^products/$', products, name='products'),
    re_path(r'^catalog/category/(\d+)/$', products, name='catalog'),
    re_path(r'^contacts/$', contacts, name='contacts'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)