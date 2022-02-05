# 2048 Ratkaisija

## Dokumentaatio
- [Määrittelydokumentti](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/maarittelydokumentti.md)
- [Viikkoraportti 1](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikkoraportti1.md)
- [Viikkoraportti 2](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikkoraportti2.md)
- [Viikkoraportti 3](https://github.com/skeltal2/tira-harjoitustyo/blob/main/Dokumentaatio/viikkoraportti3.md)

## Käyttöohje
Asenna riippuvuudet:
```
poetry install
```
Aloita peli:
```
poetry run invoke start
```
Tämän jälkeen ohjelma kysyy, haluaako käyttäjä pelata itse vai käyttää (keskeneräistä) algoritmia. Peliä pelataan kirjoittamalla suunta (w, a, s, d) ja painamalla enter.

Suorita testit:
```
poetry run invoke test
```
Suorita pylint:
```
poetry run invoke pylint
```
