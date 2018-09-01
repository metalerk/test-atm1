from django.contrib import admin
from .models import Account

def stole(modeladmin, request, queryset):
	queryset.update(balance=0)

stole.short_description = 'Robar'

class AccountAdmin(admin.ModelAdmin):
	actions = (stole,)
	list_display = ('id', 'owner', 'account_type', 'balance',)

admin.site.register(Account, AccountAdmin)