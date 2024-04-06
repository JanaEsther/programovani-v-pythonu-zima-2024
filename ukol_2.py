import requests
import json

ico= input("Zadejte IČ subkjektu, který Vás zajímá:\n")
headers = {
    'accept': 'application/json',
}

response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")

if response.text and response.status_code == 200:
    data = response.json()
    

obchodniJmeno = data.get('obchodniJmeno')
textovaAdresa = data.get('sidlo', {}).get('textovaAdresa')

print( f"{obchodniJmeno} \n{textovaAdresa}")

def find_legal_form(code, items):
    for item in items:
        if item['kod'] == code:
            return item['nazev']
    return None

# Získání číselníku právních forem

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat", headers=headers, data=data)
ciselnik = res.json()['ciselniky'][0]['polozkyCiselniku']

# Získání názvu subjektu od uživatele
nazev_subjektu = input("Zadejte název subjektu, který chcete vyhledat: ")

# Vyhledání subjektů
data = json.dumps({"obchodniJmeno": nazev_subjektu})
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
subjekty = res.json()

# Výpis nalezených subjektů
print(f"Nalezeno subjektů: {subjekty['pocetCelkem']}")
for subjekt in subjekty['ekonomickeSubjekty']:
    pravni_forma = find_legal_form(subjekt['pravniForma'], ciselnik)
    print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}, {pravni_forma}")























