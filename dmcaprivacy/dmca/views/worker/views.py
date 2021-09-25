from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from ...forms import NicksCreateForm, NickEditForm
from ...models import Nicks, Clients, Pages, NicksPages, Plans
from ...mixins import SuperuserRequired
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import jsonpickle
# from django.apps import apps
# User = apps.get_model('accounts', 'User')
from django.contrib.auth import get_user_model
User = get_user_model()


class ListClients(ListView, LoginRequiredMixin):
    model = Clients
    template_name = 'dmca/worker/list_clients.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        data2 = {}
        worker = User.objects.get(id=self.request.user.id)
        client = Clients.objects.filter(worker_id=worker.id)
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []

                for i in client:
                    encode_client = jsonpickle.encode(i, unpicklable=False)
                    client_json = json.loads(encode_client)

                    name = User.objects.values('first_name', 'last_name').get(id=i.user_id)
                    plan = Plans.objects.get(id_plan=i.plan_id_id)

                    encode_name = jsonpickle.encode(name, unpicklable=False)
                    name_json = json.loads(encode_name)
                    encode_plan = jsonpickle.encode(plan, unpicklable=False)
                    plan_json = json.loads(encode_plan)

                    dest = {}
                    dest.update(client_json)
                    dest.update(name_json)
                    dest.update(plan_json)
                    dic = {'nick_pages': [],
                           }
                    dest.update()

                    for e in client:
                        for a in Nicks.objects.filter(clients_id_clie=e.id_clie):
                            encodenicks = jsonpickle.encode(a, unpicklable=False)
                            nicksjson = json.loads(encodenicks)
                            pages_nicks = Nicks.objects.get(id_nick=a.id_nick).pages.all()

                            for s in pages_nicks:
                                encodepages = jsonpickle.encode(s, unpicklable=False)
                                pagesjson = json.loads(encodepages)
                                dic['nick_pages'].append({
                                    'nick': a.nick,
                                    'name_page': s.name_page,
                                    'prio': a.prio,
                                })
                            dest.update(dic)
                    data.append(dest)
            else:
                data['error'] = 'An error has occurred here here here'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of Clients assigned to you'
        context['list_url'] = reverse_lazy('list_clients')
        context['entity'] = 'Clients'
        return context
