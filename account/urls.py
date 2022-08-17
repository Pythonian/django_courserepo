from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
     # Access     
     path('logout/',
          auth_views.LogoutView.as_view(), name='logout'),
     path('login/',
          auth_views.LoginView.as_view(
               redirect_authenticated_user=True), name='login'),

     # Account activation
     path('activation/sent/',
          views.account_activation_sent,
          name='account_activation_sent'),
     path('activate/<uidb64>/<token>/',
          views.activate,
          name='activate'),

     # password reset with email
     path('password_reset/',
          auth_views.PasswordResetView.as_view(
               success_url=reverse_lazy('account:password_reset_done')),
          name='password_reset'),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
          name='password_reset_done'),
     path('password_reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(
               success_url=reverse_lazy('account:password_reset_complete')),
          name='password_reset_confirm'),
     path('password_reset/complete/',
          auth_views.PasswordResetCompleteView.as_view(),
          name='password_reset_complete'),

     # password change
     path('password_change/', views.CustomPasswordChangeView.as_view(),
          name='password_change'),

     path('signup/', views.signup, name='signup'),
     path('profile/', views.profile, name='profile'),
     path('settings/', views.settings, name='settings'),
]
