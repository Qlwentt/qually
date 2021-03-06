import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="qlwentt").exists():
            User.objects.create_superuser(os.environ["ADMIN_USER_NAME"], os.environ["ADMIN_EMAIL"], os.environ["ADMIN_PASSWORD"])
