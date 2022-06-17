from django.urls import path

from .views import (InstituteCreateView, InstituteDeleteView,
                    InstituteDetailView, InstituteListView,
                    InstituteUpdateView, TodayView, MonthView, UnpaidView, TotalView, YearInstallmentView)

app_name = "institute"

urlpatterns = [
    path("list", InstituteListView.as_view(), name="list"),
    path("detail/<int:id>/", InstituteDetailView.as_view(), name="detail"),
    path("delete/<int:institute_id>/", InstituteDeleteView.as_view(), name="delete"),
    path("update/<int:id>/", InstituteUpdateView.as_view(), name="update"),
    path("create/", InstituteCreateView.as_view(), name="create"),
    path("today/<int:Institute_id>/", TodayView.as_view(), name="today"),
    path("month/<int:Institute_id>/", MonthView.as_view(), name="month"),
    path("unpaid/<int:Institute_id>/", UnpaidView.as_view(), name="unpaid"),
    path("total/<int:Institute_id>/", TotalView.as_view(), name="total"),
    path('<int:year>/archive/', YearInstallmentView.as_view(), name='archive')
]
