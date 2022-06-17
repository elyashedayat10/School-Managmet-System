from django.urls import path

from .views import (CourseCreateView, CourseDeleteView, CourseDetailView,
                    CourseListView, CourseParticipationAdd, CourseUpdateView)

app_name = "Course"

urlpatterns = [
    path("list/", CourseListView.as_view(), name="List"),
    path("create/", CourseCreateView.as_view(), name="Create"),
    path("update/<int:id>/", CourseUpdateView.as_view(), name="Update"),
    path("delete/<int:id>/", CourseDeleteView.as_view(), name="Delete"),
    path("detail/<int:id>/", CourseDetailView.as_view(), name="Detail"),
    path(
        "course_participation_add/<int:course_id>/<int:student_id>/",
        CourseParticipationAdd.as_view(),
        name="participation_add",
    ),
]
