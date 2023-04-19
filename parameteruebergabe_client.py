
"""

# Parameterübergabe mit HTTP

Bearbeiten Sie die folgenden Aufgaben und laden Sie Ihre Ergebnis anschließend
auf Moodle hoch:

1. Beschreiben Sie, wie bei GET- und POST-Anfragen Parameter an den Server
   übergeben werden.
2. Stellen Sie die Vorteile und Nachteile der beiden Verfahren gegenüber.
3. Recherchieren Sie, wie sich mit der Python-Bibliothek flask GET- und
   POST-Parameter empfangen und verarbeiten lassen.
4. Erstellen Sie ein Python-Programm, das einen HTTP-Server mit zwei Endpunkten
   (/get und /post) implementiert. Bei beiden Ressourcen soll es möglich sein,
   in der Anfrage Parameter als GET- bzw. als POST-Parameter zu übergeben.
   Beide sollen die übergebenen Parameter im JSON-Format zurück zum anfragenden
   Browser schicken.
5. Testen Sie Ihren HTTP-Server mit der Browser-Erweiterung RESTED (oder einem
   anderen Programm, wie Postman) mit Beispiel-Anfragen, die GET- bzw.
   POST-Parameter enthalten.
6. Führen Sie das unten stehende Python-Programm aus und prüfen Sie damit Ihren
   HTTP-Server auf korrekte Funktion.

Laden Sie anschließend Ihre Antworten auf die ersten beiden Fragen und das
erstellte Python-Programm mit dem HTTP-Server hoch.

"""

import urllib.parse

import requests


base_url = 'http://127.0.0.1:5000'
parametersatz = {'wert1': '42', 'wert2': '47', 'wert3': '1337'}


# GET-Anfrage an den korrekten Endpunkt
r = requests.get(urllib.parse.urljoin(base_url, '/get'),  params=parametersatz)
assert r.status_code == 200, 'GET-Anfrage wurde mit falschem Status-Code beantwortet.'
assert r.json() == parametersatz, 'GET-Anfrage liefert fehlerhafte Daten zurück.'

# POST-Anfrage an den falschen Endpunkt
r = requests.post(urllib.parse.urljoin(base_url, '/get'), data=parametersatz)
assert r.status_code == 405, 'POST-Anfrage an den GET-Endpunkt wurde mit falschem Status-Code beantwortet.'

# GET-Anfrage an den falschen Endpunkt
r = requests.get(urllib.parse.urljoin(base_url, '/post'),  params=parametersatz)
assert r.status_code == 405, 'GET-Anfrage an den POST-Endpunkt wurde mit falschem Status-Code beantwortet.'

# POST-Anfrage an den korrekten Endpunkt
r = requests.post(urllib.parse.urljoin(base_url, '/post'), data=parametersatz)
assert r.status_code == 200, 'POST-Anfrage wurde mit falschem Status-Code beantwortet.'
assert r.json() == parametersatz, 'POST-Anfrage liefert fehlerhafte Daten zurück.'

print('Wenn diese Nachricht ausgegeben wird, funktioniert ihr Server gemäß Vorgaben. :-)')
