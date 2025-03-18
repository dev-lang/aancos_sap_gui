import requests
from bs4 import BeautifulSoup
import csv

def extract_links(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    dropbox_links = []
    for a_tag in soup.find_all('a', href=True):
        if 'dropbox.com' in a_tag['href']:
            text = a_tag.get_text(strip=True)
            dropbox_links.append((text, a_tag['href']))

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Descripción", "Enlace"])
        writer.writerows(dropbox_links)

    print(f"Se encontraron {len(dropbox_links)} enlaces de Dropbox en {filename}.")

# URLs de las páginas
urls = {
    "SAP_GUI_750": "https://aancos.com/2017/05/12/sap-gui-for-windows-7-50/",
    "SAP_GUI_760": "https://aancos.com/2019/03/04/sap-gui-for-windows-7-60/",
    "SAP_GUI_770": "https://aancos.com/2021/02/01/sap-gui-for-windows-7-70/",
    "SAP_GUI_800": "https://aancos.com/2023/02/08/sap-gui-for-windows-8-00/"
}

# Extraer enlaces para cada versión
for version, url in urls.items():
    extract_links(url, f"enlaces_{version}.csv")
