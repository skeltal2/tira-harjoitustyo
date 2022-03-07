# Toteutusdokumentti

## Minimax-algoritmi

Ratkaisualgoritmi on minimax-algoritmi alfa-beeta karsinnalla. Algoritmissa on kaksi osaa, maximointi ja minimointi, jotka simiuloivat pelin kahta eri osaa, laattojen siirtoa ja uusien laattojen luomista. Maximointi hakee kaikki lailliset siirrot, ja luo uuden haun jokaisen siirron luomalle pelikentälle. Minimointi käy läpi kaikki mahdolliset sijainnit, joihin on mahdollista laittaa uusi laatta. Koska uusi laatta voi olla joko 2- tai 4-laatta, jokainen vapaa sijainti luo kaksi uutta pelikenttää, joille tehdään uusi haku.

Kun algoritmi pääsee haun loppuun, se kutsuu arviointi-algoritmia, joka arvioi kentän heuristisen arvon. Tämä saatu arvo palautetaan hakua kutsuneelle haulle. Koska vain maximointi vähentää syvyysarvoa, eli haku voi loppua vain maksimoinnin vuoroon, maximoija valitsee laillisista siirroista sen, joka sai parhaan arvon, eli parhaan mahdollisen siirron.

Syntyneet parhaat arvon palautetaan minimoinnille, joka valitsee huonoimman arvon, eli huonoimman sijainnin (ja arvon) johon uusi laatta voi syntyä. Tämä prosessi jatkuu, kunnes alkuperäinen haku saa arvot kaikille lailisille siirroille (maximointi aloittaa haun), ja palauttaa parhaan arvon ja siten siirron. Tämä saatu siirto on paras mahdollinen siirto, jos oletetaan, että uusi laatta syntyy aina huonoimpaan paikkaan.

## Arviointi-algoritmi

Arviointi-algoritmi käyttää neljää eri arvoa pelikentän heuristisen arvon laskemiseen. Nämä ovat: monotonisuus, tasaisuus, vapaiden laattojen määrä, ja suurimman laatan arvo. Pelikentän heuristisen arvon saamiseksi, jokainen arvo ensin kerrotaan jollain painolla, ja sitten kaikki arvot lasketaan yhteen. Monotonisuus ja tasaisuus ovat rankaisevia, ne voivat vain vähentää heuristisista arvoa, eli suurin mahdollisen monotonisuus tai tasaisuus on 0. Vapaiden laattojen määrä, ja suurimman laatan arvo lisäävät heuristisista arvoa.

### Monotonisuus

Monotonisuus mittaa kuinka hyvin kaikkien laattojen arvo kasvaa jonkin kulman suuntaan. 2048-peliä pelatessa pelaaja yleensä oppii, että paras strategia pelin voittamiseen on kasata laattoja johonkin kulmaan. Monotonisuus vähentää kentän arvoa, jos se ei noudata tätä strategiaa. Monotosuus laskeminen aloitetaan laskemalla kaikkien suuntien omat monotonisuudet. Ensin kaikki laatat käydään läpi vasemmalta oikealle. Jos laatan n+1 arvo on suurempi kuin laatan n arvo, niin vasen-suunnan monotonisuutta vähennetään. Jos n laatta on suurempi, niin oikea-suunnan monotonisuutta vähennetään. Sama tedään myös ylös/alas-suuntaan. Tämän jälkeen kummastakin parista (vasen/oikea, ylös/alas) valitaan suurempi arvo, ja ne lasketaan yhteen, jolloin saadaan parhaan kulman monotonisuus, eli pelikentän monotonisuus.

Monotonisuus riippuu laattojen arvojen kahden logaritmin erosta. Esimerkiksi 64- ja 128-laatat vierekkäin vähentävät vasen-suunnan monotonisuutta yhdellä, ja 64- ja 256-laatat vähentävät arvoa kahdella.

#### Esimerkki:

A) Monotonisuus on 0 (vasen -12, oikea 0, ylös 0, alas -12)

![image](https://user-images.githubusercontent.com/77693693/157096375-796242aa-d1ab-4a38-872c-eeda14c57b3d.png)

B) Monotonisuus on -4 (vasen -12, oikea 0, ylös -4, alas -4)

![image](https://user-images.githubusercontent.com/77693693/157098746-e2f89f5a-8e3d-411d-8e26-131837a8953f.png)


C) Monotonisuus on -16 (vasen -6, oikea -6, ylös -6, alas -6)

![image](https://user-images.githubusercontent.com/77693693/157099222-a05130a2-f949-4e4a-b773-bdcc14d72cbc.png)


