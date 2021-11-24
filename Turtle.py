import turtle #si importa la libreria turtle 
fiore = turtle.Turtle() #assegnamo a fiore il comando di turtle 
for i in range(10): #per il nostro fiore ci serve disegnare per 12 volte la stessa forma
    for x in range(2): #ciclo per chiudere una forma in maniera regolare
        fiore.forward(100) #traccia una linea dritta lunga 100
        fiore.right(60) #la freccia si gira di 60 verso destra
        fiore.forward(100) #traccia una linea dritta lunga 100
        fiore.right(120) #la freccia si gira di 120 verso destra
    fiore.right(36) #la freccia si gira di 36 verso destra
