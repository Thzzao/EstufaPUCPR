from ast import Str
import paho.mqtt.client as mqtt 
import time
from hal import temperaturaDips1, temperaturaDips2, aquecedor, controleTemp
from definitionsButton import user, password, server, port, client_id

def mensagem (client, userdata, msg):
    vetor = msg.payload.decode().split(',') 
    controleTemp ('on' if vetor [1] == '1' else 'off') 
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor [0]}') 
    


#Conexão inicial
client = mqtt.Client(client_id)
client.username_pw_set(user, password)  
client.connect(server, port)


client.on_message = mensagem 
client.subscribe (f'v1/{user}/things/{client_id}/cmd/0') 
client.loop_start() 


#Comportamento do sistema 
while True:

    if controleTemp(str) == 'on':

        if temperaturaDips1() < 29:
            client.publish('v1/025fbe60-3ac9-11ed-baf6-35fab7fd0ac8/things/653f2cf0-3ac9-11ed-baf6-35fab7fd0ac8/data/0', aquecedor(str) == 'on')
          
        elif temperaturaDips1() > 31:
            client.publish('v1/025fbe60-3ac9-11ed-baf6-35fab7fd0ac8/things/653f2cf0-3ac9-11ed-baf6-35fab7fd0ac8/data/0', aquecedor(str) == 'off')
           
        if temperaturaDips2() < 29:
            client.publish('v1/025fbe60-3ac9-11ed-baf6-35fab7fd0ac8/things/861383d0-3ade-11ed-bf0a-bb4ba43bd3f6/data/0', aquecedor(str) == 'on')
            
        elif temperaturaDips2() > 31:
            client.publish('v1/025fbe60-3ac9-11ed-baf6-35fab7fd0ac8/things/861383d0-3ade-11ed-bf0a-bb4ba43bd3f6/data/0', aquecedor(str) == 'off')
           
    time.sleep(10)
        

  
           


