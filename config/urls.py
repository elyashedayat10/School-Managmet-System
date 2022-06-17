from django.urls import path

from .views import PanelView, SiteSettingCreateView, SiteSettingUpdateView, SiteSettingView

app_name = "Config"

urlpatterns = [
    path("", PanelView.as_view(), name="Panel"),
    path("create/", SiteSettingCreateView.as_view(), name="create"),
    path("update/<int:id>/", SiteSettingUpdateView.as_view(), name="update"),
    path("site_setting/", SiteSettingView.as_view(), name="setting"),
]
