# Toteutusdokumentti

## Minimax-algoritmi

Ratkaisualgoritmi on minimax-algoritmi alfa-beeta karsinnalla. Algoritmissa on kaksi osaa, maksimointi ja minimointi, jotka simuloivat pelin kahta eri osaa, laattojen siirtoa ja uusien laattojen luomista. Maksimointi hakee kaikki lailliset siirrot, ja luo uuden haun jokaisen siirron luomalle pelikentälle. Minimointi käy läpi kaikki mahdolliset sijainnit, joihin on mahdollista laittaa uusi laatta. Koska uusi laatta voi olla joko 2- tai 4-laatta, jokainen vapaa sijainti luo kaksi uutta pelikenttää, joille tehdään uusi haku.

Kun algoritmi pääsee haun loppuun, se kutsuu arviointialgoritmia, joka arvioi kentän heuristisen arvon. Tämä saatu arvo palautetaan hakua kutsuneelle haulle. Koska vain maksimointi vähentää syvyysarvoa, eli haku voi loppua vain maksimoinnin vuoroon, maksimoija valitsee laillisista siirroista sen, joka sai parhaan arvon, eli parhaan mahdollisen siirron.

Syntyneet parhaat arvon palautetaan minimoinnille, joka valitsee huonoimman arvon, eli huonoimman sijainnin (ja arvon) johon uusi laatta voi syntyä. Tämä prosessi jatkuu, kunnes alkuperäinen haku saa arvot kaikille laillisille siirroille (Maksimointi aloittaa haun), ja palauttaa parhaan arvon ja siten siirron. Tämä saatu siirto on paras mahdollinen siirto, jos oletetaan, että uusi laatta syntyy aina huonoimpaan paikkaan.

## Arviointi-algoritmi

Arviointi-algoritmi käyttää neljää eri arvoa pelikentän heuristisen arvon laskemiseen. Nämä ovat: monotonisuus, tasaisuus, vapaiden laattojen määrä, ja suurimman laatan arvo. Pelikentän heuristisen arvon saamiseksi, jokainen arvo ensin kerrotaan jollain painolla, ja sitten kaikki arvot lasketaan yhteen. Monotonisuus ja tasaisuus ovat rankaisevia, ne voivat vain vähentää heuristisista arvoa, eli suurin mahdollisen monotonisuus tai tasaisuus on 0. Vapaiden laattojen määrä, ja suurimman laatan arvo lisäävät heuristisista arvoa, eli niiden huonoin arvo on 0.

### Monotonisuus

Monotonisuus mittaa kuinka hyvin kaikkien laattojen arvo kasvaa jonkin kulman suuntaan. 2048-peliä pelatessa pelaaja yleensä oppii, että paras strategia pelin voittamiseen on kasata laattoja johonkin kulmaan. Monotonisuus vähentää kentän arvoa, jos se ei noudata tätä strategiaa. Monotonisuus laskeminen aloitetaan laskemalla kaikkien suuntien omat monotonisuudet. Ensin kaikki laatat käydään läpi vasemmalta oikealle. Jos laatan n+1 arvo on suurempi kuin laatan n arvo, niin vasen-suunnan monotonisuutta vähennetään. Jos n laatta on suurempi, niin oikea-suunnan monotonisuutta vähennetään. Sama tehdään myös ylös/alas-suuntaan. Tämän jälkeen kummastakin parista (vasen/oikea, ylös/alas) valitaan suurempi arvo, ja ne lasketaan yhteen, jolloin saadaan parhaan kulman monotonisuus, eli pelikentän monotonisuus.

Monotonisuus riippuu laattojen arvojen kahden logaritmin erosta. Esimerkiksi 64- ja 128-laatat vierekkäin vähentävät vasen-suunnan monotonisuutta yhdellä, ja 64- ja 256-laatat vähentävät arvoa kahdella.

#### Esimerkki

A) Monotonisuus on 0 (vasen -12, oikea 0, ylös 0, alas -12)

![image](https://user-images.githubusercontent.com/77693693/157096375-796242aa-d1ab-4a38-872c-eeda14c57b3d.png)

B) Monotonisuus on -4 (vasen -12, oikea 0, ylös -4, alas -4)

![image](https://user-images.githubusercontent.com/77693693/157098746-e2f89f5a-8e3d-411d-8e26-131837a8953f.png)

C) Monotonisuus on -12 (vasen -6, oikea -6, ylös -6, alas -6)

![image](https://user-images.githubusercontent.com/77693693/157099222-a05130a2-f949-4e4a-b773-bdcc14d72cbc.png)

### Tasaisuus

Tasaisuus mittaa kuinka paljon jokaisen laatan arvon eroaa naapurilaattojen arvoista. Arvot lasketaan kahden logaritmissa. Tasaisuuden tarkoitus on estää pienien laattojen siirtämistä suurien laattojen viereen; laatat voivat vain yhdistyä saman arvoisten laattojen kanssa, joten on hyvä pitää lähes saman arvoiset laatat vierekkäin. Naapurilaataksi lasketaan ensimmäinen laatta jokaiseen suuntaan, joka ei ole tyhjä, eli tyhjiä laattoja ei oteta mukaan tasaisuuden laskemisessa.

#### Esimerkki

Jos 2048-laatan vieressä on 1024-laatta, tai 4-laatan vieressä on 2-laatta, tasaisuus on -1, koska log2(2048) - log2(1024) = -1 = log2(4) - log2(2).

A) Tasaisuus on 0 (kaikkien laattojen naapurit ovat samoja laattoja tai 0-laattoja)

![image](https://user-images.githubusercontent.com/77693693/157104561-c975c25a-77a0-4856-9f43-940839920826.png)

B) Tasaisuus on -8 (Naapureita on yhteensä 8, jokaisen laatan naapuri on kaksi kertaa tai puolet laatan arvosta, eli -1)

![image](https://user-images.githubusercontent.com/77693693/157104947-75fbef68-f373-4d3d-8a79-e3f6eda50b81.png)

### Tyhjät laatat ja suurin laatta

Tyhjät laatat ja suurin laatta ovat yksinkertaisia arvoja, kummankin arvo on vain nimensä mukaisen arvon logaritmi. Tyhjät laatat lasketaan luonnollisella logaritmilla, ja suurin laatta kahden logaritmilla. Tämä on siksi, että suurin laatta on aina kahden potenssi, mutta tyhjiä laattoja voi olla mikä tahansa määrä nollan ja viidentoista välillä.

Tyhjien laattojen tarkoitus on estää pelin päättyminen. Peli päättyy, jos laillisia siirtoja ei ole. Jos tyhjiä laattoja on ainakin yksi, laillisia siirtoja on ainakin kaksi. On siis tärkeää pitää tyhjien laattojen määrä korkealla.

Suurin laatta vaikuttaa heuristiseen arvoon vain, kun on mahdollista luoda uusi suurin laatta. Koska pelin tarkoituksena on luoda 2048-laatta, pelikentän arvo nousee, kun sen suurimman laatan arvo nousee.

#### Esimerkki

A) Tyhjiä laattoja on 6, eli tyhjien arvojen arvo on noin 1,6. Suurin laatta on 2048, eli suurimman laatan arvo on 11.

![image](https://user-images.githubusercontent.com/77693693/157108777-28f10f11-d6b9-4d0f-ac32-92dc46b86169.png)
