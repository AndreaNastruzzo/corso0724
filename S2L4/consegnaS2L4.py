menu=input("quale perimetro preferisci calcolare tra: quadrato, cerchio, o rettangolo? ")
if menu == "quadrato": 
    print("hai scelto di calcolare il perimetro del quadrato")
    lato=float (input("inserire la lunghezza dei lati: "))
    print (f"il perimetro del quadrato è: {lato*4}")
elif menu == "rettangolo":
    print("hai scelto di calcolare il perimetro del rettangolo")            
    base=float (input("inserire lunghezza base: "))
    altezza=float (input("inserire l'altezza del rettangolo: "))
    print (f"il perimetro del rettangolo è: {(base+altezza)*2}")
elif menu == "cerchio":
    print("hai scelto di calcolare la circonferenza del cerchio")
    raggio=float (input("inserire la lunghezza del raggio: "))
    print (f"la circonferenza del cerchio è: {(2*3.14)*raggio}")
print ("Grazie e buon proseguimento!!")