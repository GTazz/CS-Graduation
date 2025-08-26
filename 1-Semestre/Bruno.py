import requests
import json
import time
from datetime import datetime

# === SETTINGS ===
url_power_bi = ""
token = ""

# === DADOS ===
ELEMENTS = ("organizations", "deals", "products")
DATA_INICIAL = "2024-01-01"
DATA_FINAL = "2024-01-31"

# LIMITE_MAXIMO = 7000

class Main():
    def __init__(self, debug=False, fake_data=False):

        # === COLETAR DADOS===
        self.all_data = self.get_data() if not debug else self.__get_data_simulation(fake_data)
        
        # === ENVIAR DADOS===
        self.post_data()

    def get_data(self) -> dict:
        
        result = {}
        for element in ELEMENTS:
            print(f"Getting {element}...")
            end_point = f"https://crm.rdstation.com/api/v1/{element}"
            end_point = f"{end_point}?token={token}"
            # end_point = f"{base_url}?token={token}&start_date={DATA_INICIAL}&end_date={DATA_FINAL}"
            
            res = requests.get(end_point)

            if res.status_code == 429:
                print(f"[{element}] Limite atingido. Aguardando 60 segundos...")
                time.sleep(60)
                continue

            if res.status_code != 200:
                print(f"[{element}] Erro ao buscar dados: {res.status_code}")
                break

            data = res.json()
            with open(f"log.{element}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"{element} succesfully acquired.\n")

            result[element] = data

        return result

    def __get_data_simulation(self, fake_data=False) -> dict:
        
        result = {}
        if not fake_data:
            for element in ELEMENTS:
                with open(f"log.{element}.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                result[element] = data

        else:
            for element in ELEMENTS:    
                pass

        return result

    def post_data(self):
        """
        Envia os dados coletados para o Power BI.
        """
        
        headers = {"Content-Type": "application/json"} #Bearer token
        try:
            response = requests.post(url_power_bi, headers=headers, data=json.dumps(self.all_data))
            if response.status_code == 200:
                print("Dados enviados com sucesso para o Power BI!")
            else:
                print(f"Erro ao enviar dados para o Power BI: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Erro ao tentar enviar dados: {e}")


if __name__ == "__main__":
    
    Main()
    # Main(debug=True)
    # Main(debug=True, fake_data=True)
