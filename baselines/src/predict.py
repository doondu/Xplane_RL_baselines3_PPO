import gymnasium as gym
import numpy as np
import xpc as xp
from modelMake import XplaneEnv
from time import sleep
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
import csv

model = PPO.load("models/PPO/2")
env = XplaneEnv(clientAddr='0.0.0.0', xpHost='127.0.0.1', xpPort=49009, clientPort=1, timeout=3000, max_episode_steps=2000, test=False)

n_steps = 2048
env.setting(12345)
obs = env.reset()
obs = obs[0]
for step in range(n_steps):
    print(f"Step {step + 1}")
    action, _states = model.predict(obs)
    obs, rewards, dones, trunc, info = env.step(action)

    print(info)
    # print("obs=", obs, "reward=", rewards)