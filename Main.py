import requests
from time import sleep
from bs4 import BeautifulSoup
from InfosExtract import get_info

url_base = 'https://doxbin.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Cookie": "__ddg1_=HBaDYHTwDj8JtiDQuu6L; vDDoS=672567fbefd293529e5ca870e2c2b570; XSRF-TOKEN=eyJpdiI6IkN5M3VXV1c3dUNjTHJUdmlqOWdiZHc9PSIsInZhbHVlIjoiMVU2UE83cm1sRisxUHFQNzErMm93Z3p3OXdZbU9mdkhranIrUzU0bkFMcHdVUnVUTnRPSWVTUUlPblc4N3YzMiIsIm1hYyI6IjVkMDFmM2ZiNmRlYzQzMTk1NWQwYmIxN2VhMDQ3NmIzODUzNThiNmUzM2FiYmNkMjUwNDhkY2Y3NjQ3ZjEyMTAifQ%3D%3D; doxbin_session=eyJpdiI6IkpPMlBDcFRVeVA3aWRYXC83RVNPWlhnPT0iLCJ2YWx1ZSI6IjZzK2lNbnJ0UjBwb2g3NHByZTJNVjc5OTBDTG5GMDRGSzUramU0R290U1hSMUdPWklwa1wvS3BvalN1MXdOVERjIiwibWFjIjoiYjU5YWE4MjFiZjZkN2Y1YWMzNjhhNTg0YjdlYmI4NDk1OWNjYTgwMTU2MmYyZjc0MjYwZDUyMzY4OThhYTBkOCJ9"
}

list_url = []
list_url_ok = []
def get_links():

    response = requests.get(url_base, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    for link in soup.find_all('a'):

        if 'C2' in str(link.get('href')):
            if str(link.get('href')) not in list_url:
            
                list_url.append(str(link.get('href')))
                print(f"ADD: {str(link.get('href'))}")


while True:

    get_links()

    if __name__ == '__main__':

        for url in list_url:
            if url not in list_url_ok:
                
                url_ok = get_info(url, headers=headers)
                list_url_ok.append(url_ok)
    
    print("REINICIANDO EM 15 SEGUNDOS")
    sleep(15)
    
        
        