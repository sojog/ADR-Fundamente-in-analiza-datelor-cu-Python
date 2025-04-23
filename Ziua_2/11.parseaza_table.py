import pandas as pd
from bs4 import BeautifulSoup
import os

# Creăm directorul pentru rezultate dacă nu există
output_dir = 'rezultate'
os.makedirs(output_dir, exist_ok=True)

# Citim fișierul HTML
with open('Ziua_2/tabel.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parsăm HTML-ul
soup = BeautifulSoup(html_content, 'html.parser')

# Găsim tabelul
tabel = soup.find('table')

# Extragem toate rândurile din tabel (excepție header-ul)
randuri = tabel.find_all('tr')[1:]  # Prima linie e header-ul

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

# Salvăm în CSV
output_file = os.path.join(output_dir, 'situri_arheologice.csv')
df.to_csv(output_file, index=False, encoding='utf-8')

print(f'Datele au fost salvate cu succes în fișierul: {output_file}')
print(f'Au fost extrase {len(date)} înregistrări.')
