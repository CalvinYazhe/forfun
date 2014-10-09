from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import os

from bms.models import Server, Layer

# Create your views here.

def index(request):
	Server_list = Server.objects.all()
	Layer_list = Layer.objects.all()
	return render_to_response('bms/server_list.html', {'Server_list': Server_list, 'Layer_list': Layer_list})
	#model = {Server, Layer}
	#context_object_name = {'Server_list', 'Layer_list'}

class add_server(CreateView):
	model = Server
	fields = ['ServerName', 'WlanAddress', 'LanAddress']
	template_name = 'bms/server_form.html'
	success_url = "/bms/list_server"

class delete_server(DeleteView):
	model = Server
	#fields = ['ServerName', 'WlanAddress', 'LanAddress', 'UseFor']
	#template_name = 'bms/server_form.html'
	success_url = "/bms/list_server"

class add_layer(CreateView):
	model = Layer
	template_name = 'bms/server_form.html'
	success_url = "/bms/list_server"

def layer_detail(request, layer_id):
	p = get_object_or_404(Layer, pk=layer_id)
	Layer_list = Layer.objects.all()
	return render_to_response('bms/layer_detail.html', {'server_list': p, 'Layer_list': Layer_list})

class layer_add_server(CreateView):
	model = Server
	fields = ['ServerName', 'WlanAddress', 'LanAddress', 'UseFor']
	template_name = 'bms/server_form.html'
	success_url = "/bms/list_server"

	def form_valid(self, form):
	   	p = Layer.objects.get(pk = self.kwargs['layer_id'])
	   	form.instance.Layer = p
		return super(layer_add_server, self).form_valid(form)

class server_detail(UpdateView):
	model = Server
	success_url = "/bms/list_server"

def api(request):
	WlanAddress = request.POST.get('WlanAddress')
	LanAddress = request.POST.get('LanAddress')
	result = os.popen("ssh calvin@192.168.0.30 'dmesg'").read()
	return render_to_response('bms/dmesg_info.html', {'WlanAddress': WlanAddress, 'LanAddress': LanAddress, 'info': result})
