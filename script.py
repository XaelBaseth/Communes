import urllib.request
import json

def codePostal():
	codePostal = input("Entrez le code postal recherché : ")

	if len(codePostal) < 5:
		print("Votre code postal ne peut pas avoir moins de 5 chiffres.")
	elif len(codePostal) > 5:
		print("Votre code postal ne peut pas avoir plus de 5 chiffres.")
	else:
		requete = urllib.request.Request('http://api.zippopotam.us/FR/' + codePostal) #requete de l'api
		reponse = urllib.request.urlopen(requete)#réponse de l'api
		donneesBrut = reponse.read().decode('utf-8')#decryptement de la réponse
		donneesJSON = json.loads(donneesBrut)#chargement de la réponse
		listeCommunes = donneesJSON["places"]#les données places sont les seuls qui nous interessent ici.
		print("Voici la liste des communes ayant pour code postal " + codePostal + ' : ')
		for commune in listeCommunes:
			print(" - " + commune["place name"] + " situé en : " + commune["state"])


codePostal()
