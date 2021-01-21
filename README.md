# analiza_podatkov_skotski_viskiji

<h2>Škotski viski</h2>

Analiziral bom škotske viskije s spletne strani https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky.

Za vsak viski bom zajel:<ul>
  <li>ime</li>
  <li>volumen</li>
  <li>procent alkohola</li>
  <li>procent alkohola na liter</li>
  <li>ali so standardni ali posebni in stari</li>
  <li>iz katerega dela Škotske prihajajo</li>
  </ul>
  Delovne hipoteze:<ul>
  <li>Katera regija ima v povprečju najdržje viskije in katera najcenejše?</li>
  <li>Ali procent alkohola vpliva na ceno viskija oziroma ali velja večji procent alkohola dražji bo viskij?</li>
  <li>Ali je večji procent alkohola v posebnih in starih viskijih kot v standardnih vskijih?</li>
  <li>70% viskijev je cenejših od 200 funtov.</li>
  <li>Kakšen je povprečni odstotek alkohola v viskijih za vsako regijo?</li>
<h3>Naložene datotke</h3><ul>
  <li>python datoteki sta za pobiranje podatkov s spletne strani in za zapis teh podatkov v csv in json.<br>
    Datoteka orodja.py je "pobrana" s predavanj Programiranja 1,  ki jo je napisal doc. dr. Matija Pretnar.<br>
    Druga datoteka pa je poberi_z_orodji.py, ki naredi html datoteke(teh nisem prilagal), iz teh datotek pa izlušči relavantne podatke v csv in json datoteke..</li>
  <li>skotski_viskiji.csv in skotski_viskiji.json sta datoteki ki sta bili narjeni s poberi_z_orodji.py, kjer so shranjeni osnovni podatki za vse viskije.</li>
  <li>mapi viskiji_po_regijah in viskiji_standardni_ali_stari vsebujeta csv in json datoteke pridobljene z poberi_z_orodji.py, vsaka datoteka vsebuje viskije le ene regije ali le standardne ali le stare viskije.</li>
  <li>Datoteka obdelava_podatkov.ipynb pa je datoteka, kjer sem obdelal pridobljene podatke, ter ovrgel ali potrdil delovne hipoteze.</li>
  </ul>
  <h3>Navodila za uporabnika</h3>
  Za prenos podatkov boste potrebovali datoteke orodja.py in poberi_z_orodji.py, dovolj je le zagnati slednjo datoteko, ki bo naredila vse html, json in csv datoteke.
  To bo vse kar boste potrebovali za zagon datoteke obdelava_podatkov.ipynb.
