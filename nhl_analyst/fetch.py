import requests

id_kucherov = 8476453
api_url = f'https://api-web.nhle.com/v1/player/{id_kucherov}/landing'

print(api_url)

def fetch_data():

    response = requests.get(api_url)

    with open("kucherov.json", "w") as file:
        file.write(response.text)

if __name__ == '__main__':
    fetch_data()
