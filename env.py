import random

class TheftEnv:
    def __init__(self):
        self.max_steps = 50
        self.reset()

    def reset(self):
        self.step_count = 0
        self.resources = 5
        self.tracked = 0
        self.suspicion = random.randint(0, 10)
        return self._get_state()

    def _get_state(self):
        return (self.suspicion, self.resources, self.tracked)

    def step(self, action):
        self.step_count += 1

        # Probabilistic ground truth (better than pure random)
        if self.suspicion > 7:
            stolen = 1 if random.random() < 0.7 else 0
        else:
            stolen = 1 if random.random() < 0.2 else 0

        reward = 0

        if action == 0:  # Ignore
            if stolen:
                reward = -15
            else:
                reward = 2

        elif action == 1:  # Track
            if self.resources > 0:
                self.resources -= 1
                self.tracked = 1

                # Improve suspicion (tracking effect)
                if stolen:
                    self.suspicion = min(10, self.suspicion + random.randint(2, 3))
                    reward = 10
                else:
                    self.suspicion = max(0, self.suspicion - random.randint(2, 3))
                    reward = -2
            else:
                reward = -5

        elif action == 2:  # Alert
            if stolen:
                reward = 20
            else:
                reward = -10

        done = self.step_count >= self.max_steps

        # New incoming vehicle
        self.suspicion = random.randint(0, 10)
        self.tracked = 0

        return self._get_state(), reward, done