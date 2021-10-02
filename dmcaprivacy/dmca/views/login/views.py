import jsonpickle
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from jsonpickle import json
from django.db.models import Sum

from ...models import Nicks, Clients, Plans, GoogleReports, TubePages, TubeReports
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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        client = Clients.objects.get(user=self.request.user.id)
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for e in GoogleReports.objects.filter(clients_id_clie=client.id_clie):
                    encode_reports = jsonpickle.encode(e, unpicklable=False)
                    reports_json = json.loads(encode_reports)
                    dest = {}
                    dest.update(reports_json)
                    for a in Nicks.objects.filter(clients_id_clie=e.clients_id_clie):
                        encodenicks = jsonpickle.encode(a, unpicklable=False)
                        nicksjson = json.loads(encodenicks)
                        dest.update(nicksjson)
                    data.append(dest)

            else:
                data['error'] = 'An error has occurred'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        client = Clients.objects.get(user=self.request.user.id)
        google = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', clients_id_clie=client.id_clie) \
            .aggregate(Sum('cant_urls_gore'))
        content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', clients_id_clie=client.id_clie) \
            .aggregate(Sum('cant_urls_gore'))
        tubes = TubeReports.objects.filter(clients_id_clie_id=client.id_clie).aggregate(Sum('cant_urls'))
        total = google['cant_urls_gore__sum'] + content['cant_urls_gore__sum'] + tubes['cant_urls__sum']

        context = super().get_context_data(**kwargs)
        context['title'] = 'List of Google Reports'
        context['list_url'] = reverse_lazy('manage_reports')
        context['entity'] = 'GoogleReports'
        context['nicks'] = GoogleReports.objects.filter()
        context['name_tube_page'] = TubeReports.objects.filter()
        context['total'] = total
        context['images'] = google
        context['content'] = content
        context['tubes'] = tubes

        # google_reports = GoogleReports.objects.filter(clients_id_clie=client.id_clie)
        # tube_reports = TubeReports.objects.filter(clients_id_clie_id=client.id_clie)
        # client.date_joined

        return context
