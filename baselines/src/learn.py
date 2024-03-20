import gymnasium as gym
from modelMake import XplaneEnv
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise
from stable_baselines3.common.env_checker import check_env

models_dir = "models/PPO"

env = XplaneEnv(clientAddr='0.0.0.0', xpHost='127.0.0.1', xpPort=49009, clientPort=1, timeout=3000, max_episode_steps=2000, test=False)
# initial setting for xplane environment
env.reset()

# n_actions = env.action_space.shape[-1]
# action_noise = NormalActionNoise(mean=np.zeros(n_actions), sigma=0.1 * np.ones(n_actions))

# model = PPO("MlpPolicy", env, verbose=1)
# model._last_obs = None
# model.learn(total_timesteps=10, log_interval=10, reset_num_timesteps=False)

# model.save("ppo_ex")

model = PPO("MlpPolicy", env, verbose=1)
# this is not using now
TIMESTEPS = 2048
iters = 0
for i in range(3):
    iters += 1
    env.setting(iters)
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS*i}")