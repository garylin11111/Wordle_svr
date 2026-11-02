from fastapi import FastAPI
import random
import uuid

WORD_BANK = ["APPLE", "TRAIN", "HOUSE", "PLANT", "CLOUD"]
games_db = {}

app = FastAPI(title="Wordle API")

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/new-game")
def start_new_game():
    game_id = str(uuid.uuid4())
    target_word = random.choice(WORD_BANK)
    games_db[game_id] = {
    "target": target_word,
    "status": "PLAYING"
    }
    return {"game_id": game_id, "message": "New game started!"}