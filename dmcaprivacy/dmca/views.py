from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .forms import UserEditForm
from .models import Plans
from .mixins import SuperuserRequired
User = get_user_model()


class Loginview(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    template_name = 'dmca/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return HttpResponseRedirect('administrator')
        elif request.user.is_worker:
            return HttpResponseRedirect('worker')
        else:
            return HttpResponseRedirect('client')
        return super(TemplateView, self).get(request, *args, **kwargs)


class Administrator(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    template_name = 'dmca/administrator.html'


class Worker(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    template_name = 'dmca/worker.html'


class Client(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    template_name = 'dmca/client.html'


class UserEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    model = User
    form_class = UserEditForm
    template_name = 'dmca/pages/edit_user.html'
    success_message = '%(first_name)s was edited successfully'

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

    def get_success_url(self):
        return reverse('edit_user', kwargs={'slug': self.object.slug})


class ManageUsers(LoginRequiredMixin, SuperuserRequired, ListView):
    """docstring for ."""
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    model = User
    template_name = "dmca/admin/manage_users.html"


class ManagePlans(LoginRequiredMixin, SuperuserRequired, ListView):
    model = Plans
    template_name = 'dmca/admin/manage_plans.html'



