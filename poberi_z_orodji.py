import orodja
import re
import requests
import json

def string_to_float (niz):
    if "," in niz:
       return float(niz.replace(",", ""))
    return float(niz)

def percent_to_float(niz):
    if "%" in niz :
       return round(float(niz.replace("%", "")) / 100, 2)
    return round (float(niz) / 100, 2)

def page_to_viskiji(page_content):

    pattern = re.compile(r'<div class="information">(.*?)</a>', re.DOTALL)
    viskiji = [m.group(1).strip() for m in re.finditer(pattern, page_content)]

    return viskiji

def get_dict_from_block(block):
    
    pattern_ime= re.compile(r'<div class="name">(?P<ime>.*?)<', re.DOTALL)
    pattern_cena = re.compile(r'<span class="price">£(?P<cena>.*?)</span>', re.DOTALL)
    pattern_kolicina = re.compile(r'<span class="meta">(?P<kolicina>.*?)cl\s/',re.DOTALL)
    pattern_procent_alkohola = re.compile(r'<span class="meta">.*?/\s(?P<procent_alkohola>.*?)</span>', re.DOTALL)
    pattern_cena_na_enoto = re.compile(r'<span class="price-meta">\(£(?P<cena_na_enoto>.*?)\)</span>', re.DOTALL)
    match_ime = re.search(pattern_ime, block)
    match_cena = re.search(pattern_cena, block)
    match_kolicina = re.search(pattern_kolicina, block)
    match_procent_alkohola = re.search(pattern_procent_alkohola, block)
    match_cena_na_enoto = re.search(pattern_cena_na_enoto, block)

    slovar = {'ime': match_ime.group('ime') if match_ime is not None else None,
    'cena': string_to_float(match_cena.group('cena')) if match_cena is not None else None,
    'kolicina': match_kolicina.group('kolicina')if match_kolicina is not None else None,
    'procent_alkohola': percent_to_float(match_procent_alkohola.group('procent_alkohola'))if match_procent_alkohola is not None else None, 
    'cena_na_enoto': match_cena_na_enoto.group('cena_na_enoto')if match_cena_na_enoto is not None else None}
    return slovar



stevilo_strani = 45
stevilo_viskijev_na_stran = 60
count = 0
slovarji_viskijev = []

for start in range(1, stevilo_strani + 1):
    url = f'https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?pg={start}#productlist-filter'
    
    prvi_pobran = 1 + count * stevilo_viskijev_na_stran
    zadnji_pobran = (count + 1) * stevilo_viskijev_na_stran
    datoteka = f'Skotski_viskiji/{prvi_pobran}-{zadnji_pobran}.html'
    count +=1

    orodja.shrani_spletno_stran(url, datoteka)

    vsebina = orodja.vsebina_datoteke(datoteka) 
    viskiji = page_to_viskiji(vsebina)
    for viski in viskiji:
        slovarji_viskijev.append(get_dict_from_block(viski))

print(len(slovarji_viskijev))

orodja.zapisi_csv(slovarji_viskijev, slovarji_viskijev[0].keys(),'skotski_viskiji.csv')

with open ('skotski_viskiji.json', 'w') as f:
    json.dump (slovarji_viskijev, f, indent = 2, ensure_ascii = True)




#poberem z orodji še vsako posamično regijo posebaj
## 1 CAMPBELTOWN

stevilo_strani_campbeltown = 2
count_campbeltown = 0
slovarji_viskijev_campbeltown = []

for start in range(1, stevilo_strani_campbeltown + 1):
    url = f'https://www.thewhiskyexchange.com/c/316/campbeltown-single-malt-scotch-whisky?filter=true&rfdata=&pg={start}#productlist-filter'
    
    prvi_pobran = 1 + count_campbeltown * stevilo_viskijev_na_stran
    zadnji_pobran = (count_campbeltown + 1) * stevilo_viskijev_na_stran
    datoteka = f'Skotski_viskiji_campbeltown/{prvi_pobran}-{zadnji_pobran}.html'
    count_campbeltown +=1

    orodja.shrani_spletno_stran(url, datoteka)

    vsebina = orodja.vsebina_datoteke(datoteka) 
    viskiji = page_to_viskiji(vsebina)
    for viski in viskiji:
        slovarji_viskijev_campbeltown.append(get_dict_from_block(viski))

print(len(slovarji_viskijev_campbeltown))

orodja.zapisi_csv(slovarji_viskijev_campbeltown, slovarji_viskijev_campbeltown[0].keys(),'viskiji_po_regijah/skotski_viskiji_campbeltown.csv')

with open ('viskiji_po_regijah/skotski_viskiji_campbeltown.json', 'w') as f:
    json.dump (slovarji_viskijev_campbeltown, f, indent = 2, ensure_ascii = True)

## HIGHLAND

stevilo_strani_highland = 11
count_highland = 0
slovarji_viskijev_highland = []

for start in range(1, stevilo_strani_highland + 1):
    url = f'https://www.thewhiskyexchange.com/c/313/highland-single-malt-scotch-whisky?filter=true&rfdata=&pg={start}#productlist-filter'
    
    prvi_pobran = 1 + count_highland * stevilo_viskijev_na_stran
    zadnji_pobran = (count_highland + 1) * stevilo_viskijev_na_stran
    datoteka = f'Skotski_viskiji_highland/{prvi_pobran}-{zadnji_pobran}.html'
    count_highland +=1

    orodja.shrani_spletno_stran(url, datoteka)

    vsebina = orodja.vsebina_datoteke(datoteka) 
    viskiji = page_to_viskiji(vsebina)
    for viski in viskiji:
        slovarji_viskijev_highland.append(get_dict_from_block(viski))

print(len(slovarji_viskijev_highland))

orodja.zapisi_csv(slovarji_viskijev_highland, slovarji_viskijev_highland[0].keys(),'viskiji_po_regijah/skotski_viskiji_highland.csv')

with open ('viskiji_po_regijah/skotski_viskiji_highland.json', 'w') as f:
    json.dump (slovarji_viskijev_highland, f, indent = 2, ensure_ascii = True)

## ISLAND

stevilo_strani_island = 4
count_island = 0
slovarji_viskijev_island = []

for start in range(1, stevilo_strani_island + 1):
    url = f'https://www.thewhiskyexchange.com/c/315/island-single-malt-scotch-whisky?filter=true&rfdata=&pg={start}#productlist-filter'
    
    prvi_pobran = 1 + count_island * stevilo_viskijev_na_stran
    zadnji_pobran = (count_island + 1) * stevilo_viskijev_na_stran
    datoteka = f'Skotski_viskiji_island/{prvi_pobran}-{zadnji_pobran}.html'
    count_island +=1

    orodja.shrani_spletno_stran(url, datoteka)

    vsebina = orodja.vsebina_datoteke(datoteka) 
    viskiji = page_to_viskiji(vsebina)
    for viski in viskiji:
        slovarji_viskijev_island.append(get_dict_from_block(viski))

print(len(slovarji_viskijev_island))

orodja.zapisi_csv(slovarji_viskijev_island, slovarji_viskijev_island[0].keys(),'viskiji_po_regijah/skotski_viskiji_island.csv')

with open ('viskiji_po_regijah/skotski_viskiji_island.json', 'w') as f:
    json.dump (slovarji_viskijev_island, f, indent = 2, ensure_ascii = True)

## ISLAY

stevilo_strani_islay = 9
count_islay = 0
slovarji_viskijev_islay = []

for start in range(1, stevilo_strani_islay + 1):
    url = f'https://www.thewhiskyexchange.com/c/50/islay-single-malt-scotch-whisky?filter=true&rfdata=&pg={start}#productlist-filter'
    
    prvi_pobran = 1 + count_islay * stevilo_viskijev_na_stran
    zadnji_pobran = (count_islay + 1) * stevilo_viskijev_na_stran
    datoteka = f'Skotski_viskiji_islay/{prvi_pobran}-{zadnji_pobran}.html'
    count_islay +=1

    orodja.shrani_spletno_stran(url, datoteka)

    vsebina = orodja.vsebina_datoteke(datoteka) 
    viskiji = page_to_viskiji(vsebina)
    for viski in viskiji:
        slovarji_viskijev_islay.append(get_dict_from_block(viski))

print(len(slovarji_viskijev_islay))

orodja.zapisi_csv(slovarji_viskijev_islay, slovarji_viskijev_islay[0].keys(),'viskiji_po_regijah/skotski_viskiji_islay.csv')

with open ('viskiji_po_regijah/skotski_viskiji_islay.json', 'w') as f:
    json.dump (slovarji_viskijev_islay, f, indent = 2, ensure_ascii = True)

## LOWLAND

stevilo_strani_lowland = 3
count_lowland = 0
slovarji_viskijev_lowland = []

for start in range(1, stevilo_strani_lowland + 1):
    url = f'https://www.thewhiskyexchange.com/c/312/lowland-single-malt-scotch-whisky?filter=true&rfdata=&pg={start}#productlist-filter'
    
    prvi_pobran = 1 + count_lowland * stevilo_viskijev_na_stran
    zadnji_pobran = (count_lowland + 1) * stevilo_viskijev_na_stran
    datoteka = f'Skotski_viskiji_lowland/{prvi_pobran}-{zadnji_pobran}.html'
    count_lowland +=1

    orodja.shrani_spletno_stran(url, datoteka)

    vsebina = orodja.vsebina_datoteke(datoteka) 
    viskiji = page_to_viskiji(vsebina)
    for viski in viskiji:
        slovarji_viskijev_lowland.append(get_dict_from_block(viski))

print(len(slovarji_viskijev_lowland))

orodja.zapisi_csv(slovarji_viskijev_lowland, slovarji_viskijev_lowland[0].keys(),'viskiji_po_regijah/skotski_viskiji_lowland.csv')

with open ('viskiji_po_regijah/skotski_viskiji_lowland.json', 'w') as f:
    json.dump (slovarji_viskijev_lowland, f, indent = 2, ensure_ascii = True)

## SPEYSIDE

stevilo_strani_speyside = 19
count_speyside = 0
slovarji_viskijev_speyside = []

for start in range(1, stevilo_strani_speyside + 1):
    url = f'https://www.thewhiskyexchange.com/c/314/speyside-single-malt-scotch-whisky?filter=true&rfdata=&pg={start}#productlist-filter'
    
    prvi_pobran = 1 + count_speyside * stevilo_viskijev_na_stran
    zadnji_pobran = (count_speyside + 1) * stevilo_viskijev_na_stran
    datoteka = f'Skotski_viskiji_speyside/{prvi_pobran}-{zadnji_pobran}.html'
    count_speyside +=1

    orodja.shrani_spletno_stran(url, datoteka)

    vsebina = orodja.vsebina_datoteke(datoteka) 
    viskiji = page_to_viskiji(vsebina)
    for viski in viskiji:
        slovarji_viskijev_speyside.append(get_dict_from_block(viski))

print(len(slovarji_viskijev_speyside))

orodja.zapisi_csv(slovarji_viskijev_speyside, slovarji_viskijev_speyside[0].keys(),'viskiji_po_regijah/skotski_viskiji_speyside.csv')

with open ('viskiji_po_regijah/skotski_viskiji_speyside.json', 'w') as f:
    json.dump (slovarji_viskijev_speyside, f, indent = 2, ensure_ascii = True)

## STANDARDNI VISKIJI


stevilo_strani_standard = 19
count_standard = 0
slovarji_viskijev_standard = []

for start in range(1, stevilo_strani_standard + 1):
    url = f'https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?status=no&pg={start}#productlist-filter'
    
    prvi_pobran = 1 + count_standard * stevilo_viskijev_na_stran
    zadnji_pobran = (count_standard + 1) * stevilo_viskijev_na_stran
    datoteka = f'Skotski_viskiji_standard/{prvi_pobran}-{zadnji_pobran}.html'
    count_standard +=1

    orodja.shrani_spletno_stran(url, datoteka)

    vsebina = orodja.vsebina_datoteke(datoteka) 
    viskiji = page_to_viskiji(vsebina)
    for viski in viskiji:
        slovarji_viskijev_standard.append(get_dict_from_block(viski))

print(len(slovarji_viskijev_standard))

orodja.zapisi_csv(slovarji_viskijev_standard, slovarji_viskijev_standard[0].keys(),'viskiji_standardni_ali_stari/skotski_viskiji_standard.csv')

with open ('viskiji_standardni_ali_stari/skotski_viskiji_standard.json', 'w') as f:
    json.dump (slovarji_viskijev_standard, f, indent = 2, ensure_ascii = True)


## STARI IN POSEBNI## to samo pomeni da imajo "status"

stevilo_strani_old_and_rare = 27
count_old_and_rare = 0
slovarji_viskijev_old_and_rare = []

for start in range(1, stevilo_strani_old_and_rare + 1):
    url = f'https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?pg={start}&status=yes#productlist-filter'
    
    prvi_pobran = 1 + count_old_and_rare * stevilo_viskijev_na_stran
    zadnji_pobran = (count_old_and_rare + 1) * stevilo_viskijev_na_stran
    datoteka = f'Skotski_viskiji_old_and_rare/{prvi_pobran}-{zadnji_pobran}.html'
    count_old_and_rare +=1

    orodja.shrani_spletno_stran(url, datoteka)

    vsebina = orodja.vsebina_datoteke(datoteka) 
    viskiji = page_to_viskiji(vsebina)
    for viski in viskiji:
        slovarji_viskijev_old_and_rare.append(get_dict_from_block(viski))

print(len(slovarji_viskijev_old_and_rare))

orodja.zapisi_csv(slovarji_viskijev_old_and_rare, slovarji_viskijev_old_and_rare[0].keys(),'viskiji_standardni_ali_stari/skotski_viskiji_old_and_rare.csv')

with open ('viskiji_standardni_ali_stari/skotski_viskiji_old_and_rare.json', 'w') as f:
    json.dump (slovarji_viskijev_old_and_rare, f, indent = 2, ensure_ascii = True)

