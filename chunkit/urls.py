from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path("home", views.home, name="home"),
path("register", views.register, name="register"),
path("download/<str:file_id>", views.download, name="download"),
path("login", views.sign_in, name="login"),
path("faq", views.faq, name="faq"),
path("send", views.send, name="send"),
path("", views.landing_page, name="landing_page"),
path("about", views.about, name="about"),

# ******************* RESET PASSWORD VIEW *****************************
path('password_reset', auth_views.PasswordResetView.as_view(
    template_name='reset_password.html'), name='password_reset'),
path('password_reset_done', auth_views.PasswordResetDoneView.as_view(
    template_name='reset_password_done.html'), name='password_reset_done'),
path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name='reset_password_confirm.html'), name='password_reset_confirm'),
path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
    template_name='reset_password_complete.html'), name='password_reset_complete'),

# ******************* ADMIN PAGE VIEW *****************************
path("admin_home", views.admin_home, name="admin_home"),
path("message", views.message, name="message"),
path("user", views.user, name="user"),
path("subscribe", views.subscribe, name="subscribe"),
path("file", views.file, name="file"),
path("admin_login", views.admin_login, name="admin_login"),
path("signout", views.signout, name="signout"),

]