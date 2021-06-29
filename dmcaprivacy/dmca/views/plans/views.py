from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from ...forms import PlanCreateForm
from ...models import Plans
from ...mixins import SuperuserRequired


class ManagePlans(ListView, SuperuserRequired):
    model = Plans
    template_name = 'dmca/admin/manage_plans.html'

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
                for i in Plans.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                pla = Plans()
                pla.plan = request.POST['plan']
                pla.save()
            elif action == 'edit':
                pla = Plans.objects.get(pk=request.POST['id_plan'])
                pla.plan = request.POST['plan']
                pla.save()
            elif action == 'delete':
                pla = Plans.objects.get(pk=request.POST['id_plan'])
                pla.delete()
            else:
                data['error'] = 'An error has occurred'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of plans, search, add, edit or remove.'
        context['list_url'] = reverse_lazy('manage_plans')
        context['entity'] = 'Plans'
        context['form'] = PlanCreateForm()
        return context
