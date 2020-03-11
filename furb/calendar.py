dia_semana = int(input("Em qual dia da semana começa o mês? (1-dom, 2-seg, 3-ter, ...) "))
dias_mes   = int(input("Quantos dias tem o mês? "))

contador = 1
lista=[]
list_sem1 = []
list_sem2 = []
list_sem3 = []
list_sem4 = []
list_sem5 = []

while contador < dia_semana: #adiciona as caixas vazias do mês, se tiver
    list_sem1.append("|    ")
    contador+=1

for i in range(1, dias_mes+1): #adiciona os números do mês na lista, junto com os traços
    if i < 10:
        lista.append("|  "+str(i)+" ")
    else:
        lista.append("| "+str(i)+" ")

#a seguir, contadores de indices    
v=7-len(list_sem1)
z=v+7
x=z+7
w=x+7

list_sem1 += lista[0:7-len(list_sem1)]
list_sem2 = lista[v:z]
list_sem3 = lista[z:x]
list_sem4 = lista[x:w]
list_sem5 = lista[w:dias_mes+1]


if len(list_sem5) > 0:
    #list_sem5+="|"
    if len(list_sem5) < 7:
        while len(list_sem5)<8:
            list_sem5.append("|    ")


semana1=""
semana2=""
semana3=""
semana4=""
semana5=""

print("------------------------------------")  
print("| D  | S  | T  | Q  | Q  | S  | S  |")
print("------------------------------------")  

for i in list_sem1:
    semana1+=i

for i in list_sem2:
    semana2+=i

for i in list_sem3:
    semana3+=i

for i in list_sem4:
    semana4+=i

for i in list_sem5:
    semana5+=i

if len(semana2) > 0:
    semana2+="|"

if len(semana3) > 0:
    semana3+="|"

if len(semana4) > 0:
    semana4+="|"

print(semana1+"|")
print(semana2)
print(semana3)
print(semana4)
print(semana5)
print("------------------------------------")  
