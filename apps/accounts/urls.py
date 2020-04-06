from django.urls import path

from apps.accounts.views import ActivateUserView

urlpatterns = [
    path('activate/<uidb64>/<token>/', ActivateUserView.as_view(), name='account_activate')
]
