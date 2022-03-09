# Käyttöohje

Ohjelman riippuvuudet asennetaan komennolla:
```
poetry install
```

Ohjelma käynnistetään komennolla:
```
poetry run invoke start
```
Komennon suorittaminen avaa seuraavan käyttöliittymän:

![image](https://user-images.githubusercontent.com/77693693/157441545-3ed9661a-17d6-4901-9bc9-1ee239d3af09.png)

A) Käynnistä ratkaisualgoritmi

B) Valitse kuinka monta millisekuntia algoritmi odottaa vähintään jokaisen siirron välissä

C) Pysähtyykö peli kun 2048-laatta on saavutettu (vaikuttaa myös algoritmin toimintaan)

D) Viimeisimmän siirron suunta

E) Piste ja siirto laskuri

F) Aloita uusi peli

G) Poistu ohjelmasta

## Pelin pelaaminen

2048 on pulmapeli, jonka tavoitteena on laattoja yhdistämällä muodostaa 2048-laatta. Pelinkenttä on 4 x 4 ruudukko, jossa on laattoja. Jokaisella laatalla on arvo, joka on jokin kahden potenssi. Pelilaudalla olevia laattoja voi siirtä neljään eri suuntaan (vasen, oikea, ylös, alas), jolloin kaikki laatat liikkuvat valittuun suuntaan. Jos mikään laatta ei siirry, siirto on laiton eikä sitä voitehdä. Jos kaksi saman arvoista laattaa törmää toisiinsa, ne yhdistyvät yhdeksi laataksi, jonka arvo on yhdistyneiden laattojen summa. Jokaisella siirrolla pelilaudalle syntyy uusi laatta, jonka arvo on joka 2 tai 4. Peli päätty, jos laillisia siirtoja ei voi enää tehdä.

Ohjelman peliä pelataan joko nuolinäppäimillä tai WASD-näppäimillä.

## Muut komennot

Ohjelman voi myös suorittaa kokonaan terminaalissa komennolla:
```
poetry run invoke start --no-ui
```

Tämän jälkeen ohjelma kysyy haluaako käyttäjä käyttää algoritmia (y/n). Jos käyttäjä valitsee (y), algoritmi käynnistyy. Jos käyttäjä valitsee (n), peliä voi pelata ASCII grafiikoilla. Ohjelmasta voi poistua missä tahansa vaiheessa Ctrl+C näppäinyhdistelmällä.

Testit suoritetaan komennolla:
```
poetry run invoke test
```

Testikattavuuden voi nähdä komennolla:
```
poetry run invoke coverage
```

Ohjelman suorituskykyä voi testata komennolla:
```
poetry run invoke perf
```

Suorituskykyä testatessa ohjelma kysyy ensin montako peliä algoritmi pelaa. Tämän jälkeen ohjelma suorittaa algoritmin käyttäjän antaman määrän verran. Testin tulokset voi nähdä  ```sq_test.json``` ja ```test_results.json``` tiedostoista. ```sq_test.json``` tiedostossa kaikkien tähän asti suoritettujen pelien tarkkuus jokaiselle eri pelille. ```test_results.json``` tiedostossa on jokaisen pelin tiedot (aika, pisteet, suurin laatta, jne.)

Pylintin voi suorittaa komennolla:
```
poetry run invoke pylint
```
