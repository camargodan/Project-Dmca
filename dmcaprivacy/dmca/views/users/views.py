from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from ...mixins import SuperuserRequired
from ...forms import UserEditForm, UserStatus


class CustomEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, ImageFieldFile):
            return obj.url
        return super(CustomEncoder, self).default(obj)


User = get_user_model()


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


class ManageUsers(ListView, SuperuserRequired):
    model = User
    template_name = "dmca/admin/manage_users.html"
    form_class = UserStatus

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
                for i in User.objects.all():
                    data.append(i.toJSON())
            elif action == 'edit':
                use = User.objects.get(pk=request.POST['id'])
                use.is_active = request.POST.get('is_active', False)
                use.is_superuser = request.POST.get('is_superuser', False)
                use.is_worker = request.POST.get('is_worker', False)
                use.is_client = request.POST.get('is_client', False)
                use.save()
            else:
                data['error'] = 'An error has occurred'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, encoder=CustomEncoder, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of user register in the App. FLAG'
        context['list_url'] = reverse_lazy('manage_users')
        context['entity'] = 'User'
        context['form'] = UserStatus()
        return context
