from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("create/", views.create_post, name="create"),
    path("delete/<int:post_id>/", views.delete_post, name="delete"),
    path("<int:post_id>/", views.detail, name="detail"),
]
