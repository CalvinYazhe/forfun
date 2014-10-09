from django.conf.urls import patterns, include, url
from bms.views import *

urlpatterns = patterns('',
	url(r'^$', index),
	url(r'list_server/$', index),
	url(r'add_server/$', add_server.as_view()),
	url(r'delete_server/$', delete_server.as_view()),
	url(r'add_layer/$', add_layer.as_view()),
	url(r'^detail/(?P<layer_id>\d+)/$', layer_detail),
	url(r'server_detail/(?P<pk>\d+)/$', server_detail.as_view()),
	url(r'layer_add_server/(?P<layer_id>\d+)/$', layer_add_server.as_view()),
	#url(r'api/(?P<server_id>\d+)/$', api),
	url(r'api/$', api),

	)