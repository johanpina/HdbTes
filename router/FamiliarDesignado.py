import sys
sys.path.append("..")
from fastapi import APIRouter
from utils.dbAlchemy import session
from typing import List
from schema.FamiliarDesignado import FamiliarDesignadoSchema
from models.model import FamiliarDesignadoModel

familiarDesignado = APIRouter()


@familiarDesignado.get("/all/", response_model=List[FamiliarDesignadoSchema])
async def listar_familiaresdesignados():
    familiares = session.query(FamiliarDesignadoModel).all()
    return familiares
