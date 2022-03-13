# Testausdokumentti

Ohjelmassa on kaksi eri osaa, peli ja logiikka. Peli sisältää käyttöliittymän ja algoritmin suorittamisen, joten sitä ei ole testattu. Logiikassa on kolme eri osaa, ```board.py```, ```minimax.py``` ja ```heuristic.py```, jotka ovat vastuussa pelilaudasta, minimax-algoritmista ja heuristiikka-algoritmista.

### Pelilauta
Pelilauta sisältää 2048-pelin logiikan, joita muut moduulit voivat käyttää kutsumalla ```board``` olion eri metodeja. Näistä tärkein on ```move``` metodi, joka on vastuussa pelilaudan laattojen liikuttamisesta. Pelilaudan testaaminen sisältää monta eri testiä, jotka varmistavat, että laatat siirtyvät oikein. Laattojen pitää yhdistyä toiseen samaan laattaan, jos ne törmäävät toisiinsa, mutta laatta voi yhdistyä vain kerran yhdellä siirrolla. Näitä testaa kaksi eri testiä (pystysuuntaan ja vaakasuuntaan liikkuminen), joissa kummassakin on pelilauta, jossa on kaikki eri mahdolliset siirtotyypit.

Muut pelilaudan testit testaavat pelilaudan muita metodeja; osaako pelilauta sijoittaa uuden laatan, löytääkö se tietyn laatan naapurit, tunnistaako se, jos peli on voitettu, löytääkö se tyhjien laattojen sijainnit, löytääkö se lailliset siirrot (ja toimiiko se oikein, jos laillisia siirtoja ei ole) ja onko pelilaudan merkkijono esitys oikein.

### Minimax
Minimax-algoritmin testaus on kaksi yksinkertaista testiä, jotka testaavat löytääkö algoritmi pelilaudan parhaan siirron, jos paras siirto on selvä. Selvä siirto on joko siirrto, jossa kaikki muut päättyvät huonoon pelilautaan, tai muilla siirroilla ei saada muodostettua 2048-laattaa.

### Heuristiikka
Heuristiikka-algoritmia testataan katsomalla saako algoritmi jokaisen eri heuristiikan arvon laskettua oikein. Neljä eri testiä testaavat algoritmin neljää eri osaa, monotonisuutta, tasaisuutta, suurinta laattaa, ja vapaiden laattojen määrää. Jokainen arvo lasketaan erikseen. Viimeinen testi laskee yksinkertaisen pelilaudan koko heuristisen arvon.

## Suorituskyky ja tarkkuus

Suorituskykyä mitataan ```performance.py``` moduulilla. Moduuli suorittaa käyttäjän antaman verran pelejä, ja kirjoittaa niistä saadut tulokset kahteen eri tiedostoon. Suorituskyvyn voi laskea ```test_results.json``` tiedostosta. Tiedostoon kirjoitetaan jokaisen eri pelin:

- Suoritusaika sekunneissa
- Pisteet
- Siirtojen määrät
- Voitettiinko peli
- Kuinka monta siirtoa jokaisen arvon saavuttamiseen meni
- Mikä oli suurin saavutettu arvo

Algoritmin tarkkuutta, eli sen kykyä saavuttaa 2048-laatta, mitatessa pitää suorittaa noin 30 peliä. Seuraavissa testeissa huomaa, että esimerkiksi 10 pelillä, tarkkuus voi vaihdella jopa 30 prosenttiyksilöllä (testi 1: 60%, testi 2: 90%), eli suuri määrä pelejä on pelattava, jotta tarkkuus lasketaan tarkasti. Tarkkuus jokaisen pelin jälkeen kirjoitetaan ```sq_wins.json``` tiedostoon.

Testauksessa kestää 15 - 60 sekuntia per peli, riippuen tietokoneen suorituskyvystä, ja siitä milloin jokainen peli lopetetaan.

## Testauksen tulokset

### Testi 1
Data kerättiin suorittamalla 50 peliä. 2048-laatan saavuttaminen päätti pelin.

![tarkkuus](https://user-images.githubusercontent.com/77693693/157531050-b5cc5a50-5922-4c85-aa6c-313cf72b1d07.svg)

- 50 pelistä 70% saavutti 2048-laatan
- Suorittamiseen meni yhtensä 1750,3988 sekuntia (noin 30 minuuttia)
- Yksi peli kesti keskimäärin 35 sekuntia
- Yhteensä 48 930 siirtoa
- Eli yhteen siirtoon meni keskimäärin 35,8 millisekuntia
- Yksi peli päättyi 128-laattaan (!?)

| Arvo | Määrä | Osa |
|------|-------|-----|
| 2048 | 35    | 70% |
| 1024 | 47    | 94% |
| 512  | 49    | 98% |
| <512 | 50    | 100%|

### Testi 2
Data kerättiin suorittamalla 50 peliä. Peli jatkui, kun 2048-laatta oli saavutettu.

![tarkkuus](https://user-images.githubusercontent.com/77693693/157554400-4f1c7b82-95e0-4fd8-b63c-96d86553f882.svg)

- 50 pelistä 68% saavutti 2048-laatan
- Suorittamiseen meni yhteensä 2493,3492 sekuntia (noin 42 minuuttia)
- Yksi peli kesti keskimäärin 50 sekuntia
- Yhteensä 72 269 siirtoa
- Eli yhteen siirtoon meni keskimäärin 34,5 millisekuntia

| Arvo | Määrä | Osa |
|------|-------|-----|
| 4096 | 1     | 2%  |
| 2048 | 34    | 68% |
| 1024 | 48    | 96% |
|  512 | 50    | 100%|
