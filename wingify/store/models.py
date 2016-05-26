from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


class OnlineStore(models.Model):
	"""
	Create model for online store
	"""
	name = models.CharField(max_length=128)
	address = models.CharField(max_length=500)
	phone_no = models.CharField(max_length=10)
	email_id = models.EmailField(max_length=100, null=True, blank=True)
	user = models.OneToOneField(User, db_index=True)
	

	def __unicode__(self):
		return self.name


class Products(models.Model):
	"""
	Create model for products
	"""
	name = models.CharField(max_length = 128)
	sku_id = models.CharField(max_length = 128, db_index = True)
	quantity = models.IntegerField()
	store_id = models.ForeignKey(OnlineStore, db_index = True)
	price = models.IntegerField()
	is_active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.sku_id


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	"""
	Post save signal on user to create a token when user is created
	"""
	if created:
		token = Token.objects.create(user=instance)
		print (token.key)
	return True







