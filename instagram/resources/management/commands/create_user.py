from django.core.management.base import BaseCommand

from resources.models import Users

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        name = input("Ingrese el nombre: ")
        last_name = input("Ingrese el apellido: ")
        email = input("Ingrese el email: ")
        user_name = input("Ingrese el user name: ")
        new_user = Users(name = name, last_name = last_name, email = email, user_name = user_name)
        new_user.save()
        print("Cantidad despues: ", Users.objects.all().count())