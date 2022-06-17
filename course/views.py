from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, FormView, ListView,
                                  UpdateView, View)

from extenstion.mixins import AdminUserMixin
from student.models import Student

from .filters import CourseFilter
from .forms import CourseCreateForm, CourseUpdateForm
from .models import Course

# Create your views here.


class CourseListView(AdminUserMixin, ListView):
    template_name = "course/list.html"
    context_object_name = "filter"

    def get_queryset(self):
        course_list = CourseFilter(self.request.GET, queryset=Course.objects.all())
        return course_list


class CourseDetailView(AdminUserMixin, DetailView):
    model = Course
    template_name = "course/detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"


class CourseCreateView(CreateView):
    model = Course
    template_name = "course/create.html"
    success_url = reverse_lazy("Course:List")
    form_class = CourseCreateForm


class CourseUpdateView(AdminUserMixin, UpdateView):
    model = Course
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "course/update.html"
    form_class = CourseUpdateForm

    def get_success_url(self):
        return reverse("Course:detail", kwargs=[self.object.id])


class CourseDeleteView(AdminUserMixin, View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        return redirect("Course:List")


class CourseParticipationAdd(View):
    def get(self, request, course_id, student_id):
        student = get_object_or_404(Student, id=student_id)
        course = get_object_or_404(Course, id=course_id)
        course.participation.add(student)
        course.save()
        return redirect(request.META.get("HTTP_REFERER", "/"))
