#Prima e ultima lettera
nomecitta = input("dammi un nome di una citta'");
print(f"citta': {nomecitta}");
print(f"prima lettera: {nomecitta[0]}");
print(f"ultima lettera: {nomecitta[-1]}");



#Stampare tutte le lettere tranne la prima e l'ultima
nomecitta = input("dammi un nome di una citta'");
print(f"citta': {nomecitta}");
for x in nomecitta:
    if x!=nomecitta[0] and x!=nomecitta[-1]:
        print(x);



#Stampare una lettera si e una no
nomecitta = input("dammi un nome di una citta'");
print(f"citta': {nomecitta}");
print(nomecitta[::2])


#Stampare la parola invertita
nomecitta = input("dammi un nome di una citta'");
print(f"citta': {nomecitta}");
print(nomecitta[::-1]);

#Stampare al posto della 3 lettera "?"
nomecitta = input("dammi un nome di una citta'");
print(f"citta': {nomecitta}");
for x in nomecitta:
    if x==nomecitta[2]:
        print("?");
    else:
        print(x);



