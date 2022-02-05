# Viikkoraportti 3

Työmäärä: 14 h

Tällä viikolla lisäsin pytest, coveragen ja pylintin projektiin. Aloitin tekemään yksikkötestejä, tällä hetkellä kaikki testit liittyvät pelilaudan laattojen liikkumiseen. Aloitin lisäämään myös docstringejä ja korjaamaan koodia, jotta se pysyy PEP8-tyylissä. Suurin osa tämän viikon työmäärästä meni ratkaisualgoritmin ensimmäisen version kirjoittamiseen. Tällä hetkellä ratkaisualgoritmi on yksinkertainen rekursiivinen algoritmi, jonka ainoa heuristiikka on pelilaudan kokonaispisteet. Vaikka se on vielä todella yksinkertainen, se saavuttaa 1024-laatan noin 80% ajasta ja 2048-laatan noin 20% ajasta (jos siirrot valitaan satunnaisesti, 256-laatta saavutetaan vain noin 10% ajasta). Yritin keksiä parempaa heuristiikkaa, mutta kaikki mitä keksin toimi huonommin, kuin yksinkertaisesti pelilaudan pisteiden laskeminen.

Seuraavalla viikolla on tavoitteena kirjoittaa algoritmi ja yksikkötestit loppuun.
