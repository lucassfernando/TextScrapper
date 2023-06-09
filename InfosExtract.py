import requests
from random import randint
from bs4 import BeautifulSoup



def get_info(url, headers):

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        
        print(f"{url} | 200")
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        infos = str(soup.find("div", {"class": "show-container"}))
        lines = infos[132:].split('\n')

        with open(f'CARD {randint(0, 10000)}.txt', 'a') as file:

            for line in lines:

                if 'Name' in line:
                    file.writelines(line+"\n")
                elif 'Address' in line:
                    file.writelines(line+"\n")
                elif 'IP' in line:
                    file.writelines(line+"\n")
                elif 'SSN' in line:
                    file.writelines(line+"\n")
                elif 'Phone' in line:
                    file.writelines(line+"\n")
                elif 'Email' in line:
                    file.writelines(line+"\n")
                elif 'CC' in line:
                    file.writelines(line+"\n")
                elif 'Works' in line:
                    file.writelines(line+"\n")
                elif 'email' in line:
                    file.writelines(line+"\n")
                else:
                    pass

        return url

        

        

