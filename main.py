from pydantic import BaseModel
from fastapi import FastAPI
import os
from datetime import datetime
app = FastAPI()

@app.get("/meli")
def challenge():
  return {"Hello world!"}

class Item(BaseModel):
    id: int
    ipServidor: str
    infoProcess: str
    processRun: str
    sessionUser: str
    nameServer: str
    systemOper: str
    
@app.post("/meli")
def challenge2(Item: Item):
#   return {"id":Item}

    file = open("./info/"+Item.ipServidor + " "+ datetime.today().strftime('%Y-%m-%d') +".txt", "a")
    file.write("id: "+str(Item.id)+"\n")
    file.write("IP del servidor: "+Item.ipServidor+"\n")
    file.write("Nombre del servidor: "+Item.nameServer +"\n")
    file.write("Nombre del servidor: "+Item.systemOper+"\n")
    file.write("Información Procesador:"+"\n"+Item.infoProcess+"\n")
    file.write("Información Procesos ejecutandose:"+"\n"+Item.processRun+"\n")
    file.write("Información usuarios activos:"+"\n"+Item.sessionUser+"\n")
    file.write("__________________________________________________ _________________________\n")
    file.close()
    return "Información del servidor guardada correctamente"