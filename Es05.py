#Verificare se la prima lettere di una stringa è in maiuscolo
"""
verifica_maggiore = lambda frase: print("no") if frase.islower() else print("si")

frase = input("Inserisci una frase: ")

verifica_maggiore(frase[0])
"""

#Verificare che una stringa sia palindroma
"""
verifica_palindroma = lambda frase: print("si") if frase == frase[::-1] else print("no")

frase = input("Inserisci una frase: ")

verifica_palindroma(frase)
"""

#Creare da una lista di parole una lista di parole maiuscole e palindrome
"""
parole = ["Ciao", "non", "pino", "Albero","si"]
palindrome_maiuscole = []


for parola in parole:
    if(parole[parola]==parola[::-1]):
        palindrome_maiuscole.append(parole[x])
    

print(parole)
print(palindrome_maiuscole)
"""
#quadrati perfetti minori di 1000

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

for i in range(0, 1000):
   print(is_square)



