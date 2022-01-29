# Viikkoraportti 1

Työmäärä: 13 h

Tällä viikolla toteutin pelilogiikan ja yksinkertaisen pelisilmukan. Suorittamalla ohjelman käynnistyy tekstiversio 2048-pelistä, joka toimii kuten alkuperäisen peli. Peliä voi pelata kirjoittamalla suunnan (w, a, s, d) ja painamalla Enter. Peli tunnistaa, voiko siirron tehdä, ja päättyy kun siirtoja ei voi tehdä tai 2048-laatta on luotu. Suurin osa ajasta meni move()-metodin kirjoittamiseen. Kirjoitin sen kaksi kertaan, koska ensimmäisellä kerralla metodi ei toiminut oikein tietyissä tilanteissa. Jos rivillä oli kolme laattaa, joista kaksi liikkuu ja yhdistyy, kolmas laatta ei liikkunut oikein. Päätin korjata metodin kirjoittamalla sen kokonaan uudelleen käyttäen toista tekniikkaa. Uusi metodi on tehokkaampi ja toimii oikein.

Lisäsin myö Poetryn, jolla voi tehdä riippuvuuksien hallintaa.
