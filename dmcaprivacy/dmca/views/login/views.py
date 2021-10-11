from datetime import datetime, timedelta, timezone, date
import jsonpickle
from django.contrib.auth import get_user_model
from django.core import serializers
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from jsonpickle import json
from django.db.models import Sum

from ...mixins import SuperuserRequired
from ...models import Nicks, Clients, Plans, GoogleReports, TubePages, TubeReports, Pages
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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = {}
        try:
            google = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES').aggregate(Sum('cant_urls_gore'))
            content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT').aggregate(Sum('cant_urls_gore'))
            tubes = TubeReports.objects.all().aggregate(Sum('cant_urls'))
            total = google['cant_urls_gore__sum'] + content['cant_urls_gore__sum'] + tubes['cant_urls__sum']

            context = super().get_context_data(**kwargs)
            context['total'] = total
            context['images'] = google
            context['content'] = content
            context['tubes'] = tubes

            week = date.today() - timedelta(days=7)
            last_week = GoogleReports.objects.filter(date_gore__gte=week)
            last_week_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', date_gore__gte=week) \
                .aggregate(Sum('cant_urls_gore'))
            last_week_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', date_gore__gte=week) \
                .aggregate(Sum('cant_urls_gore'))
            context['last_week'] = last_week
            context['last_week_images'] = last_week_images
            context['last_week_content'] = last_week_content

            today = date.today()
            this_month = GoogleReports.objects.filter(date_gore__month=today.month)
            this_month_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', date_gore__month=today.month) \
                .aggregate(Sum('cant_urls_gore'))
            this_month_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', date_gore__month=today.month) \
                .aggregate(Sum('cant_urls_gore'))
            context['this_month'] = this_month
            context['this_month_images'] = this_month_images
            context['this_month_content'] = this_month_content

            last_month = GoogleReports.objects.filter(date_gore__month=today.month - 1)
            last_month_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', date_gore__month=today.month - 1) \
                .aggregate(Sum('cant_urls_gore'))
            last_month_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', date_gore__month=today.month - 1) \
                .aggregate(Sum('cant_urls_gore'))
            context['last_month'] = last_month
            context['last_month_images'] = last_month_images
            context['last_month_content'] = last_month_content

            two_month = GoogleReports.objects.filter(date_gore__month=today.month - 2)
            two_month_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', date_gore__month=today.month - 2) \
                .aggregate(Sum('cant_urls_gore'))
            two_month_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', date_gore__month=today.month - 2) \
                .aggregate(Sum('cant_urls_gore'))
            context['two_month'] = two_month
            context['two_month_images'] = two_month_images
            context['two_month_content'] = two_month_content

            return context
        except Exception as e:
            data['error'] = str(e)
        return data


class Worker(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    template_name = 'dmca/worker.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        worker = self.request.user.id
        data = {}
        try:
            google = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', clients_id_clie__worker_id=worker) \
                .aggregate(Sum('cant_urls_gore'))
            content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', clients_id_clie__worker_id=worker) \
                .aggregate(Sum('cant_urls_gore'))
            tubes = TubeReports.objects.filter(clients_id_clie__worker_id=worker).aggregate(Sum('cant_urls'))
            total = google['cant_urls_gore__sum'] + content['cant_urls_gore__sum'] + tubes['cant_urls__sum']

            context = super().get_context_data(**kwargs)
            context['total'] = total
            context['images'] = google
            context['content'] = content
            context['tubes'] = tubes

            week = date.today() - timedelta(days=7)
            last_week = GoogleReports.objects.filter(clients_id_clie__worker_id=worker, date_gore__gte=week)
            last_week_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', clients_id_clie__worker_id=worker,
                                                            date_gore__gte=week).aggregate(Sum('cant_urls_gore'))
            last_week_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', clients_id_clie__worker_id=worker,
                                                             date_gore__gte=week).aggregate(Sum('cant_urls_gore'))
            context['last_week'] = last_week
            context['last_week_images'] = last_week_images
            context['last_week_content'] = last_week_content

            today = date.today()
            this_month = GoogleReports.objects.filter(clients_id_clie__worker_id=worker, date_gore__month=today.month)
            this_month_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', clients_id_clie__worker_id=worker,
                                                             date_gore__month=today.month).aggregate(Sum('cant_urls_gore'))
            this_month_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', clients_id_clie__worker_id=worker,
                                                              date_gore__month=today.month).aggregate(Sum('cant_urls_gore'))
            context['this_month'] = this_month
            context['this_month_images'] = this_month_images
            context['this_month_content'] = this_month_content

            last_month = GoogleReports.objects.filter(clients_id_clie__worker_id=worker, date_gore__month=today.month - 1)
            last_month_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', clients_id_clie__worker_id=worker,
                                                             date_gore__month=today.month - 1).aggregate(Sum('cant_urls_gore'))
            last_month_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', clients_id_clie__worker_id=worker,
                                                              date_gore__month=today.month - 1).aggregate(Sum('cant_urls_gore'))
            context['last_month'] = last_month
            context['last_month_images'] = last_month_images
            context['last_month_content'] = last_month_content

            two_month = GoogleReports.objects.filter(clients_id_clie__worker_id=worker, date_gore__month=today.month - 2)
            two_month_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', clients_id_clie__worker_id=worker,
                                                            date_gore__month=today.month - 2).aggregate(Sum('cant_urls_gore'))
            two_month_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', clients_id_clie__worker_id=worker,
                                                             date_gore__month=today.month - 2).aggregate(Sum('cant_urls_gore'))
            context['two_month'] = two_month
            context['two_month_images'] = two_month_images
            context['two_month_content'] = two_month_content

            return context
        except Exception as e:
            data['error'] = str(e)
        return data


class Client(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'home'
    template_name = 'dmca/client.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = {}
        try:
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

            for_pages = Pages.objects.filter(nicks__clients_id_clie=client.id_clie)
            for_nicks = Nicks.objects.filter(pages__nicks__clients_id_clie=client.id_clie).distinct()
            context['for_nicks'] = for_nicks
            context['for_pages'] = for_pages

            week = date.today()-timedelta(days=7)
            last_week = GoogleReports.objects.filter(clients_id_clie=client.id_clie, date_gore__gte=week)
            last_week_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', clients_id_clie=client.id_clie, date_gore__gte=week) \
                .aggregate(Sum('cant_urls_gore'))
            last_week_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', clients_id_clie=client.id_clie, date_gore__gte=week) \
                .aggregate(Sum('cant_urls_gore'))
            context['last_week'] = last_week
            context['last_week_images'] = last_week_images
            context['last_week_content'] = last_week_content

            today = date.today()
            this_month = GoogleReports.objects.filter(clients_id_clie=client.id_clie, date_gore__month=today.month)
            this_month_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', clients_id_clie=client.id_clie,
                                                            date_gore__month=today.month) \
                .aggregate(Sum('cant_urls_gore'))
            this_month_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', clients_id_clie=client.id_clie,
                                                             date_gore__month=today.month) \
                .aggregate(Sum('cant_urls_gore'))
            context['this_month'] = this_month
            context['this_month_images'] = this_month_images
            context['this_month_content'] = this_month_content

            last_month = GoogleReports.objects.filter(clients_id_clie=client.id_clie, date_gore__month=today.month-1)
            last_month_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', clients_id_clie=client.id_clie,
                                                             date_gore__month=today.month-1) \
                .aggregate(Sum('cant_urls_gore'))
            last_month_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', clients_id_clie=client.id_clie,
                                                              date_gore__month=today.month-1) \
                .aggregate(Sum('cant_urls_gore'))
            context['last_month'] = last_month
            context['last_month_images'] = last_month_images
            context['last_month_content'] = last_month_content

            two_month = GoogleReports.objects.filter(clients_id_clie=client.id_clie, date_gore__month=today.month-2)
            two_month_images = GoogleReports.objects.filter(type_clai_gore='DMCA-IMAGES', clients_id_clie=client.id_clie,
                                                             date_gore__month=today.month - 2) \
                .aggregate(Sum('cant_urls_gore'))
            two_month_content = GoogleReports.objects.filter(type_clai_gore='DMCA-CONTENT', clients_id_clie=client.id_clie,
                                                              date_gore__month=today.month - 2) \
                .aggregate(Sum('cant_urls_gore'))
            context['two_month'] = two_month
            context['two_month_images'] = two_month_images
            context['two_month_content'] = two_month_content

            return context
        except Exception as e:
            data['error'] = str(e)
        return data


class ReportsList(ListView, SuperuserRequired):
    model = GoogleReports
    template_name = 'dmca/pages/reports_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        client = Clients.objects.get(user=self.request.user.id)
        try:
            action = request.POST['action']
            data = {}
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
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of all Google Reports'
        for_pages = Pages.objects.filter(nicks__clients_id_clie=client.id_clie)
        for_nicks = Nicks.objects.filter(pages__nicks__clients_id_clie=client.id_clie).distinct()
        context['for_nicks'] = for_nicks
        context['for_pages'] = for_pages
        return context


class TubesList(ListView, SuperuserRequired):
    model = TubeReports
    template_name = 'dmca/pages/tubes_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        client = Clients.objects.get(user=self.request.user.id)
        try:
            action = request.POST['action']
            data = {}
            if action == 'searchdata':
                data = []
                for e in TubeReports.objects.filter(clients_id_clie_id=client.id_clie):
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
            else:
                data['error'] = 'An error has occurred'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        client = Clients.objects.get(user=self.request.user.id)
        for_pages = Pages.objects.filter(nicks__clients_id_clie=client.id_clie)
        for_nicks = Nicks.objects.filter(pages__nicks__clients_id_clie=client.id_clie).distinct()
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of all Tube Reports'
        context['for_nicks'] = for_nicks
        context['for_pages'] = for_pages
        return context
