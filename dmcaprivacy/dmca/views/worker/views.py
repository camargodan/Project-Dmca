from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from ...forms import AddReport, AddTube
from ...models import Nicks, Clients, Plans, GoogleReports, TubePages, TubeReports
from ...mixins import SuperuserRequired
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import jsonpickle
from django.contrib import messages
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


class AddGoogleReports(CreateView, SuperuserRequired):
    model = GoogleReports
    form_class = AddReport
    template_name = 'dmca/worker/add_google_report.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        try:
            report = GoogleReports()
            nick = Nicks.objects.get(nick=request.POST['nick'])
            report.clients_id_clie = nick.clients_id_clie
            report.date_gore = request.POST['date_gore']
            report.id_clai_gore = request.POST['id_clai_gore']
            report.type_clai_gore = request.POST['type_clai_gore']
            report.urls_gore = request.POST['urls_gore']
            number = len(report.urls_gore.splitlines())
            report.cant_urls_gore = number
            report.save()

            messages.success(request, 'Report uploaded successfully')
            return HttpResponseRedirect('google_reports')
        except Exception as e:
            messages.error(request, e)

        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a new Google Report'
        context['list_url'] = reverse_lazy('worker')
        context['entity'] = 'GoogleReports'
        context['nicks'] = Nicks.objects.values_list('nick', flat=True)
        return context


class ManageGoogleReports(ListView, SuperuserRequired):
    model = GoogleReports
    template_name = 'dmca/worker/manage_reports.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        worker = User.objects.get(id=self.request.user.id)
        client = Clients.objects.filter(worker_id=worker.id)
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in client:
                    for e in GoogleReports.objects.filter(clients_id_clie=i.id_clie):
                        encode_reports = jsonpickle.encode(e, unpicklable=False)
                        reports_json = json.loads(encode_reports)
                        dest = {}
                        dest.update(reports_json)
                        for a in Nicks.objects.filter(clients_id_clie=e.clients_id_clie):
                            encodenicks = jsonpickle.encode(a, unpicklable=False)
                            nicksjson = json.loads(encodenicks)
                            dest.update(nicksjson)
                        data.append(dest)

            elif action == 'edit':
                report = GoogleReports.objects.get(pk=request.POST['id_goog_repo'])
                nick = Nicks.objects.get(nick=request.POST['nick'])
                report.clients_id_clie = nick.clients_id_clie
                report.date_gore = request.POST['date_gore']
                report.id_clai_gore = request.POST['id_clai_gore']
                report.type_clai_gore = request.POST['type_clai_gore']
                urls = request.POST['urls_gore']
                number = len(urls.splitlines())
                report.cant_urls_gore = number
                report.save()
            elif action == 'delete':
                report = GoogleReports.objects.get(pk=request.POST['id_goog_repo'])
                report.delete()
            else:
                data['error'] = 'An error has occurred'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of Google Reports'
        context['list_url'] = reverse_lazy('manage_reports')
        context['entity'] = 'GoogleReports'
        context['form'] = AddReport()
        context['nicks'] = Nicks.objects.values_list('nick', flat=True)
        return context


class AddTubeReports(CreateView, SuperuserRequired):
    model = TubeReports
    form_class = AddTube
    template_name = 'dmca/worker/add_tube_reports.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        try:
            report = TubeReports()
            nick = Nicks.objects.get(nick=request.POST['nick'])
            report.clients_id_clie = nick.clients_id_clie

            report.date_tube = request.POST['date_tube']

            tube = TubePages.objects.get(name_tube_page=request.POST['tube'])
            report.id_tube_pages_id = tube.id_tube_pages

            report.tube_urls = request.POST['tube_urls']
            number = len(report.tube_urls.splitlines())
            report.cant_urls = number
            report.save()

            messages.success(request, 'Report uploaded successfully')
            return HttpResponseRedirect('tube_reports')
        except Exception as e:
            messages.error(request, e)

        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a new Tube Report'
        context['list_url'] = reverse_lazy('worker')
        context['entity'] = 'TubeReports'
        context['nicks'] = Nicks.objects.values_list('nick', flat=True)
        context['name_tube_page'] = TubePages.objects.values_list('name_tube_page', flat=True)
        return context


class ManageTubeReports(ListView, SuperuserRequired):
    model = TubeReports
    template_name = 'dmca/worker/manage_tubes.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        worker = User.objects.get(id=self.request.user.id)
        client = Clients.objects.filter(worker_id=worker.id)
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in client:
                    for e in TubeReports.objects.filter(clients_id_clie=i.id_clie):
                        encode_reports = jsonpickle.encode(e, unpicklable=False)
                        reports_json = json.loads(encode_reports)
                        dest = {}
                        dest.update(reports_json)
                        for a in Nicks.objects.filter(clients_id_clie=e.clients_id_clie):
                            encodenicks = jsonpickle.encode(a, unpicklable=False)
                            nicksjson = json.loads(encodenicks)
                            dest.update(nicksjson)
                        for b in TubePages.objects.filter(id_tube_pages=e.id_tube_pages_id):
                            encodepage = jsonpickle.encode(b, unpicklable=False)
                            pagejson = json.loads(encodepage)
                            dest.update(pagejson)
                        data.append(dest)

            elif action == 'edit':
                report = TubeReports.objects.get(pk=request.POST['id_tube_repo'])
                nick = Nicks.objects.get(nick=request.POST['nick'])
                page = TubePages.objects.get(name_tube_page=request.POST['tube'])

                report.clients_id_clie = nick.clients_id_clie
                report.date_tube = request.POST['date_tube']
                report.id_tube_pages_id = page.id_tube_pages
                report.tube_urls = request.POST['tube_urls']

                number = len(report.tube_urls.splitlines())
                report.cant_urls = number
                report.save()
            elif action == 'delete':
                report = TubeReports.objects.get(pk=request.POST['id_tube_repo'])
                report.delete()
            else:
                data['error'] = 'An error has occurred'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of Tube Reports'
        context['list_url'] = reverse_lazy('manage_tubes')
        context['entity'] = 'TubeReports'
        context['form'] = AddTube()
        context['nicks'] = Nicks.objects.values_list('nick', flat=True)
        context['name_tube_page'] = TubePages.objects.values_list('name_tube_page', flat=True)
        return context
