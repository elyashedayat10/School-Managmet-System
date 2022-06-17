from .models import SiteSetting


def site_setting_info(request):
    return {'site_setting_obj': SiteSetting.objects.first()}
