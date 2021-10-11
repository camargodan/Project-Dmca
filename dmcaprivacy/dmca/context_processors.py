from .models import GoogleReports, TubeReports, TubePages, Clients
import jsonpickle
from jsonpickle import json


def custom_processor(request):
    if not request.user.id:
        data = 'none'
        last_five = 'none'
    elif request.user.is_worker or request.user.is_superuser:
        data = 'none'
        last_five = 'none'
    else:
        client = Clients.objects.get(user=request.user.id)
        last_five = GoogleReports.objects.filter(clients_id_clie=client.id_clie).order_by('-date_gore')[:5]
        data = {}
        data = []
        for e in TubeReports.objects.filter(clients_id_clie=client.id_clie):
            encode_reports = jsonpickle.encode(e, unpicklable=False)
            reports_json = json.loads(encode_reports)
            dest = {}
            dest.update(reports_json)
            for b in TubePages.objects.filter(id_tube_pages=e.id_tube_pages_id):
                encodepage = jsonpickle.encode(b, unpicklable=False)
                pagejson = json.loads(encodepage)
                dest.update(pagejson)
            data.append(dest)

    return {"last_five_google": last_five,
            "last_tubes": data,
            }
