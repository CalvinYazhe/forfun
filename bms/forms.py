from django import forms
from bms.models import Layer, Server
from django.shortcuts import get_object_or_404

class LayerForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):	
		super(LayerForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Layer

class ServerForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ServerForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Server