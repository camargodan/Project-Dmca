from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from ...forms import PageCreateForm
from ...models import Pages
from ...mixins import SuperuserRequired


class ManagePages(ListView, SuperuserRequired):
    model = Pages
    template_name = 'dmca/admin/manage_pages.html'

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
        context['list_url'] = reverse_lazy('manage_pages')
        context['entity'] = 'Pages'
        context['form'] = PageCreateForm()
        return context
