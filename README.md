# RL-Based Theft Vehicle Monitoring System

## Problem
Detecting stolen vehicles efficiently under limited surveillance resources.

## Approach
We model this as a Reinforcement Learning problem where an agent decides:
- Ignore
- Track
- Alert

## State
- Suspicion score (0–10)
- Available tracking resources
- Tracking status

## Actions
- 0: Ignore
- 1: Track
- 2: Alert

## Reward Design
- +20 → Correct alert
- -10 → False alert
- -15 → Missed stolen vehicle
- +10 → Useful tracking
- Resource penalties included

## Key Idea
Tracking improves the quality of information (reduces uncertainty),
allowing better future decisions.

## Result
The agent learns to:
- Focus on high-risk vehicles
- Avoid unnecessary alerts
- Efficiently use limited resources

## How to Run
```bash
python train.py
## Results

The agent shows improvement over time:

- Initial episodes: low/negative rewards
- Later episodes: higher rewards

This indicates the agent learns better decision-making policies.
# sample results
First 20 episodes avg reward: -8.4
Last 20 episodes avg reward: 48.9