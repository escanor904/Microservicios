import jwt
import time

secreto = "12345"
ts = int(time.time())
id = input("digita un ID  ")
nombre = input("Digita el nombre  ")



token = jwt.encode(
    {'id':id,'nombre':nombre,'time':ts},
    secreto,
    algorithm='HS256'
    
    
)

resultado = ""
print("-----------token------------")
print(token)


