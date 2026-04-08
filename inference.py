from env import TheftEnv
from fastapi import FastAPI

app = FastAPI()

@app.post("/reset")
def api_reset():
    return reset()

@app.post("/step")
def api_step(action: int):
    return step(action)
env = TheftEnv()

def reset():
    state = env.reset()
    return {
        "state": list(state)
    }

def step(action):
    next_state, reward, done = env.step(action)
    return {
        "state": list(next_state),
        "reward": reward,
        "done": done
    }
