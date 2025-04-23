import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from urllib.parse import urljoin

# URL-ul inițial
URL = "https://ran.cimec.ro/sel.asp?lpag=10&Lang=RO&layers=&crsl=2&csel=2&clst=1&campsel=cat&nr=2"
BASE_URL = "https://ran.cimec.ro/"




for i in range(1, 2724):
    URL = f"https://ran.cimec.ro/sel.asp?lpag={i}&Lang=RO&layers=&crsl=2&csel=2&clst=1&campsel=cat&nr={i}"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    tabel = soup.find('table', class_='table-striped')
    # print(tabel)
    # Extragem toate rândurile din tabel (excepție header-ul)
    randuri = tabel.find_all('tr')[1:]  # Prima linie e header-ul
    print(randuri)
    # Lista pentru a stoca datele
    date = []

    # Parcurgem fiecare rând
    for rand in randuri:
        # Extragem toate celulele din rând
        celule = rand.find_all('td')
        
        # Verificăm dacă există suficiente celule (tabelul nostru are 10 coloane)
        if len(celule) >= 10:
            # Extragem codul RAN (sunt și linkuri în celulă)
            cod_ran = celule[0].text.strip()
            if '\n' in cod_ran:
                cod_ran = cod_ran.split('\n')[0].strip()
            
            # Extragem restul datelor
            denumire = celule[1].text.strip()
            categorie = celule[2].text.strip()
            tip = celule[3].text.strip()
            judet = celule[4].text.strip()
            localitate = celule[5].text.strip()
            componente = celule[6].text.strip()
            cronologie = celule[7].text.strip()
            data_modificare = celule[8].text.strip()
            
            # Curățăm data modificare de text adițional
            if '(' in data_modificare:
                data_modificare = data_modificare.split('(')[0].strip()
            
            # Verificăm dacă există link către hartă
            are_harta = 'Da' if celule[9].find('a') else 'Nu'
            
            # Adăugăm datele în lista noastră
            date.append({
                'Cod RAN': cod_ran,
                'Denumire': denumire,
                'Categorie': categorie,
                'Tip': tip,
                'Judet': judet,
                'Localitate': localitate,
                'Componente': componente,
                'Cronologie': cronologie,
                'Data Modificare': data_modificare,
                'Are Harta': are_harta
            })

            # Cream un DataFrame pandas
            df = pd.DataFrame(date)

            output_dir = "rezultate"
            os.makedirs(output_dir, exist_ok=True)
            # Salvăm în CSV
            output_file = os.path.join(output_dir, f'situri_arheologice{i}.csv')
            df.to_csv(output_file, index=False, encoding='utf-8')

            print(f'Datele au fost salvate cu succes în fișierul: {output_file}')
            print(f'Au fost extrase {len(date)} înregistrări.')
            input()







# Creăm directorul pentru CSV dacă nu există
csv_dir = "date_extrase"
os.makedirs(csv_dir, exist_ok=True)
csv_file = os.path.join(csv_dir, "date_ran.csv")

# Verifică dacă fișierul există și determină pagina de la care să continue
current_page = 1
progress_file = os.path.join(csv_dir, "progres.txt")

if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        try:
            current_page = int(f.read().strip())
            print(f"Continuăm de la pagina {current_page}")
        except:
            current_page = 1

# Funcția pentru extragerea datelor din tabel
def extrage_date(soup):
    try:
        tabel = soup.find('table', class_='tab1')
        if not tabel:
            return []
            
        randuri = tabel.find_all('tr')[1:]  # Ignorăm antetul
        date_extrase = []
        
        for rand in randuri:
            coloane = rand.find_all('td')
            if len(coloane) >= 7:
                date_rand = {
                    'Cod': coloane[0].text.strip(),
                    'Nume': coloane[1].text.strip(),
                    'Categorie': coloane[2].text.strip(),
                    'Tip': coloane[3].text.strip(),
                    'Judet': coloane[4].text.strip(),
                    'Localitate': coloane[5].text.strip(),
                    'Punct': coloane[6].text.strip()
                }
                date_extrase.append(date_rand)
                
        return date_extrase
    except Exception as e:
        print(f"Eroare la extragerea datelor: {e}")
        return []

# Funcția pentru a găsi link-ul către pagina următoare
def gaseste_pagina_urmatoare(soup, pagina_curenta):
    try:
        # Căutăm în paginație link-ul către pagina următoare
        paginatie = soup.find('div', class_='paginatie')
        if not paginatie:
            return None
            
        link_pagina_urmatoare = None
        linkuri = paginatie.find_all('a')
        
        # Căutăm link care conține "pagina următoare" sau numărul paginii curente + 1
        for link in linkuri:
            if link.text.strip() == str(pagina_curenta + 1):
                link_pagina_urmatoare = link.get('href')
                break
                
        if link_pagina_urmatoare:
            return urljoin(BASE_URL, link_pagina_urmatoare)
        return None
    except Exception as e:
        print(f"Eroare la găsirea paginii următoare: {e}")
        return None

# Procesăm toate paginile
date_totale = []
pagina_curenta = current_page
url_curent = URL

# Modificăm URL-ul inițial dacă începem de la o pagină diferită de 1
if pagina_curenta > 1:
    # Încercăm să construim URL-ul pentru pagina de start
    url_curent = URL.replace("lpag=10", f"lpag={pagina_curenta * 10}")

# Numărul total de pagini
total_pagini = 10 #2724

while pagina_curenta <= total_pagini:
    print(f"Procesăm pagina {pagina_curenta} din {total_pagini}")
    
    # Facem cererea HTTP cu încercări multiple în caz de eșec
    incercari = 0
    max_incercari = 5
    succes = False
    
    while incercari < max_incercari and not succes:
        try:
            response = requests.get(url_curent, timeout=30)
            response.raise_for_status()  # Verificăm dacă cererea a avut succes
            succes = True
        except Exception as e:
            incercari += 1
            print(f"Încercarea {incercari} eșuată: {e}")
            if incercari < max_incercari:
                time.sleep(5)  # Așteptăm 5 secunde înainte de a reîncerca
            else:
                print(f"Nu s-a putut accesa pagina {pagina_curenta} după {max_incercari} încercări")
                # Salvăm progresul și ieșim
                with open(progress_file, "w") as f:
                    f.write(str(pagina_curenta))
                break
    
    if not succes:
        break
    
    # Parsăm conținutul HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extragem datele
    date_pagina = extrage_date(soup)
    if date_pagina:
        date_totale.extend(date_pagina)
        
        # Salvăm datele după fiecare pagină pentru a nu pierde progresul
        df = pd.DataFrame(date_totale)
        df.to_csv(csv_file, index=False)
        
        # Salvăm numărul paginii curente
        with open(progress_file, "w") as f:
            f.write(str(pagina_curenta))
    
    # Găsim link-ul către pagina următoare
    url_urmator = gaseste_pagina_urmatoare(soup, pagina_curenta)
    if not url_urmator:
        # Dacă nu găsim link-ul direct, încercăm să construim URL-ul pentru pagina următoare
        url_urmator = URL.replace("lpag=10", f"lpag={(pagina_curenta + 1) * 10}")
    
    # Trecem la pagina următoare
    pagina_curenta += 1
    url_curent = url_urmator
    
    # Introducem o pauză pentru a nu supraîncărca serverul
    time.sleep(2)

print(f"Procesare finalizată. Date salvate în {csv_file}")
print(f"Au fost procesate {pagina_curenta - 1} pagini din {total_pagini}")