
#%%
import csv


#%%
class QuizRangliste(object):
    def __init__(self, datei=None):
        """

        """
        self._datei = datei
        self._rangliste = {}

        try:
            with open(datei, 'r', encoding='utf-8') as f:
                r = csv.reader(f, delimiter=',')
                for row in r:
                    try:
                        self._rangliste[row[0]] = {'Punkte': int(row[1]), 'Zeit': float(row[2])}
                    except IndexError:
                        continue

        except FileNotFoundError:
            with open(datei, 'w', encoding='utf-8') as f:
                print('New empty file created.')

    def als_dictionary(self):
        """Returnt die Rangliste als Dictionary.
        
        Ausgabe:
            Key = name, Value = {’Punkte’: punkte, ’Zeit’: zeit}
        
        Argumente:
            -
        
        Elemente:
            type(name) == str,
            type(punkte) == int,
            type(zeit) == float
            
        """
        return self._rangliste
    
    def als_liste(self):
        """Return die Rangliste als Liste.
        
        Ausgabe:
            [(name, punkte, zeit), ...]
        
        Argumente:
            -
        
        Elemente:
            type(name) == str,
            type(punkte) == int,
            type(zeit) == float
        
        """
        output = []
        for k, v in self._rangliste.items():
            output.append((k, v['Punkte'], v['Zeit']))
        return sorted(output, key=lambda x: (-x[1], x[2], x[0]))
                
            

    def als_string(self):
        """Return die Rangliste als String.
        
        Ausgabe:
            'name  | pkt |  zeit'
        
            Max   | 6 | 100.0
            Anna  | 5 |  20.6
            Laura | 5 |  20.6
            Fritz | 5 |  39.3
            Hans  | 2 |  45.2
        
        Argumente:
            -
        
        Elemente:
            type(name) == str,
            type(punkte) == int,
            type(zeit) == float
        
        
        """
        pass
    
    def resultat_addieren(self, name, pkt, zeit):
        """Fügt ein Resultat der Rangliste hinzu.
        
        Falls ein der Name bereits vorhanden ist, werden die Resultate addiert.
        Falls der Name nicht existiert, wird ein neuer Eintrag erstellt.
        Der Name darf keine Kommas enthalten
        
        Argumente:
            name -- Name der Person, type = string
            pkt  -- Erzielte Punkte, type = int, str
            zeit -- Benötigte Zeit,  type = float, str
            
        """
        try:
            name = str(name)
            pkt = int(pkt)
            zeit = float(zeit)
        except ValueError:
            print('ValueError: Please enter correct types.')
            return False
        
        if name in self._rangliste:
            self._rangliste[name]['Punkte'] += int(pkt)
            self._rangliste[name]['Zeit'] += float(zeit)
            print(f'{name} wurde um Pkt: {pkt} und Zeit: {zeit} ergänzt.')
        else:
            self._rangliste[name] = {'Punkte': pkt, 'Zeit': zeit}
            print(f'Rangliste wurde um {name} ergänzt.')
        
        return True

    
    def name_entfernen(self, name):
        """Entfernt einen Eintrag.
        
        Argumente:
            name -- Name der Person, type = string
        
        """
        try:
            del self._rangliste[name]
            print(f'{name} wurde entfernt.')
        except KeyError:
            print("Zu diesem Namen existiert kein Eintrag. Does nothing.")


    def speichern(self, als=None):
        """Speichert die Rangliste als csv-Datei.
        
        Argumente:
            path (opt) -- Pfad zu neuer Datei, ansonsten wird alte Datei überschrieben. type = string
         
        """
        if als == None:
            als = self._datei
        with open(als, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',')
            li = self.als_liste()
            for line in li:
                writer.writerow(line)


#%%
qr = QuizRangliste(datei='rangliste.txt')


#%%
qr.resultat_addieren('Abdul', 8, 32.0)


#%%
qr.name_entfernen('Peter')


#%%
qr.speichern(path='resultat.txt')


#%%
qr._rangliste


#%%
qr.als_liste()


#%%
dir(qr)


