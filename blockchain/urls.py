from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name = "home"),
    path('balanceEth/',views.balance,name="balance"),
    path('txn/',views.txn,name="txn")
]