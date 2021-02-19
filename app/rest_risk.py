from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from detect import assess_risk


class Passenger(BaseModel):
    name: Optional[str] = None
    Pclass: int = Field(title="Ticket class: 1, 2 or 3")
    Sex: bool = Field(title="Male: 0 (False), Female: 1 (True)")
    Age: int
    SibSp: int = Field(title="# of siblings / spouses aboard the Titanic")
    Parch: int = Field(title="# of parents / children aboard the Titanic")
    Fare: float = Field(title="Passenger fare")
    Cabin: Optional[str] = None
    Embarked: Optional[str] = None


tags_metadata = [
    {
        "name": "post",
        "description": "Add passenger. See schema for required values.",
    },
    {
        "name": "get",
        "description": "Get a list of passengers added.",
    },
    {
        "name": "get_risk",
        "description": "Get the risk scale for the last added person.",
    },
    {
        "name": "get_risks",
        "description": "Basically the same as get persons, but with risk associated with each checked passenger.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

passengers = []
passengers_risks = []


@app.post("/passenger", tags=["post"])
async def create_passenger(passenger: Passenger):
    passenger = passenger.dict()
    passengers.append(passenger)
    return passenger


@app.get("/passengers", tags=["get"])
async def get_passengers():
    return passengers


@app.get("/passenger/risk", tags=["get_risk"])
async def get_risk():
    singular_passenger = passengers[-1]
    pclass = singular_passenger.get('Pclass')
    sex = singular_passenger.get('Sex')
    age = singular_passenger.get("Age")
    sibsp = singular_passenger.get("SibSp")
    parch = singular_passenger.get("Parch")
    fare = singular_passenger.get("Fare")
    survival = assess_risk(pclass, sex, age, sibsp, parch, fare)
    risk = 1 - survival
    risk = round(risk, 4)
    risk_passenger = singular_passenger
    risk_passenger["risk"] = risk
    passengers_risks.append(risk_passenger)
    return risk


@app.get("/passengers/risk", tags=["get_risks"])
async def get_risks():
    return passengers_risks
