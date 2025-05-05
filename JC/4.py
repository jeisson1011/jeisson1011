edad=int(input("¿cuantos años tienes?"))
licencia=input("¿tienes licencia? (si/no):")
if edad>=18 and licencia=="si":
    print("si puedes conducir")
else:
    print("no puedes conducir")