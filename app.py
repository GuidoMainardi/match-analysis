import os
from fastapi import FastAPI
from src.MatchAnalysis.pipeline.prediction import PredictionPipeline

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Match analysis API"}


@app.post("/train")
async def train():
    os.system('dvc repro')
    return {"message": "Training done successfully"}


@app.get("/predict")
async def predict(
    blueGold: int, blueMinionsKilled: int,
    blueJungleMinionsKilled: int, blueAvgLevel: float,
    redGold: int, redMinionsKilled: int,
    redJungleMinionsKilled: int, redAvgLevel: float,
    blueChampKills: int, blueHeraldKills: int,
    blueDragonKills: int, blueTowersDestroyed: int,
    redChampKills: int, redHeraldKills: int,
    redDragonKills: int, redTowersDestroyed: int
):
    sample = dict(
        blueGold=blueGold, blueMinionsKilled=blueMinionsKilled,
        blueJungleMinionsKilled=blueJungleMinionsKilled, blueAvgLevel=blueAvgLevel,
        redGold=redGold, redMinionsKilled=redMinionsKilled,
        redJungleMinionsKilled=redJungleMinionsKilled, redAvgLevel=redAvgLevel,
        blueChampKills=blueChampKills, blueHeraldKills=blueHeraldKills,
        blueDragonKills=blueDragonKills, blueTowersDestroyed=blueTowersDestroyed,
        redChampKills=redChampKills, redHeraldKills=redHeraldKills,
        redDragonKills=redDragonKills, redTowersDestroyed=redTowersDestroyed
    )
    return PredictionPipeline.predict(sample)

