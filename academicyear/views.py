from django.shortcuts import render, get_object_or_404, redirect
from .models import AcademicYear
from .forms import AcademicYearForm
from django.views.generic import CreateView, ListView, View
from django.urls import reverse_lazy
from institute.models import Institute
from student.models import Installment

# Create your views here.


class AcademicYearCreateView(CreateView):
    model = AcademicYear
    form_class = AcademicYearForm
    success_url = reverse_lazy('academic_year:list')
    template_name = 'academicyear/create.html'


class AcademicYearListView(ListView):
    model = AcademicYear
    template_name = 'academicyear/list.html'


class AcademicYearDeleteView(View):
    def get(self, request, pk):
        academic_year = get_object_or_404(AcademicYear, pk=pk)
        academic_year.delete()
        return redirect('')


class InstituteAcademicYearView(View):
    def get(self, request, *args, **kwargs):
        institute_id = kwargs.get('id')
        institute_name=get_object_or_404(Institute,id=institute_id)
        obj=AcademicYear.objects.filter(institute=institute_id)
        return render(request, 'academicyear/institute.html', {'object': obj,'institute':institute_name})
from django.db.models import  Sum,Count

class PaidBaseOnYearInstitute(View):
    def get(self,request,institute_id,year):
        institute_obj=Institute.objects.get(id=institute_id)
        installment_pay=Installment.objects.filter(institute_id=institute_id,academic_year_id=year)
        total_pay=installment_pay.aggregate(Sum('amount'))['amount__sum'] or 0
        installment_count=installment_pay.aggregate(Count('id'))['id__count']
        paid=installment_pay.filter(paid=True).aggregate(Sum('amount'))['amount__sum'] or 0
        unpaid=installment_pay.filter(paid=False).aggregate(Sum('amount'))['amount__sum'] or 0
        return render(request,'academicyear/pay_archive.html',{
            'total':installment_pay,'paid':paid,'unpaid':unpaid,'total_pay':total_pay,'count':installment_count,"institute_obj":institute_obj})
