from Testat import QuizRangliste

qr = QuizRangliste(datei='rangliste.txt')

print(qr.als_dictionary())
print(qr.als_liste())
print(qr.als_string())

qr.resultat_addieren('Helen', 1, 100)
qr.speichern(als='resultat.txt')