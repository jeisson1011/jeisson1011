nombre1=input("nombre del primer hermano:")
edad1=int(input("edad de"+nombre1+":"))
nombre2=int("nombre del sefundo hermano:")
edad2=int(input("edad de"+nombre2+":"))
mayor=nombre1 if edad1>edad2 else nombre2
print("el mayor es:",mayor)