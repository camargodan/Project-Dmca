from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from ...forms import NicksCreateForm
from ...models import Nicks, Clients, Pages
from ...mixins import SuperuserRequired
# from django.contrib.auth import get_user_model
#
# User = get_user_model()


class ManageNicks(ListView, SuperuserRequired):
    model = Nicks
    template_name = 'dmca/client/manage_nicks.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
#
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            client = Clients.objects.get(user=self.request.user.id)
            if action == 'searchdata':
                data = []
                # nicks = Nicks.objects.filter(pages__name_page=)
                for i in Nicks.pages.through.objects.all():
                    print(i)
                    data.append(i.toJSON())
                    # for e in Pages.objects.filter(id_page=nicks.pages_id_pages):
                    #     data.append(e.toJSON())
            # elif action == 'add':
            #     nick = Nicks()
            #     nick.name_page = request.POST['name_page']
            #     nick.save()
            # elif action == 'edit':
            #     pag = Pages.objects.get(pk=request.POST['id_page'])
            #     pag.name_page = request.POST['name_page']
            #     pag.save()
            # elif action == 'delete':
            #     pag = Pages.objects.get(pk=request.POST['id_page'])
            #     pag.delete()
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
#
#
# class ManageTubePages(ListView, SuperuserRequired):
#     model = TubePages
#     template_name = 'dmca/admin/tube_pages.html'
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     @method_decorator(csrf_exempt)
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'searchdata':
#                 data = []
#                 for i in TubePages.objects.all():
#                     data.append(i.toJSON())
#             elif action == 'add':
#                 tub = TubePages()
#                 tub.name_tube_page = request.POST['name_tube_page']
#                 tub.contact_tube = request.POST['contact_tube']
#                 tub.save()
#             elif action == 'edit':
#                 tub = TubePages.objects.get(pk=request.POST['id_tube_pages'])
#                 tub.name_tube_page = request.POST['name_tube_page']
#                 tub.contact_tube = request.POST['contact_tube']
#                 tub.save()
#             elif action == 'delete':
#                 tub = TubePages.objects.get(pk=request.POST['id_tube_pages'])
#                 tub.delete()
#             else:
#                 data['error'] = 'An error has occurred'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'List of tubes, search, add, edit or remove.'
#         context['list_url'] = reverse_lazy('tube_pages')
#         context['entity'] = 'TubePages'
#         context['form'] = TubePageCreateForm()
#         return context
