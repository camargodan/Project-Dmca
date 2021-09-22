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
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                worker = User.objects.get(id=self.request.user.id)
                client = Clients.objects.filter(worker_id=worker.id)

                for i in client:
                    plan = Plans.objects.get(id_plan=i.plan_id)
                    print(plan.plan)

                    data.append(i.toJSON())

            elif action == 'edit':
                pag = Nicks.objects.get(id_nick=request.POST['id_nick'])
                pag.delete()

            else:
                data['error'] = 'An error has occurred'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of Clients assigned to you'
        context['list_url'] = reverse_lazy('list_clients')
        context['entity'] = 'Clients'
        return context
