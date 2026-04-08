from env import TheftEnv
from agent import QAgent
import matplotlib.pyplot as plt


env = TheftEnv()
agent = QAgent()

episodes = 200
rewards = []

for ep in range(episodes):
    state = env.reset()
    total_reward = 0

    while True:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)

        agent.update(state, action, reward, next_state)

        state = next_state
        total_reward += reward

        if done:
            break

    rewards.append(total_reward)
    print(f"Episode {ep+1}: Total Reward = {total_reward}")
print("\n=== Performance Summary ===")
print(f"First 20 episodes avg reward: {sum(rewards[:20]) / 20}")
print(f"Last 20 episodes avg reward: {sum(rewards[-20:]) / 20}")
plt.plot(rewards)
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("Training Performance")
plt.show()