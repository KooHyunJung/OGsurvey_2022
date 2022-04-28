from django.urls import path
from survey_a import views


app_name = "survey_a"

urlpatterns = [
    path("detail/<int:pk>", views.send_survey_detail, name="detail"),
]
