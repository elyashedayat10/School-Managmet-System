from django import template
from ..models import SiteSetting

register = template.Library()


@register.inclusion_tag('config/site_setting_check.html')
def setting_show():
    able = True
    site_setting_count = SiteSetting.objects.count()
    if site_setting_count > 0:
        able = False
    return {'able': able}
