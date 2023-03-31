from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import CustomUser
from app1.forms import CustomUserForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['user'] = CustomUser.objects.all()
        return context


class CustomUserFormView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('index')
    template_name = 'registration.html'


class CustomUserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')




