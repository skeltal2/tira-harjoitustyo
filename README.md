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
Peliä pelataan joko WASD- tai nuolinäppäimillä. "Uusi Peli" aloittaa uuden pelin, "Lopeta" poistuu ohjelmasta, ja "Ratkaise!" käynnistää algoritmin. "Ratkaise"-napin alapuolella on valitsin, jolla voi valita minimiajan, jonka algoritmi käyttää siirtoihin (millisekunneissa). Yksi peli kestää noin 1000 siirtoa tai 30-60 sekuntia.

Pelin voi myös aloittaa ilman käyttöliittymää komennolla
```
poetry run invoke start -no-ui
```

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
