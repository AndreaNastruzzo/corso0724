risposta=input("Potrei aiutarti a trovare un nome per la tua nuova band?")
if risposta.lower()[0]=="s":
    x=input("Nome animale domestico: ")
    y=input("Città di provenienza: ")
    def somma(animale,città):
        
        return f"Il nome della tua band potrebbe essere: {animale+città}"
    print(somma(x,y))
