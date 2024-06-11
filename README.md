# [M] 8c.1: Zeichenrechteck, Zahlenraten und Palindromtest


Löse die Beispiele jeweils in einer eigenen Python-Datei. Die Abgabe erfolgt durch Hochladen des Source Codes als zip.
Zeichenrechteck

Schreib ein Programm, das eine Breite, eine Höhe und ein Zeichen einliest (stelle sicher, dass du nur das 1. Zeichen verwendest, wenn mehrere Zeichen eingegeben werden). Bilde dann ein Rechteck aus den eingegebenen Daten. So soll z.B. bei einer Eingabe von 9, 4 und SEW folgende Ausgabe erscheinen.

```
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
```

Zahlenraten

Schreibe ein Python-Programm, mit dem das Spiel Zahlenraten implementiert werden kann. Recherchiere dazu, wie man Zufallszahlen in einem Zahlen-Bereich in Python machen kann und verwende deine Erkenntnisse, um eine Geheimzahl im Bereich 1-10 zu erzeugen. Wenn die Zahl nicht stimmt, dann soll ausgegeben werden, ob die Zahl zu groß oder zu klein ist und noch eine Eingabe abgefragt werden. Dies soll solange wiederholt werden, bis die richtige Zahl erraten wird. Dann soll eine Erfolgsmeldung und die Anzahl der Versuche ausgegeben werden. Ein Beispielablauf könnte so aussehen:

1. Versuch: Was ist die Geheimzahl? 5
Die eingegebene Zahl ist zu klein
2. Versuch: Was ist die Geheimzahl? 8
Die eingegebene Zahl ist zu groß
3. Versuch: Was ist die Geheimzahl? 7
Gratulation! Das Geheimnis 7 wurde nach 3 Versuchen erraten.

Palindromtest

Schreibe die folgenden zwei Funktionen in Python:

- `ist_palindrom`: Diese Funktion soll einen Text als Parameter übernehmen und überprüfen, ob dieser Text ein Wort-Palindrom ist (von vorne und hinten gleich gelesen, z.B. Otto). In diesem Fall soll True zurück gegeben werden, im anderen Fall false
- `ist_satzpalindrom`: Diese Funktion soll auch Palindrom-Sätze erkennen (z.B. Regine, wette weniger!). Dazu sollen zunächst die Satz- und Leerzeichen aus dem String gefiltert werden. Dieser gefilterte String soll dann mit Hilfe von ist_palindrom getestet werden und das Ergebnis zurückgegeben werden.

Teste deine Funktionen. Achte darauf, dass die Tests nicht ausgeführt werden wenn deine Datei als Modul importiert wird.
