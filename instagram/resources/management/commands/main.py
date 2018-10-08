from django.core.management.base import BaseCommand
import resources.actions as action

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
      selec = "-1"
      while selec != "0":
        selec = action.menu()

        if selec == "1":
          action.create_user()

        elif selec == "2":
          action.show_users()

        elif selec == "3":
          given_username = input("Ingrese el username: ")
          given_email = input("Ingrese el email: ")
          current_user = action.login(given_username, given_email)
          selec2 = "-1"

          while selec2 != "0":
            selec2 = action.menu_log()
            if selec2 == "1":
              action.create_post()
            elif selec2 == "2":
              action.show_posts()
              liked_id = input("Ingrese el numero del post: ")
              action.like_post(current_user,liked_id)
            elif selec2 == "3":
              action.show_posts()
              deleted_id = input("Ingrese el numero del post: ")
              action.delete_post(deleted_id)
            elif selec2 == "4":
              selec2 = "0"
            else:
              print("Opcion incorrecta trate de nuevo")
              print("----------------------------------")

          print("----------------------------------")

        elif selec == "4":
          print("Adios!")
          print("----------------------------------")
          selec = "0"
       
        else:
          print("Opcion incorrecta trate de nuevo")
          print("----------------------------------")