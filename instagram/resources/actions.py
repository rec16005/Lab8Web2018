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

def menu_log():
  print("MENU")
  print("1. Crear post")
  print("2. Likear post")
  print("3. Borrar post")
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

def login(username, email):
  try:
    current_user = Users.objects.get(user_name=username, email=email)
    print("Bienvenido " + current_user.user_name)
  except Users.DoesNotExist:
    print("No hay usuarios con ese ID")
  print("----------------------------------")
  return current_user

def create_post():
  title = input("Ingrese el título del post: ")
  post_body = input("Ingrese el contenido del post: ")
  new_post = Posts(title = title, post_body = post_body)
  new_post.save()
  print("Cantidad despues: ", Posts.objects.all().count())
  print("----------------------------------")

def show_posts():
  print("Posts: ")
  for post in Posts.objects.all():
    print("Numero={}: {} | {} ({}) -- {}".format(post.pk, post.title, post.post_body, post.number_likes.count(), post.date))
  print("----------------------------------")

def like_post(current_user, liked_id):
  try:
    liked_post = Posts.objects.get(id=liked_id)
    new_like = Likes(user = current_user, post = liked_post)
    new_like.save()
    print("Post likeado: " + liked_post.title)
  except Posts.DoesNotExist:
    print("No existe el post")
  print("----------------------------------")

def delete_post(deleted_id):
  try:
    deleted_post = Posts.objects.get(id=deleted_id)
    deleted_post.delete()
    print("Cantidad despues: ", Posts.objects.all().count())
  except Posts.DoesNotExist:
    print("No existe el post")
  print("----------------------------------")