from django.core.management.base import BaseCommand
import resources.actions as action

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
      selec = "-1"
      current_user_id = "-1"
      while selec != "0":
        selec = action.menu()

        if selec == "1":
          action.create_user()
        elif selec == "2":
          action.show_users()
        elif selec == "3":
          current_user_id = action.login()
          if current_user_id == "-1":
            print("Usuario o email incorrecto")
          print("----------------------------------")
        elif selec == "4":
          print("Adios!")
          print("----------------------------------")
          selec = "0"
        else:
          print("Opcion incorrecta trate de nuevo")
          print("----------------------------------")