from pydantic import BaseModel
from fastapi import FastAPI
from datetime import datetime
app = FastAPI()

class Item(BaseModel):
    id: int
    ipServidor: str
    infoProcess: str
    processRun: str
    sessionUser: str
    nameServer: str
    systemOper: str
    
@app.post("/meli")
def challenge(Item: Item):
#   return {"id":Item}

    file = open("./info/"+Item.ipServidor + " " + datetime.today().strftime('%Y-%m-%d') +".txt", "a")
    file.write("id: "+str(Item.id)+"\n")
    file.write("IP del servidor: "+Item.ipServidor+"\n")
    file.write("Nombre del servidor: "+Item.nameServer +"\n")
    file.write("Sistema Operativo: "+Item.systemOper+"\n")
    file.write("Informacion Procesador:"+"\n"+Item.infoProcess+"\n")
    file.write("Informacion Procesos ejecutandose:"+"\n"+Item.processRun+"\n")
    file.write("Informacion usuarios activos:"+"\n"+Item.sessionUser+"\n")
    file.write("__________________________________________________ _________________________\n")
    file.close()
    return "Información del servidor guardada correctamente"