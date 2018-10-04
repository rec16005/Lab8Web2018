from resources.models import Users, Posts, Likes

def menu():
  print("MENU")
  print("1. Crear usuario")
  print("2. Mostrar usuarios")
  print("3. Acceder")
  print("4. Salir")
  selection = input("Ingrese su selección: ")
  print("----------------------------------")
  return selection

def create_user():
  name = input("Ingrese el nombre: ")
  last_name = input("Ingrese el apellido: ")
  email = input("Ingrese el email: ")
  user_name = input("Ingrese el user name: ")
  new_user = Users(name = name, last_name = last_name, email = email, user_name = user_name)
  new_user.save()
  print("Cantidad despues: ", Users.objects.all().count())
  print("----------------------------------")

def show_users():
  print("Usuarios:")
  for user in Users.objects.all():
    print("pk={}: {} {} - {} - {}".format(user.pk, user.name, user.last_name, user.user_name, user.email))
  print("----------------------------------")

def login():
  user = input("Ingrese username: ")
  this_email = input("Ingrese email: ")
  current_id = -1
  for user in Users.objects.all():
    if user.user_name == user and user.email == this_email:
      current_id = user.pk
      print("Hola {}").format(user.name)
      break
  return current_id