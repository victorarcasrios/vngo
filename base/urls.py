from django.conf.urls import patterns, url
from base import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^objects/$', views.objects_list),
	url(r'^objects/categories/(?P<category_name>\w+)/$', views.objects_list),
	url(r'^objects/(?P<object_id>\d+)/$', views.object_detail)
)