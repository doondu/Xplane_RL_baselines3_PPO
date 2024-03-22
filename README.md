# Xplane_RL_baselines3_PPO
Reinforcement learning with the PPO algorithm in X-plane11 simulator.

### Using tool
1. baselines3
   https://github.com/DLR-RM/stable-baselines3
2. XPC
   https://github.com/nasa/XPlaneConnect
3. X-Plane
   https://www.x-plane.com/
4. FlyWithLua
   https://forums.x-plane.org/index.php?/files/file/38445-flywithlua-ng-next-generation-edition-for-x-plane-11-win-lin-mac/

### Refernce git
1. https://github.com/adderbyte/GYM_XPLANE_ML
### Environment
Ubuntu 20.04.6 LTS, 64bit x86_64
<br>

--------------------------------

<br>

## Setting

### 1_ XPlane setting
1. X-Plane
   Download and install X-Plane 11
### 2_ XPlane connection setting
1. XPC
   link >> https://github.com/nasa/XPlaneConnect/releases
   Download version 1.2.0 XPlaneConnect-v1.2.0.zip (another version make error)
2. Change folder
   - unzip file
   - Move XPlaneConnect (in XPlaneConnect-v1.2.0 folder) folder to /X-Plane 11/Resources/plugins
3. Check your menu bar in X Plane 11
    - plugins > show Plugin Admin
    if you can check X-Plane Connect [Version 1.2.0], it's done

### 3_ FlyWithLua
1. FlyWithLua
   link >> (https://forums.x-plane.org/index.php?/files/file/38445-flywithlua-ng-next-generation-edition-for-x-plane-11-win-lin-mac/)
2. Change folder
   - unzip file
   - Move FlyWithLua foder to /X-Plane 11/Resources/plugins
3. Check your menu bar in X Plane 11
    - plugins > show Plugin Admin
    if you can check XLua 1.0.0r1, it's done

### 4_ virtualenv

    python3.8 -m pip install virtualenv
    virtualenv --python=python3.8 myEnv #you can change myEnv what you want
    cd myEnv
    source bin/activate

  
### 5_ install baselines3


    pip install stable-baselines3


<br>

--------------------------------

<br>

## Action space parameters

| Action Space Parameter | Action type | Action Value Range |
| --- | --- |---|
| Latitudinal Stick | [Box]|  [-1,1] |
| Longitudinal Stick  | [Box]| [-1,1] |
| Rudder Pedals | [Box]| [-1,1]|
| Throttle | [Box]| [-1/4,1] |


## Observation space parameters


| State Space Parameter | State type | State Value Range |
| --- | --- |---|
| yaw (heading) | [Box]|  [0,360] |
| pitch | [Box] | [-180,180] |
| roll | [Box] | [-180,180]|


<br>

--------------------------------

<br>

## Result

### Learn

![alt-text](https://github.com/doondu/Xplane_RL_baselines3_PPO/blob/main/images/150_ppo_last_reward.png)

### Comparison model_2 and model_150

![alt-text](https://github.com/doondu/Xplane_RL_baselines3_PPO/blob/main/images/test_ppo_model.png)


