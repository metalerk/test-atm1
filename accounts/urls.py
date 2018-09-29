from django.urls import re_path, path
from .views import ViewAllBalances, WithdrawAction, WithdrawMoney

app_name = 'accounts'
urlpatterns = [
    path('', ViewAllBalances.as_view(), name='main'),
    #re_path(r'^msg/(?P<msg>\w+)/$', ViewAllBalances.as_view(), name='main'),
    path('withdraw_action/', WithdrawAction.as_view(), name='withdraw_redirect'),
    path('withdraw/', WithdrawMoney.as_view(), name='withdraw'),
]