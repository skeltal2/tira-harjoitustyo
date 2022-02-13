# Viikkoraportti 4

Työmäärä 17 h

Tällä viikolla lähes kaikki aika meni algoritmin ja heuristiikan kirjoittamiseen. Ensimmäinen versio, jonka sain toimimaan kunnolla, saavutti 2048-laatan noin 80 % ajasta, mutta oli todella hidas. Yksi peli saattoi kestää (huonommalla tietokoneella) jopa 5 minuuttia. En keksinyt, miten mahdollisia vapaita laattoja pystyisi karsimaan enemmän siten, että tarkkuus ei putoaisi paljon. Lopulta päädyin käyttämään yksinkertaisempaa versiota, joka saavuttaa 2048-laatan noin 30 % ajasta, mutta suoritusaika on noin yksi minuutti.

Hitaan algoritmin suoritus:

![kuva](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikko4_suoritus.png)

Kuitenkin myöhemmin keksin tavan nopeuttaa suoritusaikaa paljon. Muutin maksimisyvyyden neljästä kolmeen, ja muutin minimaxin siten, että se lopettaa haun, jos vapaita laattoja on liikaa. Tämä vähensi suoritusajan noin 25 sekunttiin, mutta 2048-laatta saavutettiin vain noin 40% ajasta. Kuitenkin heuristiikan painojen arvojen muuttamisen jälkeen sain nostettua 2048-saavutuksen 80 %.

![kuva](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikko4_suoritus_2.png)