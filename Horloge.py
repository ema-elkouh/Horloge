from datetime import datetime, timedelta
import time

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(1)

horloge = int(input ( " Entrez le nombre de secondes voulue : "))
# question pour les nombres de secondes 

secondes = horloge % (24 * 3600)
#nombres de secondes par jour 
heures = horloge // 3600
#nombre d'heures en secondes
secondes %= 3600
minutes = horloge // 60
#nombre de seconde en 1 min
secondes %= 60 

print("%d:%02d:%02d" % (heures, minutes, secondes))
#affiche l'heure final

#mon deuxième code qui marche avec le nombre de secondes donnée

alarme = int(input ( " M'écrire un message à "))

message = alarme % (24 * 3600)
heures = alarme // 3600
secondes %= 3600

minutes = alarme // 60

secondes %= 60

print("%d:%02d:%02d" % (heures, minutes, secondes))

import time

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(1)
