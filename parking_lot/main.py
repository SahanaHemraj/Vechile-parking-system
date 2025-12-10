from fastapi import FastAPI, HTTPException
from parking_lot.models.parking_lot_core import ParkingLot
from pydantic import BaseModel

app = FastAPI()
lot = ParkingLot(10)  # or read config/env

class ParkReq(BaseModel):
    plate: str
    size: str

@app.post("/park")
def park(req: ParkReq):
    res = lot.park_vehicle(req.plate, req.size)
    if res == -2:
        raise HTTPException(status_code=400, detail="Duplicate vehicle")
    if res == -1:
        raise HTTPException(status_code=409, detail="No suitable slot")
    return {"slot": res}

@app.post("/leave/{slot_id}")
def leave(slot_id: int):
    ok = lot.leave_slot(slot_id)
    if not ok:
        raise HTTPException(status_code=400, detail="Invalid slot or already free")
    return {"status": "freed"}

@app.get("/status")
def status():
    return {"status_table": lot.status()}

@app.get("/summary")
def summary():
    small, large, oversize = lot.summary_counts()
    return {"small": small, "large": large, "oversize": oversize}
