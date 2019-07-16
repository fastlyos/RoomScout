from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.forms.utils import ErrorList
from .models import House

class house_create(LoginRequiredMixin, generic.CreateView):
    model = House
    fields = []
    template_name = 'houses/house_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(house_create, self).form_valid(form)
        return redirect('home')

class house_detail(generic.DetailView):
    model = House
    template_name = 'houses/house_detail.html'

class house_edit(LoginRequiredMixin, generic.UpdateView):
    model = House
    template_name = 'houses/house_edit.html'
    fields = ['title']
    success_url = reverse_lazy('home')

    def get_object(self):
        hall = super(UpdateHall, self).get_object()
        if not hall.user == self.request.user:
            raise Http404
        return hall

class house_delete(LoginRequiredMixin, generic.DeleteView):
    model = House
    template_name = 'houses/house_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        hall = super(DeleteHall, self).get_object()
        if not hall.user == self.request.user:
            raise Http404
        return hall
