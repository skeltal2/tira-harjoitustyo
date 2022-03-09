# Toteutusdokumentti

## Minimax-algoritmi

Ratkaisualgoritmi on minimax-algoritmi alfa-beeta karsinnalla. Algoritmissa on kaksi osaa, maksimointi ja minimointi, jotka simuloivat pelin kahta eri osaa, laattojen siirtoa ja uusien laattojen luomista. Maksimointi hakee kaikki lailliset siirrot, ja luo uuden haun jokaisen siirron luomalle pelikentälle. Minimointi käy läpi kaikki mahdolliset sijainnit, joihin on mahdollista laittaa uusi laatta. Koska uusi laatta voi olla joko 2- tai 4-laatta, jokainen vapaa sijainti luo kaksi uutta pelikenttää, joille tehdään uusi haku.

Kun algoritmi pääsee haun loppuun, se kutsuu arviointialgoritmia, joka arvioi kentän heuristisen arvon. Tämä saatu arvo palautetaan hakua kutsuneelle haulle. Koska vain maksimointi vähentää syvyysarvoa, eli haku voi loppua vain maksimoinnin vuoroon, maksimoija valitsee laillisista siirroista sen, joka sai parhaan arvon, eli parhaan mahdollisen siirron.

Syntyneet parhaat arvon palautetaan minimoinnille, joka valitsee huonoimman arvon, eli huonoimman sijainnin (ja arvon) johon uusi laatta voi syntyä. Tämä prosessi jatkuu, kunnes alkuperäinen haku saa arvot kaikille laillisille siirroille (Maksimointi aloittaa haun), ja palauttaa parhaan arvon ja siten siirron. Tämä saatu siirto on paras mahdollinen siirto, jos oletetaan, että uusi laatta syntyy aina huonoimpaan paikkaan.

## Arviointi-algoritmi

Arviointi-algoritmi käyttää viittä eri arvoa pelikentän heuristisen arvon laskemiseen. Nämä ovat: monotonisuus, tasaisuus, vapaiden laattojen määrä, suurimman laatan arvo, suurimman laatan sijainti. Pelikentän heuristisen arvon saamiseksi jokainen arvo ensin kerrotaan jollain painolla, ja sitten kaikki arvot lasketaan yhteen. Monotonisuus, tasaisuus ja suurimman laatan sijainti ovat rankaisevia, ne voivat vain vähentää heuristisista arvoa, eli suurin mahdollisen monotonisuus tai tasaisuus on 0. Vapaiden laattojen määrä, ja suurimman laatan arvo lisäävät heuristisista arvoa, eli niiden huonoin arvo on 0.

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

### Tyhjät laatat, ja suurimman laatan arvo ja sijanti

Tyhjät laatat ja suurimman laatan arvo ovat yksinkertaisia arvoja, kummankin arvo on vain nimensä mukaisen arvon logaritmi. Tyhjät laatat lasketaan luonnollisella logaritmilla, ja suurin laatta kahden logaritmilla. Tämä on siksi, että suurin laatta on aina jokin kahden potenssi, mutta tyhjiä laattoja voi olla vain alle 15.

Tyhjien laattojen tarkoitus on estää pelin päättyminen. Peli päättyy, jos laillisia siirtoja ei ole. Jos tyhjiä laattoja on ainakin yksi, laillisia siirtoja on ainakin kaksi. On siis tärkeää pitää tyhjien laattojen määrä korkealla.

Suurimman laatan arvo vaikuttaa heuristiseen arvoon vain, jos suurimman laatan arvo kasvaa. Sen tarkoitus on vähentää kentän laattojen määrää ja ohjata algoritmia luomaan uusi suurin laatta, jos se on mahdollista. Pelin tarkoituksena on luoda 2048-laatta, joka voidaan saavuttaa vain kasvattamalla suurimman laatan arvoa. Se myös auttaa lisäämään tyhjien laattojen määrää, koska usein suurimman laatan muodostamiseen tarvitaan useita laattoja, jotka vapautuvat, kun suurin laatta muodostetaan.

Suurimman laatan sijainti vähentää heuristisista arvoa, jos suurin laatta ei ole kulmassa. Sen tarkoituksena on helpottaa suurimman laatan kasvattamista. Jos suurin laatta ei ole kulmassa, on mahdollista, että sen kummallekin puolella kasaantuu laattoja. Esimerkiksi 1024-laatan kummallekin puolelle voi muodostua 512-laatta, joita on vaikea yhdistää. Tämä myös vie kolme laattaa, jotka voitaisiin yhdistää yhdeksi laataksi, mikä tekee pelilaudan täyttymisestä todennäköisempää. Jos suurin laatta on kulmassa, muut suuret laatat kasautuvat sen vierekkäisille reunoille, joista ne on helppo yhdistää.

#### Esimerkki

A) Tyhjiä laattoja on 6, eli tyhjien laattojen arvo on noin 1,6. Suurin laatta on 2048, eli suurimman laatan arvo on 11.

![image](https://user-images.githubusercontent.com/77693693/157108777-28f10f11-d6b9-4d0f-ac32-92dc46b86169.png)

B) Oikeasta yläkulmasta voidaan helposti muodostaa 2048-laatta kolmella siirrolla (vasen → ylös → vasen). Vasen alakuma tarvisee muita laattoja tietyissä kohdissa, jotta siitä voi muodostaa 2048-laatan, koska suurin laatta ei ole kulmassa.

![image](https://user-images.githubusercontent.com/77693693/157549583-836fd885-4a68-4cfc-8ae2-6a888cb667ec.png)

## Lähteet

https://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048/22389702#22389702 - Algoritmin idea ja monotonisuuden laskeminen

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning - Apua alfa-beeta karsinnan toteutukseen
