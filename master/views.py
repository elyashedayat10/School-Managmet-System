from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)

from extenstion.mixins import AdminUserMixin

from .forms import MasterForm
from .models import Master

# Create your views here.


class MasterListView(ListView):
    model = Master
    template_name = "master/list.html"


class MasterDetailView(AdminUserMixin, DetailView):
    model = Master
    template_name = "master/detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"


class MasterCreateView(CreateView):
    model = Master
    template_name = "master/create.html"
    success_url = reverse_lazy("Master:List")
    form_class = MasterForm


class MasterUpdateView(AdminUserMixin, UpdateView):
    model = Master
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "master/update.html"
    form_class = MasterForm

    def get_success_url(self):
        return reverse("Master:Detail", args=[self.kwargs.get("id")])


class MasterDeleteView(AdminUserMixin, View):
    def get(self, request, master_id):
        master = get_object_or_404(Master, id=master_id)
        master.delete()
        return redirect("Master:List")
