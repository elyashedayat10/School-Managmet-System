from django.urls import path

from .views import (MasterCreateView, MasterDeleteView, MasterDetailView,
                    MasterListView, MasterUpdateView)

app_name = "Master"

urlpatterns = [
    path("", MasterListView.as_view(), name="List"),
    path("<int:id>/", MasterDetailView.as_view(), name="Detail"),
    path("update/<int:id>/", MasterUpdateView.as_view(), name="Update"),
    path("delete/<int:master_id>/", MasterDeleteView.as_view(), name="Delete"),
    path("create/", MasterCreateView.as_view(), name="Create"),
]
