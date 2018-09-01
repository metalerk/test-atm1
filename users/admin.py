from django.contrib import admin
from .models import AccountHolder

class AccountHolderAdmin(admin.ModelAdmin):
	pass

admin.site.register(AccountHolder, AccountHolderAdmin)