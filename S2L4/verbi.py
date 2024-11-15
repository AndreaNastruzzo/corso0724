import http.client

host = input("Inserisci host/IP del sistema target: ")
port = input("Inserisci la porta del sistema target (default:80): ")
path = input("Inserisci il percorso (default:'/'): ")
if(port==""): port = 80
if(path==""): path = '/'
try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS', path)
    response = connection.getresponse()
    if(response.status >= 200 and response.status <= 299 and response.getheader("Allow") != None):
        print("I metodi abilitati sono:", response.getheader("Allow"))
    else:
        print("usa un metodo alternativo per deteminare i verbi\n", response.status, "\n" ,response.getheaders())
    connection.close()
except ConnectionError:
    print("connessione fallita", ConnectionError.strerror)