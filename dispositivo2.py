import paho.mqtt.client as mqtt 
import time
from hal import temperaturaDips2, aquecedor
from definitions2 import user, password, server, port, client_id

def mensagem (client, userdata, msg):
    vetor = msg.payload.decode().split(',') 
    aquecedor ('on' if vetor [1] == '1' else 'off') 
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor [0]}') 
    


#Conexão inicial
client = mqtt.Client(client_id)
client.username_pw_set(user, password)  
client.connect(server, port)


client.on_message = mensagem 
client.subscribe (f'v1/{user}/things/{client_id}/cmd/1') 
client.loop_start() 


#Comportamento do sistema 
while True:
    client.publish('v1/'+user+'/things/'+client_id+'/data/0', temperaturaDips2()) #mandando a mensagem de temperatura 
    time.sleep (10)
