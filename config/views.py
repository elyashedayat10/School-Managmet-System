from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Avg, Max, Min
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View

from course.models import Course
from extenstion.mixins import SuperuserMixin
from institute.models import Institute
from master.models import Master
from student.models import Grade, Student

from .forms import SiteSettingForm
from .models import IPAddress, SiteSetting

user = get_user_model()


# Create your views here.


class PanelView(SuperuserMixin, View):
    def get(self, request):
        context = {
            "student_count": Student.objects.values("id").count(),
            "master_count": Master.objects.values("id").count(),
            "institute_count": Institute.objects.values("id").count(),
            "admin_count": user.objects.filter(is_admin=True).values("id").count(),
            "course_count": Course.objects.values("id").count(),
            "grade_count": Grade.objects.values("id").count(),
            "average_participation_course": Course.objects.aggregate(
                result=Avg("participation")
            )["result"],
            "less_participation_course": Course.objects.annotate(
                result=Min("participation")
            ),
            "most_participation_course": Course.objects.annotate(
                result=Max("participation")
            ),
        }
        return render(request, "config/panel.html", context)


class SiteSettingCreateView(SuperuserMixin, CreateView):
    template_name = "config/create.html"
    form_class = SiteSettingForm
    model = SiteSetting
    success_url = reverse_lazy("config:Panel")
    #
    # def dispatch(self, request, *args, **kwargs):
    #     ip_address = self.request.user.ip_address
    #     if IPAddress.objects.all().count() < 1:
    #         IPAddress.objects.create(ip_address=ip_address)
    #         return super(SiteSettingCreateView, self).dispatch(request, *args, **kwargs)
    #     raise Http404

    def form_valid(self, form):
        messages.success(self.request, "", "")
        return super(SiteSettingCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "", "")
        return super(SiteSettingCreateView, self).form_invalid(form)


class SiteSettingUpdateView(SuperuserMixin, UpdateView):
    template_name = "config/update.html"
    form_class = SiteSettingForm
    model = SiteSetting
    success_url = reverse_lazy("config:setting")
    slug_field = "id"
    slug_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request, "", "")
        return super(SiteSettingUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "", "")
        return super(SiteSettingUpdateView, self).form_invalid(form)


class SiteSettingView(View):
    def get(self, request):
        site_setting_obj = SiteSetting.objects.first()
        return render(request, 'config/site_setting.html', {'object': site_setting_obj})
