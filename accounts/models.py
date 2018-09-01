from django.db import models
from users.models import AccountHolder
from uuid import uuid4

ACCOUNT_TYPE = (
	('c', 'Cheques'),
	('n', 'Nómina'),
	('a', 'Ahorro'),
	('i', 'Inversión'),
)

class Account(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	account_type = models.CharField(max_length=150, choices=ACCOUNT_TYPE, default='a')
	owner = models.ForeignKey(AccountHolder, on_delete=models.CASCADE)
	balance = models.FloatField()

	def __str__(self):
		return '{} - {}'.format(self.account_type, self.owner)
