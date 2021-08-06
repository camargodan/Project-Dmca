from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
from django.contrib.auth import get_user_model
import sys
from ..models import Clients
User = get_user_model()


def unassigned_expired_clients():
    users = User.objects.all()
    today = timezone.now().date()
    for user in users:
        try:
            client = Clients.objects.get(user_id=user.id)
            if client.date_assign <= today and user.assign:
                user.assign = False
                user.save()
                print(f'Client {user.first_name} UNASSIGNED!')
        except Clients.DoesNotExist:
            pass


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every 24 hours
    scheduler.add_job(unassigned_expired_clients, 'interval', hours=24, name='clean_accounts', jobstore='default')
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)


# from datetime import datetime
# from apscheduler.schedulers.background import BackgroundScheduler
# from .jobs import schedule_api
#
#
# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(schedule_api, 'interval', seconds=5)
#     scheduler.start()
