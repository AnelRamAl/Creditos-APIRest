from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user:User):
    # code #
    if user.INGRESOS_MENSUALES > 25000:
        x = "Aprobado"
    if user.INGRESOS_MENSUALES < 15000:
        x = "No aprobado"   
    if (user.INGRESOS_MENSUALES >= 15000) and (user.INGRESOS_MENSUALES <= 25000) and (user.DEPENDIENTES < 3):
        x = "Aprobado"
    else: 
        x = "No aprobado" 
    # # code #
    new_user = {"PRIMER_NOMBRE": user.PRIMER_NOMBRE, 
                "APELLIDO_PAT": user.APELLIDO_PAT,
                "APELLIDO_MAT": user.APELLIDO_MAT,
                "FECHA_NAC": user.FECHA_NAC,
                "RFC": (user.APELLIDO_PAT[:2]).upper()+ user.APELLIDO_MAT[:1]+user.PRIMER_NOMBRE[:1]+user.FECHA_NAC[2:4]+user.FECHA_NAC[5:7]+user.FECHA_NAC[8:10],
                "INGRESOS_MENSUALES": user.INGRESOS_MENSUALES,
                "DEPENDIENTES": user.DEPENDIENTES,
                "APROBADO": x
                }
    
    result = conn.execute(users.insert().values(new_user))
    
    return conn.execute(f"SELECT ID,RFC,APROBADO FROM users where ID = {result.lastrowid}").first()

@user.get("/users")
def helloworld():
    return "hello world 11112"

@user.get("/users")
def helloworld():
    return "hello world 11112"