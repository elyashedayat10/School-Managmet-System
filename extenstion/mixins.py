from django.http import Http404
from django.shortcuts import redirect


class AdminUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_anonymous:
            return redirect('account:login')

        if request.user.is_student:
            return redirect('Student:profile')
        return super(AdminUserMixin, self).dispatch(request, *args, **kwargs)


class SuperuserMixin:
    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_anonymous:
            return redirect('account:login')

        if request.user.is_student:
            return redirect('Student:profile')
        return super(SuperuserMixin, self).dispatch(request, *args, **kwargs)
