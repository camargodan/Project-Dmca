from dmca.models import Nicks, GoogleReports, TubeReports, TubePages, Clients
import jsonpickle
from django.contrib.auth import get_user_model
from jsonpickle import json
User = get_user_model()


def custom_processor(request):
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
