from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)
from django.views.generic.edit import FormMixin
import random
import datetime
from course.models import Course
from extenstion.send_sms import send_message
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import StudentFilter
from .forms import (GradeForm, MajorForm, StudentForm, StudentInstallmentForm,
                    StudentSelectForm, StudentGradeUpdateForm, StudentInstallmentHandForm)
from .models import Grade, Installment, Major, Student
from dateutil.relativedelta import relativedelta

user = get_user_model()


class StudentListView(ListView):
    template_name = "student/list.html"
    context_object_name = "filter"

    def get_queryset(self):
        student_list = StudentFilter(self.request.GET, queryset=Student.objects.all())
        return student_list


class StudentDetailView(DetailView):
    model = Student
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "student/detail.html"

    def get_context_data(self, **kwargs):
        context_data = super(StudentDetailView, self).get_context_data(**kwargs)
        context_data["course_list"] = Course.objects.all()
        return context_data


class StudentDeleteView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect("")


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("Student:list")
    template_name = "student/create.html"

    def form_valid(self, form):
        new_form = form.save(commit=False)
        cd = form.cleaned_data
        user_obj = user.objects.create_user(
            national_code=cd["national_code"],
            first_name=cd["first_name"],
            last_name=cd["last_name"],
            phone_number=cd["phone_number"],
            password=cd['national_code'],
        )
        user_obj.is_student = True
        user_obj.save()
        new_form.user = user_obj
        new_form.save()
        messages.success(self.request, "", "btn btn-success")
        return super(StudentCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "", "btn btn-danger")
        return super(StudentCreateView, self).form_invalid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("Student:list")
    template_name = "student/update.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_initial(self):
        initial = super().get_initial()
        initial['phone_number'] = self.object.user.phone_number
        initial['last_name'] = self.object.user.last_name
        initial['first_name'] = self.object.user.first_name
        initial['national_code'] = self.object.user.national_code
        return initial



    def form_invalid(self, form):
        new_form = form.save(commit=False)
        user_obj = get_object_or_404(user, id=self.kwargs.get("id"))
        new_form.user = user_obj
        new_form.save()
        messages.success(self.request, "", "btn btn-success")
        return super(StudentUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        messages.success()
        return super(StudentUpdateView, self).form_valid(form)


class GradeListView(ListView):
    model = Grade
    template_name = "student/grade_list.html"


class GradeDetailView(FormMixin, DetailView):
    model = Grade
    template_name = "student/grade_detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"
    form_class = MajorForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("Student:grade_detail", args=[self.kwargs.get("id")])

    def form_valid(self, form):
        new_major = form.save(commit=False)
        new_major.grade = self.object
        new_major.save()
        print("ok" * 90)
        messages.success(self.request, "", "")
        return super(GradeDetailView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "", "")
        return super(GradeDetailView, self).form_invalid(form)


class MajorCreateView(CreateView):
    model = Major
    success_url = reverse_lazy("config:Panel")
    form_class = MajorForm

    def form_valid(self, form):
        id_ = self.kwargs.get("id")
        print(id_)
        return super(MajorCreateView, self).form_valid(form)


class GradeCreateView(CreateView):
    form_class = GradeForm
    template_name = "student/grade_create.html"
    success_url = reverse_lazy("Student:grade_list")

    def form_valid(self, form):
        messages.success(self.request, "پایه با موفقیت اضافه شد", "btn btn-success")
        return super(GradeCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "خطلا دز اقزودن پایه", "btn btn-danger")
        return super(GradeCreateView, self).form_invalid(form)


class GradeUpdateView(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = "student/grade_update.html"
    success_url = reverse_lazy("Student:grade_list")
    slug_field = "id"
    slug_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(
            self.request, "به روزرسانی با موفقیت انجام شد", "btn btn-success"
        )
        return super(GradeUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "خطلا دز به روزرسانی", "btn btn-danger")
        return super(GradeUpdateView, self).form_invalid(form)


class GradeDeleteView(View):
    def get(self, request, grade_id):
        grade = get_object_or_404(Grade, id=grade_id)
        grade.delete()
        messages.success(request, "پایه با موفقیت حذف شد", "btn btn-success")
        return redirect("Student:grade_list")


from django.db.models import Sum


class InstallmentCreateView(View):
    template_name = "student/installment.html"
    form_class = StudentInstallmentForm

    def setup(self, request, *args, **kwargs):
        self.student = get_object_or_404(Student, id=kwargs.get('student_id'))
        super(InstallmentCreateView, self).setup(request, *args, **kwargs)

    def get(self, request, student_id):
        return render(request, self.template_name, {"form": self.form_class, 'object': self.student})

    def post(self, request, student_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            last_year = self.student.academic_year.last()
            cd = form.cleaned_data
            installment_list = []
            date = datetime.date.today()
            user_installment = Installment.objects.filter(student_id=self.student.id, academic_year=last_year)
            if user_installment:
                last_installment = user_installment.last()
                pay = user_installment.all().aggregate(Sum('amount'))['amount__sum']
                remain = self.student.total_pay - pay
                if remain != 0:
                    installment_count = remain // cd['count']
                    for i in range(cd["count"]):
                        month_later = relativedelta(months=i + 1)
                        installment_list.append(
                            Installment(student=self.student, amount=installment_count,
                                        code=random.randint(111111, 999999),
                                        date=last_installment.date + month_later, institute=self.student.institute,
                                        academic_year=self.student.academic_year.last())
                        )
                    Installment.objects.bulk_create(installment_list)
                    messages.success(request, "قسط بندی با موفقیت انجام شد", "btn btn-success")
                    return redirect("Student:detail", student_id)
                messages.success(request, "مبلغ قایل قسط بنذی نمیباشد", "btn btn-danger")
                return redirect("Student:detail", student_id)

            else:
                installment_count = self.student.total_pay // cd["count"]
                for i in range(cd["count"]):
                    month_later = relativedelta(months=i + 1)
                    installment_list.append(
                        Installment(student=self.student, amount=installment_count, code=random.randint(111111, 999999),
                                    date=date + month_later, institute=self.student.institute,
                                    academic_year=self.student.academic_year.last())
                    )
                Installment.objects.bulk_create(installment_list)
                messages.success(request, "قسط بندی با موفقیت انجام شد", "btn btn-success")
                return redirect("Student:detail", student_id)
        messages.error(request, "خطا در انجام عملیات", "btn btn-danger")
        return render(request, self.template_name, {"form": self.form_class})


class InstallmentHandyCreateView(View):
    template_name = "student/installmenthand.html"
    form_class = StudentInstallmentHandForm

    def setup(self, request, *args, **kwargs):
        self.student = get_object_or_404(Student, id=kwargs.get('student_id'))
        super(InstallmentHandyCreateView, self).setup(request, *args, **kwargs)

    def get(self, request, student_id):
        return render(request, self.template_name, {"form": self.form_class, 'object': self.student})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            student_installment = self.student.installment.filter(academic_year=self.student.academic_year.last()).aggregate(Sum('amount'))['amount__sum']
            if student_installment:
                date_of_last = student_installment.last()
                pay_date = date_of_last + relativedelta(months=+1)
                Installment.objects.create(amount=form.cleaned_data['amount'], student_id=self.student.id,
                                       institute=self.student.institute, code=random.randint(111111, 999999),
                                       date=pay_date,paid_date=pay_date,paid=True)
                return redirect("Student:detail", self.student.id)
            else:
                pay_date = datetime.date.today()
                Installment.objects.create(amount=form.cleaned_data['amount'], student_id=self.student.id,
                                           institute=self.student.institute, code=random.randint(111111, 999999),
                                           date=pay_date,paid_date=pay_date)
                return redirect("Student:detail", self.student.id)
        # else:
        #     return redirect("Student:detail", self.student.id)
        return render(request, self.template_name, {'form': self.form_class, 'object': self.student})


class StudentInstallmentListView(ListView):
    template_name = 'student/student_installment_list.html'

    def get_queryset(self):
        student = get_object_or_404(Student, id=self.kwargs.get('student_id'))
        object_list = student.installment.all()
        return object_list


class StudentInstallmentUpdateView(View):
    def get(self, request, installment_id):
        installment = get_object_or_404(Installment, id=installment_id)
        installment.paid = True
        installment.paid_date = datetime.date.today()
        installment.save()
        messages.success(request, '', 'success')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class StudentSelectView(View):
    form_class = StudentSelectForm
    template_name = "student/select.html"

    def get(self, request):
        return render(request, self.template_name, {"form": StudentSelectForm})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            student_list = []
            model_qs = cd["student"]
            print(cd["student"])
            for topping in cd['student']:
                obj = get_object_or_404(Student, id=topping.id)
                student_list.append(obj)
            # send_message(form.cleaned_data['message'],, )
            # for obj in model_qs:
            #     model_obj = Student.objects.get(id=obj.id)
            #     model_obj.grade = cd["grade"]
            #     student_list.append(model_obj)
            # Student.objects.bulk_update(student_list, ["grade"])
            # messages.success(request, "به روزرسانی با موفقیت انجام شد", "btn btn-success")
            print(student_list)
            return redirect("Student:list")


from .forms import MajorSmsForm, StudentSmsForm, ClassSmsForm


class StudentClassSmsSendView(View):
    def get(self, request):
        return render(request, 'student/sms.html', {'form': ClassSmsForm()})

    def post(self, request):
        course = request.POST.get('course')
        course_obj = Course.objects.get(id=int(course))
        course_student = course_obj.participation.all()
        for student in course_student:
            student_info = Student.objects.get(id=student.id)
            send_message(student_info.user.phone_number, request.POST.get('text'))
        return redirect('config:Panel')


class StudentSmsSendOnlyView(View):
    def get(self, request):
        return render(request, 'student/sms1.html', {'form': StudentSmsForm()})

    def post(self, request):
        request.POST.get('student')
        for i in request.POST.get('student'):
            student_phone = Student.objects.get(id=int(i))
            send_message(student_phone.user.phone_number, request.POST.get('text'))
        return redirect('config:Panel')


class StudentSmsSendMajorView(View):
    def get(self, request):
        return render(request, 'student/sms2.html', {'form': MajorSmsForm()})

    def post(self, request):
        grade, major = request.POST.get('grade'), request.POST.get('major')
        student_list = Student.objects.filter(grade_id=int(grade), major_id=int(major))
        for student in student_list:
            student_info = Student.objects.get(id=student.id)
            send_message(student_info.user.phone_number, request.POST.get('text'))
        return redirect('config:Panel')


class MajorDeleteView(View):
    def get(self, request, major_id):
        major_obj = get_object_or_404(Major, id=major_id)
        major_obj.delete()
        messages.success(request, '', '')
        return redirect('Student:list')


class MajorUpdateView(UpdateView):
    model = Major
    form_class = MajorForm
    success_url = reverse_lazy('config:Panel')
    template_name = "student/major_update.html"
    slug_field = 'id'
    slug_url_kwarg = 'major_id'


class StudentGradeUpdate(View):
    form_class = StudentGradeUpdateForm
    template_name = 'student/student_grade_update.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            former = cd['former']
            to_grade = cd['to_grade']
            update_list = []
            model_qs = Student.objects.filter(grade=former)
            for obj in model_qs:
                model_obj = Student.objects.get(id=obj.id)
                model_obj.grade = to_grade
                update_list.append(model_obj)
            Student.objects.bulk_update(update_list, ['grade'])
            messages.success(request, '', '')
            return redirect()
        messages.error()
        return render(request, self.template_name, {'form': form})


class StudentProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_obj = get_object_or_404(Student, id=self.request.user.student.id)
        return render(request, 'student/profile.html', {"object": user_obj})


class UploadStudentProfileView(UpdateView):
    model = Student
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'student/image_upload.html'
    fields = ('image',)
    success_url = reverse_lazy('Student:profile')
