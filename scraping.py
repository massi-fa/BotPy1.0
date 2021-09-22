import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime

def scraping():

    # url dal quale estrapolare i dati
    url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

    # chiamata in GET della pagina web
    r = requests.get(url)

    # parsing del contenuto in formato più leggibile
    soup = bs(r.content, 'html.parser')

    # get della lista di tutti i prodotti nella pagina
    product_list = soup.find_all("div", class_="thumbnail")

    #istanziamento della variabile che conterrà i dati
    result = {
        "title": [],
        "description": [],
        "price": []
    }

    # per ogni prodotto trovato vado a prendermi le proprietà
    # che mi servono e le inserisco nella apposita lista
    # del dizionario creato prima
    count = 0
    for product in product_list:
        title = product.find(class_="title").text
        description =  product.find(class_="description").text
        price =  product.find(class_="price").text

        result["title"].append(title)
        result["description"].append(description)
        result["price"].append(price)
        count += count

    # parsing del dizionario in un dataframe
    data_frame = pd.DataFrame(data=result)

    # stampa del data frame a video
    print(data_frame)

    # salvataggio del dataframe in un file
    file = open("results.txt", "a+")
    file_content = datetime.datetime.now().isoformat() + "\n\n"
    file_content += data_frame.to_string()
    file_content += "\n********************************** \n\n\n"
    file.write(file_content)