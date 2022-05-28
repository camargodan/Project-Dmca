from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from ...forms import NicksCreateForm, NickEditForm
from ...models import Nicks, Clients
from ...mixins import SuperuserRequired

import json
import jsonpickle


class NickEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    model = Nicks
    form_class = NickEditForm
    template_name = 'dmca/client/edit_nick.html'
    success_message = '%(nick)s was edited successfully'
    success_url = reverse_lazy('manage_nicks')


class AddNicks(CreateView):
    model = Nicks
    form_class = NicksCreateForm
    template_name = 'dmca/client/add_nicks.html'
    success_url = reverse_lazy('manage_nicks')

    def form_valid(self, form):
        client = Clients.objects.get(user=self.request.user.id)
        form.instance.clients_id_clie = client
        return super(AddNicks, self).form_valid(form)


class ManageNicks(ListView, SuperuserRequired):
    model = Nicks
    template_name = 'dmca/client/manage_nicks.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            client = Clients.objects.get(user=self.request.user.id)
            if action == 'searchdata':
                data = []

                for i in Nicks.objects.filter(clients_id_clie=client.id_clie):
                    encodenicks = jsonpickle.encode(i, unpicklable=False)
                    nicksjson = json.loads(encodenicks)
                    pages_nicks = Nicks.objects.get(id_nick=i.id_nick).pages.all()
                    for a in pages_nicks:
                        encodepages = jsonpickle.encode(a, unpicklable=False)
                        pagesjson = json.loads(encodepages)
                        dest = {}
                        dest.update(nicksjson)
                        dest.update(pagesjson)
                        data.append(dest)

            elif action == 'delete':
                pag = Nicks.objects.get(id_nick=request.POST['id_nick'])
                pag.delete()

            else:
                data['error'] = 'An error has occurred'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of Nicks with correspond page'
        context['list_url'] = reverse_lazy('manage_nicks')
        context['entity'] = 'Nicks'
        context['form'] = NicksCreateForm()
        return context
