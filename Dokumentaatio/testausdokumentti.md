# Testausdokumentti

Ohjelmassa on kaksi eri osaa, peli ja logiikka. Peli sisältää käyttöliittymän ja algoritmin suorittamisen, joten sitä ei ole testattu. Logiikassa on kolme eri osaa, ```board.py```, ```minimax.py``` ja ```heuristic.py```, jotka ovat vastuussa pelilaudasta, minimax-algoritmista ja heuristiikka-algoritmista.

### Pelilauta
Pelilauta sisältää 2048-pelin logiikan, joita muut moduulit voivat käyttää kutsumalla ```board``` olion eri metodeja. Näistä tärkein on ```move``` metodi, joka on vastuussa pelilaudan laattojen liikuttamisesta. Pelilaudan testaaminen sisältää monta eri testiä, jotka varmistavat, että laatat siirtyvät oikein. Laattojen pitää yhdistyä toiseen samaan laattaan, jos ne törmäävät toisiinsa, mutta laatta voi yhdistyä vain kerran yhdellä siirrolla. Näitä testaa kaksi eri testiä (pystysuuntaan ja vaakasuuntaan liikkuminen), joissa kummassakin on pelilauta, jossa on kaikki eri mahdolliset siirtotyypit.

Muut pelilaudan testit testaavat pelilaudan muita metodeja, osaako pelilauta sijoittaa uuden laatan, löytääkö se tietyn laatan naapurit, tunnistaako se, jos peli on voitettu, löytääkö se tyhjien laattojen sijainnit, löytääkö se lailliset siirrot (ja toimiiko se oikein, jos laillisia siirtoja ei ole) ja onko pelilaudan merkkijono esitys oikein.

### Minimax
Minimax-algoritmin testaus on kaksi yksinkertaista testiä, jotka testaavat löytääkö algoritmi pelilaudan parhaan siirron, jos paras siirto on selvä. Selvä siirto on joko siirrot, jossa kaikki muut päättyvät huonoon pelilautaan, tai muilla siirroilla ei saada muodostettua 2048-laattaa.

### Heuristiikka
Heuristiikka-algoritmia testataan katsomalla saako algoritmi jokaisen eri heuristiikan arvon laskettua oikein. Neljä eri testiä testaavat algoritmin neljää eri osaa, monotonisuutta, tasaisuutta, suurinta laattaa, ja vapaiden laattojen määrää. Jokainen arvo lasketaan erikseen. Viimeinen testi laskee yksinkertaisen pelilaudan koko heuristisen arvon.

## Suorituskyky ja tarkkuus

Suorituskykyä mitataan ```performance.py``` moduulilla. Moduuli suorittaa käyttäjän antaman verran pelejä, ja kirjoittaa niistä saadut tulokset kahteen eri tiedostoon. Suorituskyvyn voi laskea ```test_results.json``` tiedostosta. Tiedostoon kirjoitetaan jokaisen eri pelin:

- Suoritusaika sekunneissa
- Pisteet
- Siirtojen määrät
- Voitettiinko peli
- Kuinka monta siirtoa jokaisen arvon saavuttamiseen meni?
- Mikä oli suurin saavutettu arvo

Algoritmin tarkkuutta, eli sen kykyvä saavuttaa 2048-laatta, mitatessa pitää suorittaa noin 30 peliä. Alemmilla arvoilla, esimerkiksi 10 pelillä, tarkkuus voi vaihdella jopa 30 prosenttiyksilöllä, eli suuri määrä pelejä on pelattava, jotta tarkkuus lasketaan tarkasti. Tarkkuus jokaisen pelin jälkeen kirjoitetaan ```sq_wins.json``` tiedostoon.

## Testauksen tulokset

Data kerättiin suorittamalla 50 peliä.

![tarkkuus](https://user-images.githubusercontent.com/77693693/157531050-b5cc5a50-5922-4c85-aa6c-313cf72b1d07.svg)

- 50 pelistä 70% saavutti 2048-laatan
- Suorittamiseen meni 1750,3988 sekuntia
- Yhteensä 48 930 siirtoa
- Eli yhteen siirtoon meni keskimäärin 35 ms

| Arvo | Määrä | Osa |
|------|-------|-----|
| 2048 | 35    | 70% |
| 1024 | 47    | 94% |
| 512  | 49    | 98% |
| <512 | 1     | 100%|
