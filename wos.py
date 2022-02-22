from operator import inv


invitados =[]
invitados.append(input("nombre del invitado"))
print(invitados)

otro=input("desea agrregar otro s/n: ")

while otro == "s":
    invitados.append(input("nombre del invitado"))
    print(invitados)
    otro=input("desea agregar otro s/n:")
    
print("usted tiene",len(invitados), "invitados")
invitados.sort()
print (invitados)


nombre= input("digite su nmobre")
lista=[]

for i in nombre: 
    lista.append(i)
    

print("su nombre tiene", len(lista), "caracteres")
print(lista)