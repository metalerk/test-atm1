from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
import uuid
from .models import Account

class ViewAllBalances(TemplateView):
	template_name = 'accounts/balances.html'

	def get_context_data(self, **kwargs):
		context = super(ViewAllBalances, self).get_context_data(**kwargs)
		context.update({'queryset': Account.objects.all()})
		# context['queryset'] = Account.objects.all()
		return context

class WithdrawMoney(TemplateView):
	template_name = 'accounts/withdraw.html'

	def get_context_data(self, **kwargs):
		context = super(WithdrawMoney, self).get_context_data(**kwargs)
		return context

	def dispatch(self, request, msg=None, *args, **kwargs):
		print(self.request.META['REMOTE_ADDR'])
		if msg is not None:
			messages.set_level(request, messages.INFO)
			messages.add_message(self.request, messages.INFO, msg)
		else:
			pass

		return super(WithdrawMoney, self).dispatch(request, *args, **kwargs)

class WithdrawAction(RedirectView):
	url = '/'

	def post(self, request, *args, **kwargs):
		account_number = self.request.POST['account_number']
		qty = int(self.request.POST.get('qty'))

		# SELECT * FROM Account WHERE id = account_number;
		account = Account.objects.get(id=account_number)

		if account.balance >= qty:
			total = qty
			m_1000 = 0
			m_500 = 0
			m_100 = 0
			m_50 = 0

			if qty // 1000 > 0:
				m_1000 = qty // 1000
				qty -= m_1000 * 1000

			if qty // 500 > 0:
				m_500 = qty // 500
				qty -= m_500 * 500

			if qty // 100 > 0:
				m_100 = qty // 100
				qty -= m_100 * 100

			if qty // 50 > 0:
				m_50 = qty // 50
				qty -= m_50 * 50

			account.balance -= total
			account.save()
			money = '1000: {}, 500: {}, 100: {}, 50: {}'.format(m_1000, m_500, m_100, m_50)
			return redirect(reverse('accounts:main', kwargs={}))
		else:
			money = 'You poor hahahaha'
			return redirect(reverse('accounts:main', kwargs={}))
