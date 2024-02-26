import requests
import json #pip install jsonlib

def get_passagem(complete):
    try:  
        response = requests.get(complete, params="params")
        if response.status_code == 200:
            data = response.json()
            
            #print (data)
            print(data[0]['casos'])
            soma = 0

            for count in range(semana_ini-1, semana_fin, 1):
                
                print(count)
                #print(data[count]['casos'])
                soma += int(data[count]['casos'])
                
            print(soma)

            print(data[0]['notif_accum_year'])
    
    except: 
        print ("não foi possível fazer a consulta")


# geocode=3106200&disease=dengue&format=json&ew_start=1&ew_end=15&ey_start=2024&ey_end=2024

base = "https://info.dengue.mat.br/api/alertcity?"

geocode = 3304557
disease = 'dengue'
semana_ini = 1
semana_fin = 52
ano_ini = 2022
ano_fin = 2024

complete = (f'{base}geocode={geocode}&disease={disease}&format=json&ew_start={semana_ini}&ew_end={semana_fin}&ey_start={ano_ini}&ey_end={ano_fin}')

print(complete)
get_passagem(complete)
