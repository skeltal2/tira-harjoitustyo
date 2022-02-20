# 2048 Ratkaisija

## Dokumentaatio
- [Määrittelydokumentti](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/maarittelydokumentti.md)
- [Viikkoraportti 1](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikkoraportti1.md)
- [Viikkoraportti 2](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikkoraportti2.md)
- [Viikkoraportti 3](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikkoraportti3.md)
- [Viikkoraportti 4](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikkoraportti4.md)
- [Viikkoraportti 5](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikkoraportti5.md)

## Käyttöohje
Asenna riippuvuudet:
```
poetry install
```
Aloita peli:
```
poetry run invoke start
```
Tämän jälkeen ohjelma kysyy, haluaako käyttäjä pelata itse vai käyttää algoritmia. Peliä pelataan kirjoittamalla suunta (w, a, s, d) ja painamalla enter. Algoritmi ratkaisee (tai epäonnistuu) pelin noin 1000 siirrossa, mikä kestää noin 20 - 60 sekuntia.

Aloita peli käyttöliittymällä:
```
poetry run invoke start-ui
```
Käyttöliittymässä peliä pelataan joko WASD- tai nuolinäppäimillä. "Uusi Peli" aloittaa uuden pelin, "Lopeta" poistuu ohjelmasta, ja "Ratkaise!" käynnistää algoritmin. "Ratkaise"-napin alapuolella on valitsin, jolla voi valita minimiajan, jonka algoritmi käyttää siirtoihin (millisekunneissa).

Testit:
```
poetry run invoke test
```
Testikattavuus:
```
poetry run invoke coverage
```
Pylint:
```
poetry run invoke pylint
```
