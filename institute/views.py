from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)
from django.views.generic.edit import FormMixin

from course.forms import InstituteCourseForm

from .forms import InstituteForm
from .models import Institute

from student.models import Installment


class InstituteListView(ListView):
    model = Institute
    template_name = "institute/list.html"


import datetime


class InstituteDetailView(FormMixin, DetailView):
    model = Institute
    template_name = "institute/detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"
    form_class = InstituteCourseForm

    def get_context_data(self, **kwargs):
        context_data = super(InstituteDetailView, self).get_context_data(**kwargs)
        context_data['date'] = datetime.date
        # while datetime.date.year> datetime.date.year:
        #     context_data[f'date+{1}']=datetime.date
        return context_data

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("institute:detail", args=[self.kwargs.get("id")])

    def form_valid(self, form):
        new_course = form.save(commit=False)
        new_course.institute = self.object
        new_course.save()
        print("ok" * 90)
        messages.success(self.request, "", "")
        return super(InstituteDetailView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "", "")
        return super(InstituteDetailView, self).form_invalid(form)


class InstituteCreateView(CreateView):
    model = Institute
    success_url = reverse_lazy("institute:list")
    form_class = InstituteForm
    template_name = "institute/create.html"


class InstituteUpdateView(UpdateView):
    model = Institute
    form_class = InstituteForm
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "institute/update.html"
    success_url = reverse_lazy("institute:list")

    def get_success_url(self):
        return reverse("institute:detail", args=[self.kwargs.get("id")])


class InstituteDeleteView(View):
    def get(self, request, institute_id):
        institute = get_object_or_404(Institute, id=institute_id)
        institute.delete()
        return redirect("institute:list")


import datetime


class TodayView(View):
    def get(self, request, Institute_id):
        installment = Installment.objects.filter(institute_id=Institute_id).filter(date=datetime.date.today())
        return render(request, 'institute/today.html', {'installment_list': installment})


class MonthView(View):
    def get(self, request, Institute_id):
        print(datetime.datetime.today().month)
        installment = Installment.objects.filter(institute_id=Institute_id).filter(
            date__month=datetime.datetime.today().month)
        return render(request, 'institute/month.html', {'installment_list': installment})


class UnpaidView(View):
    def get(self, request, Institute_id):
        installment = Installment.objects.filter(institute_id=Institute_id).filter(paid=False).filter(
            date=datetime.date.today())
        return render(request, 'institute/unpaid.html', {'installment_list': installment})


from django.db.models import Sum


class TotalView(View):
    def get(self, request, Institute_id):
        installment = Installment.objects.filter(institute_id=Institute_id).filter(
            date__year=datetime.datetime.today().year).aggregate(Sum("amount"))["amount__sum"]
        return render(request, 'institute/', {'installment_list': installment})


from django.views.generic.dates import YearArchiveView


class YearInstallmentView(View):
    def get(self,request,year):
        return render(request,'institute/year_archive.html',{'object_list':Installment.objects.filter(date__year=year)})

