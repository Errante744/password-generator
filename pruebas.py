def create_password():
  print("crea una contraseña con minimo 8 caracters, Mayúsculas, Minúsculas, y Numeros")

  while True:
    password = input("Crea una contraseña: ").strip()

    tinany_minimo = len(password) >= 8
    tinany_Mayus = any(z.isupper() for z in password)
    tinany_Minus = any(z.islower() for z in password) 
    tiany_Num = any(z.isdigit() for z in password)

    if tinany_minimo and tinany_Mayus and tinany_Minus and tiany_Num:
      print("La contraseña es válida.")
      return password
    else:
      print("La contraseña debe de tener minimo 8 caracteres, Mayúsculas, Minúsculas y Números. intentalo de nuevo.")


def confirm_password(password):

  print("Confirma la contraseña, para verificar que coincidan")
  intentos = 4

  while intentos > 0:
      confirmation = input("confirma la contraseña por favor: ").strip()
    
      if confirmation == password:

          print("La confirmación fue exitosa")
          return True
  
      else:
          intentos -= 1
          print(f"La contraseña es incorrecta. Te quedan {intentos} intentos")
      
  print("Has agotado tus intentos disponibles")
  return False