import requests


def obter_dados_meteorologicos():    
        url = "http://127.0.0.1:8000/v1/forecast"   
        parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713,
        }

  
        resposta = requests.get(url, params=parametros,timeout=15)    
        resposta.raise_for_status()    
        dados = resposta.json()   
        condicoes_atuais = dados["current"]    
        temperatura = condicoes_atuais["temperature_2m"]    
        umidade = condicoes_atuais["relative_humidity_2m"]    
        sensacao_termica = condicoes_atuais["apparent_temperature"]    
        precipitacao = condicoes_atuais["precipitation"]    
        vento = condicoes_atuais["wind_speed_10m"]
        horario = condicoes_atuais["time"] 

        print(dados)
        return {    
                "temperatura": temperatura,    
                "umidade_relativa": umidade,    
                "sensacao_termica": sensacao_termica,    
                "precipitacao": precipitacao,    
                "velocidade_vento": vento,    
                "horario": horario}



obter_dados_meteorologicos()