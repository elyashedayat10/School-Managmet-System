from django.urls import path

from .views import (
    AcademicYearCreateView, AcademicYearListView, AcademicYearDeleteView,InstituteAcademicYearView
)

app_name = 'academic_year'
urlpatterns = [
    path('list/', AcademicYearListView.as_view(), name='list'),
    path('create/', AcademicYearCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', AcademicYearDeleteView.as_view(), name='delete'),
    path('institute/<int:id>/',InstituteAcademicYearView.as_view(),name='institute_academic')
]
