import sys
sys.path.append("..")
import psycopg2

from fastapi import APIRouter, HTTPException
from schema.PersonalACargo import PersonalACargoSchema, PersonalACargoBase
from schema.Usuario import UsuarioSchema
from utils.dbAlchemy import session
from models.model import PersonalACargoModel, PacienteModel, UsuarioModel, PersonalMedicoModel
from typing import List


personalAcargo = APIRouter()


@personalAcargo.get("/all/", response_model=List[PersonalACargoSchema])
def get_allPersonalAcargo():
    PersonalesACargo = session.query(PersonalACargoModel).all()
    return PersonalesACargo


@personalAcargo.post("/", response_model=PersonalACargoSchema)
def create_PersonalAcargo(personalAcargo: PersonalACargoBase):
    db_personalacargo = PersonalACargoModel(**personalAcargo.dict())
    session.add(db_personalacargo)
    session.commit()
    session.refresh(db_personalacargo)
    return db_personalacargo


@personalAcargo.put("/", response_model=PersonalACargoSchema)
def update_PersonalAcargo(personalAcargo: PersonalACargoSchema):
    personalac = session.query(PersonalACargoModel).filter_by(id = personalAcargo.id).first()

    if personalac:

        personalac.medico_id = personalAcargo.medico_id
        personalac.paciente_id = personalAcargo.paciente_id
        personalac.paciente_activo = personalAcargo.paciente_activo

        session.commit()
        print("Registro Actualizado exitosamente")
    
    else:
        raise HTTPException(status_code=404, detail="Personal A cargo no encontrado")
    
    return personalac

@personalAcargo.delete("/")
def delete_personalAcargo(idregistro: int):
    personal = session.query(PersonalACargoModel).filter(PersonalACargoModel.id == idregistro).first()

    if personal:
        session.delete(personal)
        session.commit()
        return {"mensaje": "Signo Vital Eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Personal a Cargo no encontrado")

@personalAcargo.get("/pacientes", response_model=List[UsuarioSchema])
def get_allPersonalAcargo(idmedico: int):
    PersonalesACargo = session.query(PersonalACargoModel, PacienteModel, UsuarioModel, PersonalMedicoModel).join(PacienteModel, PersonalACargoModel.paciente_id== PacienteModel.id).join(UsuarioModel, PacienteModel.usuario_id == UsuarioModel.id).join(PersonalMedicoModel, PersonalMedicoModel.id == PersonalACargoModel.medico_id).filter(PersonalMedicoModel.usuario_id == idmedico).all()
    resultado_json = []
    for item in PersonalesACargo:
        tabla_data = item[2].__dict__
        resultado_json.append({
            key: value for key, value in tabla_data.items() if not key.startswith('_')
        })

    print(resultado_json)
    # Retornar los resultados en formato JSON
    return resultado_json