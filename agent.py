import random

class QAgent:
    def __init__(self):
        self.q_table = {}
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 2)
        else:
            q_values = [self.get_q(state, a) for a in range(3)]
            return q_values.index(max(q_values))

    def update(self, state, action, reward, next_state):
        old_q = self.get_q(state, action)
        future_q = max([self.get_q(next_state, a) for a in range(3)])

        new_q = old_q + self.alpha * (reward + self.gamma * future_q - old_q)
        self.q_table[(state, action)] = new_q