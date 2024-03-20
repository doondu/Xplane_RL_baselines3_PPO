import gymnasium as gym
import numpy as np
import xpc as xp
import math
import csv
from time import sleep, time
from scipy.stats import norm
from stable_baselines3 import TD3
from stable_baselines3.common.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise
from stable_baselines3.common.env_checker import check_env

# connect with xplane at xpc.py
class initial:

    def connect( clientAddr, xpHost, xpPort  , clientPort, timeout ,max_episode_steps):
            return xp.XPlaneConnect(clientAddr,xpHost,xpPort,clientPort,timeout ,max_episode_steps)

class XplaneEnv(gym.Env):
    def __init__(self,clientAddr, xpHost, xpPort  , clientPort, timeout, max_episode_steps,test=False):
        super(XplaneEnv, self).__init__()

        # aircraft's yaw range (change O)
        self.min_yaw = 0
        self.max_yaw = 360
        self.min_roll = -180
        self.max_roll = 180
        self.min_pitch = -180
        self.max_pitch = 180
        # action space and obs space.
        self.action_space = gym.spaces.Box(low=np.array([-1, -1, -1, -1]), high=np.array([1, 1, 1, 1]), shape=(4,), dtype=np.float32)
        self.observation_space = gym.spaces.Box(low=np.array([self.min_yaw, self.min_pitch, self.min_roll]), high=np.array([self.max_yaw, self.max_pitch, self.max_roll]), dtype=np.float32)
        
        # target heading
        self.target_yaw = 160
        self.target_pitch = 17
        self.target_roll = 2

        # get value of current heading (this is not use)
        self.current_heading = 0
        self.stepTime = 0
        # xpalne setting
        XplaneEnv.CLIENT = None
        try:
            XplaneEnv.CLIENT = initial.connect(clientAddr,xpHost,xpPort,clientPort,timeout ,max_episode_steps)
            print('I am client', XplaneEnv.CLIENT )
        except:
            print("connection error. Check your paramters")

        #log

    def setting(self, num):
        self.log = open(f"models/PPO/reward_ppo{num}.csv", 'w', newline='')
        self.log = csv.writer(self.log)
        a = ["reward"]
        self.log.writerow(a)
        self.stepTime = 0
        # initial setting for xplane environment
        try:
            state = []; 
            with open('initialData.csv', newline='') as file:
                posiFirst = list(map(float, file.readline().strip().split(',')))
                velocityFirst = list(map(float, file.readline().strip().split(','))) #vx, vy, vz
                rateFirst = list(map(float, file.readline().strip().split(','))) #Roll rate(P), Pitch rate(Q), Yaw rate(R)
        
            XplaneEnv.CLIENT.sendPOSI(posiFirst)
            XplaneEnv.CLIENT.sendDREFs(["sim/flightmodel/position/local_vx","sim/flightmodel/position/local_vy","sim/flightmodel/position/local_vz"], velocityFirst)
            XplaneEnv.CLIENT.sendDREFs(["sim/flightmodel/position/P", "sim/flightmodel/position/Q", "sim/flightmodel/position/R"], rateFirst)
            print("SEND ALL")
        except Exception as e:
            print(e)
            print("Send error in initial setting.")
        
        # state = list(XplaneEnv.CLIENT.getPOSI());
        # self.current_heading = state[5]

    def step(self, action):
        self.stepTime += 1
        print(self.stepTime)
        print(action)
        # send model's prediction action. pa is previous action
        pa = [0.0,0.0,0.0,0.0,1,0.0,0.0]
        pa[0], pa[1], pa[2], pa[3]= action[0], action[1], action[2], action[3]
        new_action = pa
        print(new_action)
        XplaneEnv.CLIENT.sendCTRL(new_action)

        sleep(0.1)

        # get state
        state = list(XplaneEnv.CLIENT.getPOSI())
        self.current_heading = state[5]
        self.current_pitch = state[3]
        self.current_roll = state[4]

        new_yaw = np.clip(self.current_heading, self.min_yaw, self.max_yaw)
        new_pitch = np.clip(self.current_pitch, self.min_pitch, self.max_pitch)
        new_roll = np.clip(self.current_roll, self.min_roll, self.max_roll)

        print(new_yaw)
        reward = self._calculate_reward(new_yaw, new_pitch, new_roll)
        print(reward)
        self.current_yaw = new_yaw
        self.current_pitch = new_pitch
        self.current_roll = new_roll

        terminated = False
        truncated = False
        info = {'current heading': self.current_heading, 'reward_stats': {'new_yaw': new_yaw, 'reward': reward}}

        #log
        self.log.writerow([reward])
        return np.array([self.current_yaw, self.current_pitch, self.current_roll], np.float32), reward, terminated, truncated, info

    def reset(self, seed=None):
        firstHeading = 104.10185241699219
        firstPitch = 17.680604934692383
        firstRoll = 2.047290325164795
        return np.array([firstHeading, firstPitch, firstRoll], np.float32), {}

    def _calculate_reward(self, new_yaw, new_pitch, new_roll):
        # this logic can use when target data is positive.
        err_pitch = 0
        err_roll = 0
        if new_pitch < 0 :
            err_pi = abs(new_pitch)
            pi = self.target_pitch + err_pi
        else:
            pi = self.target_pitch - new_pitch
        
        if new_roll < 0 :
            err_ro = abs(new_roll)
            ro = self.target_roll + err_ro
        else:
            ro = self.target_roll - new_roll

        dis = math.sqrt(abs(self.target_yaw - new_yaw)**2 + abs(pi)**2 + abs(ro)**2)

        reward = 1.0 / (1.0 + dis)

        return reward
    
    def render(self):
        pass

    def close(self):
        pass
