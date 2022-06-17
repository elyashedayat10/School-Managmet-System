from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View
# from .mixins import AccessMixin
from extenstion.mixins import SuperuserMixin

from .forms import AdminCreateForm, AdminUpdateForm, PassChangeForm

user = get_user_model()
# from django.contrib.auth.mixins import

# Create your views here.


class UserLoginView(View):
    template_name = "account/login.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super(UserLoginView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect("config:Panel")

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = authenticate(
            request,
            national_code=request.POST.get("national_code"),
            password=request.POST.get("password"),
        )
        if user:
            login(request, user)
            messages.success(request, "با موفقیت وارد حساب خود شدید", "btn btn-success")
            if user.is_admin:
                return redirect("config:Panel")
            return redirect("Student:profile")
        else:
            messages.error(request, "هیچ کاربری یا این اطلاعات وجود ندارد")
        return render(request, self.template_name)


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "با موفقیت از حساب خود خارح شدید")
        return redirect("account:login")


# admin views
class AdminListView(SuperuserMixin, ListView):
    queryset = user.objects.filter(is_admin=True)
    template_name = "account/admin_list.html"


class AdminCreateView(SuperuserMixin, CreateView):
    model = user
    form_class = AdminCreateForm
    template_name = "account/admin_create.html"
    success_url = reverse_lazy("account:admin_list")

    def form_valid(self, form):
        new_admin = form.save(commit=False)
        new_admin.is_admin = True
        new_admin.save()
        messages.success(self.request, "ادمین با موفقیت اضافه شد", "info")
        return super(AdminCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "خطا در وزود اطلاعات", "danger")
        return super(AdminCreateView, self).form_invalid(form)


class AdminUpdateView(SuperuserMixin, UpdateView):
    model = user
    form_class = AdminUpdateForm
    template_name = "account/admin_update.html"
    success_url = reverse_lazy("account:admin_list")

    def form_valid(self, form):
        messages.success(
            self.request, "به روزرسانی با موفیت انحام شد", "btn btn-success"
        )
        return super(AdminUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "خطلا در بروزرسانی", "btn btn-danger")
        return super(AdminUpdateView, self).form_invalid(form)


class AdminDetailView(SuperuserMixin, DetailView):
    model = user
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "account/admin_detail.html"


class UserDeleteView(SuperuserMixin, View):
    def get(self, request, user_id):
        user_obj = get_object_or_404(user, id=user_id)
        user_obj.delete()
        messages.success(request, "ادمین مورد نظر با موفقیت حذف شد", "btn btn-success")
        return redirect("account:admin_list")


class PassChangeView(PasswordChangeView):
    template_name = "account/password_change.html"
    success_url = reverse_lazy("account:password_change_done")
    form_class = PassChangeForm


class PassChangeDoneView(PasswordChangeDoneView):
    def dispatch(self, request, *args, **kwargs):
        previous_path = request.META.get("HTTP_REFERER")
        if previous_path == "account:change_password":
            return super(PassChangeDoneView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(request.META.get("HTTP_REFERER"))

    template_name = "account/password_change_done.html"
