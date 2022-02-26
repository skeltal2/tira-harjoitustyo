# Viikkoraportti 6

Työmäärä 8 h

Tällä viikolla tarkoituksena oli nostaa testikattavuutta, mutta kun lisäsin testejä heuristiikkaan, huomasin että smoothness() eli tasaisuus ei toiminut oikein. Sen pitäisi palauttaa 0, jos pelilauta on täydellisesti tasainen, mutta jos laudalla on tyhjiä laattoja, se palautti vääriä arvoja. Metodin piti ohittaa tyhjät laatat kokonaan, mutta se toimi vain yhteen suuntaan. Se ohitti normaalien laattojen tyhjät naapurit, mutta ei tyhjien laattojen normaaleja naapureita. Ongelman korjaamiseen meni paljon aikaa, koska painoja ja syvyyttä piti muuttaa metodin korjaamisen lisäksi. Kun korjasin tämän ongelman, algoritmi toimi paremmin. Se saavutti 2048-laatan yhtä hyvin kuin viallinen algoritmi, mutta onnistui pääsemään 4096-laattaan useamman kerran.

![kuva](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikko6_suoritus1.png)
