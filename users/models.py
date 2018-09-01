from django.db import models
from django.conf import settings

class AccountHolder(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.user)