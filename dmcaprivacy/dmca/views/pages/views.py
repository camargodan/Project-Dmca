from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from ...forms import OfficialPageCreateForm, TubePageCreateForm
from ...models import Pages, Clients, TubePages, GoogleReports, Nicks, TubeReports
from ...mixins import SuperuserRequired
import jsonpickle
from jsonpickle import json


class ManageOfficialPages(ListView, SuperuserRequired):
    model = Pages
    template_name = 'dmca/admin/official_pages.html'

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
                for i in Pages.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                pag = Pages()
                pag.name_page = request.POST['name_page']
                pag.save()
            elif action == 'edit':
                pag = Pages.objects.get(pk=request.POST['id_page'])
                pag.name_page = request.POST['name_page']
                pag.save()
            elif action == 'delete':
                pag = Pages.objects.get(pk=request.POST['id_page'])
                pag.delete()
            else:
                data['error'] = 'An error has occurred'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of pages, search, add, edit or remove.'
        context['list_url'] = reverse_lazy('official_pages')
        context['entity'] = 'Pages'
        context['form'] = OfficialPageCreateForm()
        return context


class ManageTubePages(ListView, SuperuserRequired):
    model = TubePages
    template_name = 'dmca/admin/tube_pages.html'

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
                for i in TubePages.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                tub = TubePages()
                tub.name_tube_page = request.POST['name_tube_page']
                tub.contact_tube = request.POST['contact_tube']
                tub.save()
            elif action == 'edit':
                tub = TubePages.objects.get(pk=request.POST['id_tube_pages'])
                tub.name_tube_page = request.POST['name_tube_page']
                tub.contact_tube = request.POST['contact_tube']
                tub.save()
            elif action == 'delete':
                tub = TubePages.objects.get(pk=request.POST['id_tube_pages'])
                tub.delete()
            else:
                data['error'] = 'An error has occurred'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of tubes, search, add, edit or remove.'
        context['list_url'] = reverse_lazy('tube_pages')
        context['entity'] = 'TubePages'
        context['form'] = TubePageCreateForm()
        return context


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
