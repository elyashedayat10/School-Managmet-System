from django.shortcuts import render, get_object_or_404, redirect
from .models import AcademicYear
from .forms import AcademicYearForm
from django.views.generic import CreateView, ListView, View
from django.urls import reverse_lazy
from institute.models import Institute


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
        obj=AcademicYear.objects.filter(institute=institute_id)
        return render(request, 'academicyear/institute.html', {'object': obj})
