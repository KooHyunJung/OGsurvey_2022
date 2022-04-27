from django.urls import path
from user import views


app_name = "user"

urlpatterns = [
    path("login", views.admin_page_login, name="login"),
    path("logout", views.admin_page_logout, name="logout"),
]
