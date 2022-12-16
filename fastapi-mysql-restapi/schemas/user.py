from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    ID: Optional[str]
    PRIMER_NOMBRE: str
    APELLIDO_PAT: str
    APELLIDO_MAT: str
    FECHA_NAC: str
    RFC: Optional[str]
    INGRESOS_MENSUALES: int
    DEPENDIENTES: int
    APROBADO: Optional[str]