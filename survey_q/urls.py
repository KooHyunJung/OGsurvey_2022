from django.urls import path
from survey_q import views


app_name = "survey_q"

urlpatterns = [
    path("", views.survey_create, name="create"),
    path("list", views.survey_list, name="list"),
    # path("update", views.survey_update, name="update"),
    # path("delete", views.survey_delete, name="delete"),
    path("information/<int:pk>", views.survey_information, name="info"),
]