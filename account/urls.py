from django.urls import path

from .views import (
    AdminCreateView,
    AdminDetailView,
    AdminListView,
    AdminUpdateView,
    PassChangeDoneView,
    PassChangeView,
    UserDeleteView,
    UserLoginView,
    UserLogoutView,
)

app_name = "account"
urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("admin_create/", AdminCreateView.as_view(), name="admin_create"),
    path("admin_update/<int:id>/", AdminUpdateView.as_view(), name="admin_update"),
    path("admin_list/", AdminListView.as_view(), name="admin_list"),
    path("admin_detail/<int:id>/", AdminDetailView.as_view(), name="admin_detail"),
    path("delete/<int:user_id>/", UserDeleteView.as_view(), name="delete"),
    path("password_change/", PassChangeView.as_view(), name="password_change"),
    path(
        "password_change_done/",
        PassChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
