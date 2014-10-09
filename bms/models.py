from django.db import models

# Create your models here.


class Layer(models.Model):
	LayerName = models.CharField(max_length=150)

	def __unicode__(self):
		return self.LayerName

class Server(models.Model):
	ServerName = models.CharField(max_length=150)
	WlanAddress = models.IPAddressField()
	LanAddress = models.IPAddressField()
	UseFor = models.CharField(max_length=200, default="Null")
	Notification = models.BooleanField(default=True)
	Layer = models.ForeignKey(Layer, default='1')

	def __unicode__(self):
		return self.ServerName