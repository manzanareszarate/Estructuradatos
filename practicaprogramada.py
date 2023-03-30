Materia = []
Materia1 =input ("Digite la primer materia que esta cursando: ")
Materia.append(Materia1)
Materia2 =input ("Digite la segunda materia que esta cursando: ")
Materia.append(Materia2)
Materia3 =input ("Digite la tercer materia que esta cursando: ")
Materia.append(Materia3)
Materia4 =input ("Digite la cuarta materia que esta cursando: ")
Materia.append(Materia4)
Materia5 =input ("Digite la Quinta materia que esta cursando: ")
Materia.append(Materia5)
print("---------------------------------------------------------------")

for indice in Materia:
    print("Yo Estudio : " + indice)

print("---------------------------------------------------------------")

Nota=[]
nota1=input("ingrese su nota de la materia " + Materia[0]+ " ")
Nota.append(nota1)
nota2=input("ingrese su nota de la materia " + Materia[1]+ " ")
Nota.append(nota2)
nota3=input("ingrese su nota de la materia " + Materia[2] + " ")
Nota.append(nota3)
nota4=input("ingrese su nota de la materia " + Materia[3]+ " ")
Nota.append(nota4)
nota5=input("ingrese su nota de la materia " + Materia[4] + " ")
Nota.append(nota5)

print("--------------------------------------------------")
print("En materia " +Materia[0] + " has sacado : " + nota1)
print("En materia " +Materia[1] + " has sacado : " + nota2)
print("En materia " +Materia[2] + " has sacado : " + nota3)
print("En materia " +Materia[3] + " has sacado : " + nota4)
print("En materia " +Materia[4] + " has sacado : " + nota5)
print("--------------------------------------------------")

if int (nota1) < 70:
        print("Has Reprobado el curso" +" " + Materia[0]+ " " + nota1 )
else:Nota.remove(nota1)
if int(nota2) < 70:
        print("Has Reprobado el curso" +" " + Materia[1]+ " " + nota2 )
else:Nota.remove(nota2)

if int(nota3) < 70:
        print("Has Reprobado el curso" +" " + Materia[2]+ " " + nota3 )
else:Nota.remove(nota3)
if int(nota4) < 70:
        print("Has Reprobado el curso" +" " + Materia[3]+ " " + nota4 )
else:Nota.remove(nota4)

if int (nota5) < 70:
        print("Has Reprobado el curso" +" " + Materia[4]+ " " + nota5 )
else:Nota.remove(nota5)

print("--------------------------------------------------")
print(Nota)