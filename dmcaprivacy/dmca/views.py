from bootstrap_modal_forms.generic import BSModalCreateView
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from .forms import UserEditForm, PlanCreateForm
from .models import Plans
from .mixins import SuperuserRequired


User = get_user_model()


class LoginView(LoginRequiredMixin, TemplateView):
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


class ManagePlans(ListView):
    model = Plans
    template_name = 'dmca/admin/manage_plans.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Plans.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías FLAGGGGGGGGG'
        context['create_url'] = reverse_lazy('create_plan')
        context['list_url'] = reverse_lazy('manage_plans')
        context['entity'] = 'Plans'
        return context


class CreatePlan(LoginRequiredMixin, SuperuserRequired, BSModalCreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    form_class = PlanCreateForm
    template_name = 'dmca/admin/create_plan.html'
    success_message = 'Success: Created successfully.'
    success_url = reverse_lazy('manage_plans')
