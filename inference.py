from fastapi import FastAPI
from pydantic import BaseModel
from env import TheftEnv

app = FastAPI()
env = TheftEnv()

# Input schema
class ActionInput(BaseModel):
    action: int

# Health check (important for HF)
@app.get("/")
def home():
    return {"status": "running"}

# Reset environment
@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "state": list(state)
    }

# Step function
@app.post("/step")
def step(input: ActionInput):
    next_state, reward, done = env.step(input.action)
    return {
        "state": list(next_state),
        "reward": float(reward),
        "done": bool(done)
    }
