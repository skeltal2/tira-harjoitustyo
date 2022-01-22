# Määrittelydokumentti

Projektin tarkoituksena on luoda tavallinen 2048-peli ja algoritmi, joka pystyy luotettavasti voittamaan sen.

- Projektin kieli: Suomi
- Ohjelmointikieli: python
- Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT)

2048-peli koostuu 4 x 4 pelilaudasta ja laatoista, joilla on jokin arvo. Pelaaja voi tehdä siirron, jolloin hän liikuttaa kaikkia laattoja joko vasemmalle, oikealle, ylös tai alas. Jos mikään laatta ei liiku, pelaaja ei voi tehdä siirtoa siihen suuntaan. Jokaisella siirrolla pelilaudalle ilmestyy uusi 2- tai 4-laatta. Jos x-laatta törmää toiseen x-laattaan, ne yhdistyvät 2x-laataksi (esim. 2-laatta + 2-laatta = 4-laatta). Pelin tavoitteena on luoda 2048-laatta. Jos pelaaja ei voi tehdä mitään siirtoa, peli on hävitty. Alkuperäistä peliä voi kokeilla [tästä](https://play2048.co/).

Ratkaisualgoritmi perustuu [tähän](https://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048/22389702#22389702) ideaan. Se toteutetaan käyttäen minimax-algoritmia ja alfa-beeta karsintaa. Jotta tämä toimisi, algoritmin pitää voida jotenkin voida arvioida, kuinka hyviä eri pelilaudat ovat. Minimax-algoritmi tarvitsee myös "toisen pelaajan", joka tässä tapauksessa voisi olla toinen algoritmi, joka etsii huonoimman mahdollisen paikan sijoittaa uusi laatta. Todellisuudessa uudet laatat sijoitetaan satunnaisesti, mutta tällä tavalla algoritmi voi varautua huonoimpaan mahdolliseen tapaukseen. Tavoiteltu aikavaatimus on O(m^n).

Ensin peli voi toimia pelkästään ASCII-grafiikoilla, mutta kun algoritmi on saatu toimimaan, on tarkoituksena luoda graafinen käyttöliittymä, joka näyttää samalta kuin alkuperäinen 2048-peli.
