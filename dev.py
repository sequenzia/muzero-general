from muzero import MuZero

GAME_NAME = "breakout"

muzero = MuZero(GAME_NAME)

env = muzero.Game()
env.reset()
env.render()

done = False
while not done:
    action = env.human_to_action()
    observation, reward, done = env.step(action)
    print(f"\nAction: {env.action_to_string(action)}\nReward: {reward}")
    env.render()