#!/usr/bin/env python
# coding: utf-8

"""
Title: Testat.py
Autor: Remo Herzog
EMail: rherzog@hsr.ch
Datum: 12.04.2019
Organ: HSR Hochschule Rapperswil
Zweck: Testat-Aufgabe Python: QuizRangliste-cls zur Verwaltung von HSRvote.
"""


import csv


class QuizRangliste(object):
    def __init__(self, datei=None):
        """Instanziert die QuizRangliste-Klasse.

        Das txt-File sollte ein CSV-formatiert sein und
        die folgenden Values aufweisen:
        Name, Punkte, Zeit

        Ausgabe:
            -

        Argumente:
            datei -- Pfad zu txt-File

        Elemente:
            type(datei) == str,

        """
        self._datei = datei
        self._rangliste = {}

        try:
            with open(datei, 'r', encoding='utf-8') as f:
                r = csv.reader(f, delimiter=',')
                for row in r:
                    try:
                        self._rangliste[row[0]] = {
                            'Punkte': int(row[1]), 'Zeit': float(row[2])}
                    except (IndexError, ValueError, UnicodeDecodeError):
                        continue

        except FileNotFoundError:
            with open(datei, 'w', encoding='utf-8') as f:
                print('New empty file created.')

        except PermissionError as e:
            print(f'{e}: Not able to read!')

        except UnicodeDecodeError as e:
            print(f'{e}: File might be corrupted!')
            quit()

    def als_dictionary(self):
        """Returnt die Rangliste als Dictionary.

        Gibt die Rangliste unsortiert als Dictionary zurück.
        Da die innere Struktur ein Dict ist, wird diese direkt zurückgegeben.

        Ausgabe:
            {name = {’Punkte’: punkte, ’Zeit’: zeit}, ...}

            {'Noemi': {'Punkte': 7, 'Zeit': 40.0},
            'Max': {'Punkte': 6, 'Zeit': 100.02},
            'Anna': {'Punkte': 5, 'Zeit': 20.55}}

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

        Gibt die Rangliste als Liste von Tuples wieder. Diese sind sortiert
        nach Punkte (absteigend)
        nach Zeit (aufsteigend)
        nach Alphabet.

        Ausgabe:
            [(name, punkte, zeit), ...]

            [('Noemi', 7, 40.0),
            ('Max', 6, 100.02),
            ('Anna', 5, 20.55)]

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

        Gibt die Rangliste als formatierter String zurück. Dieser ist wie
        die Liste sortiert:
        nach Punkte (absteigend)
        nach Zeit (aufsteigend)
        nach Alphabet.
        Der Name ist linksbündig,
        die Punktzahl ist zentriert,
        Die Zeit ist auf eine Dezimalstelle gerundet und rechtsbündig.


        Ausgabe:
            'name  | pkt |  zeit\\n ...'

            Max   | 6 | 100.0
            Anna  | 5 |  20.6
            Laura | 5 |  20.6

        Argumente:
            -

        Elemente:
            type(name) == str,
            type(punkte) == int,
            type(zeit) == float

        """
        name_max = max([len(x) for x in self._rangliste])
        pkt_max = max([len(str(self._rangliste[x]['Punkte']))
                       for x in self._rangliste])
        zeit_max = max([len(str(round(self._rangliste[x]['Zeit'], 1)))
                        for x in self._rangliste])
        output = []
        li = self.als_liste()

        for i in li:
            intern = (i[0].ljust(name_max, ' ') +
                      ' | ' +
                      str(i[1]).center(pkt_max, ' ') +
                      ' | ' +
                      str(round(i[2], 1)).rjust(zeit_max, ' '))
            output.append(intern)

        return '\n'.join(output)

    def resultat_addieren(self, name, pkt, zeit):
        """Fügt ein Resultat der Rangliste hinzu.

        Falls ein der Name bereits vorhanden ist, werden die Resultate addiert.
        Falls der Name nicht existiert, wird ein neuer Eintrag erstellt.
        Der Name darf keine Kommas enthalten

        Argumente:
            name -- Name der Person,
            pkt  -- Erzielte Punkte,
            zeit -- Benötigte Zeit

        Argumente:
            -

        Elemente:
            type(name) == str,
            type(punkte) == int, str
            type(zeit) == float, str

        """
        if ',' in name:
            print('Keine Kommas im Namen erlaubt')
            return

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

        Entfernt einen Eintrag der Rangliste, durch Eingabe des Namens.
        Falls der Name nicht vorhanden ist, passiert nichts.

        Argumente:
            name -- Name der Person

        Argumente:
            -

        Elemente:
            type(name) == str,

        """
        try:
            del self._rangliste[name]
            print(f'{name} wurde entfernt.')
        except KeyError:
            print("Zu diesem Namen existiert kein Eintrag. Does nothing.")

    def speichern(self, als=None):
        """Speichert die Rangliste als csv-Datei.

        Speichert die Rangliste als sortierte CSV-Datei in den angegebenen Pfad
        Wird kein Pfad angegeben wird die alte Datei überschrieben.

        Argumente:
            als (opt) -- Pfad zu neuer Datei,
                ansonsten wird alte Datei überschrieben.

        Elemente:
            type(als) == str,

        """
        if als is None:
            als = self._datei
        try:
            with open(als, 'w', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=',')
                li = self.als_liste()
                for line in li:
                    writer.writerow(line)
        except PermissionError:
            print('PermissionError: Not able to write!')
