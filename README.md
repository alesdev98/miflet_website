# miflet_website

## Comandi

### Login

'''
fly auth login
'''

### Deploy

'''
fly deploy
'''

### Collegare il dominio

'''
fly domains add dominio.com
fly domains add www.dominio.com
'''

### Attivare HTTPS su Fly

Fly.io auto-genera SSL se il DNS punta correttamente alla tua app.

'''
flyctl certs create mifletwebsite.it
flyctl certs create www.mifletwebsite.it
'''

### Check dominio

'''
flyctl certs check
'''

### Configurare DNS (dominio)

Aggiungere le segunti righe nel DNS

'''
mifletwebsite.it.	    900	A	    IPv4 (Fly.io)
mifletwebsite.it.	    900	AAAA	IPv6 (Fly.io)
www.mifletwebsite.it.	900	A	    IPv4 (Fly.io)
www.mifletwebsite.it.	900	AAAA	IPv6 (Fly.io)
'''

### Check dominio

Attendere 5-10 / 2h

'''
flyctl certs check
'''
Dovresti vedere:
HOSTNAME                   STATUS
mifletwebsite.it           Verified
www.mifletwebsite.it       Verified

'''
nslookup www.mifletwebsite.it
'''
Dovrebbe rispondere con 66.241.124.168.

'''
flyctl certs list
'''
Dovresti vedere:
STATUS
Verified

### Final Check
Quando tutto è verificato

Il sito sarà disponibile su:

https://mifletwebsite.it

e

https://www.mifletwebsite.it