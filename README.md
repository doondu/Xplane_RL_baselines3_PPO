# Xplane_baselines3_PPO
Reinforcement learning with the PPO algorithm in X-plane11 simulator.
<br>
<br>
<br>

## Using tool
1. baselines3
   https://github.com/DLR-RM/stable-baselines3
2. XPC
   https://github.com/nasa/XPlaneConnect
3. X-Plane
   https://www.x-plane.com/
4. FlyWithLua
   https://forums.x-plane.org/index.php?/files/file/38445-flywithlua-ng-next-generation-edition-for-x-plane-11-win-lin-mac/
<br>
<br>
<br>

## reference git
1. https://github.com/adderbyte/GYM_XPLANE_ML

<br>
<br>
<br>
<br>
<br>
<br>

# Setting 1_ XPlane setting
1. X-Plane
   Download and install X-Plane 11

<br>
<br>
<br>


   
# Setting 2_ XPlane connection setting
1. XPC
   link >> https://github.com/nasa/XPlaneConnect/releases
   Download version 1.2.0 XPlaneConnect-v1.2.0.zip (another version make error)
2. Change folder
   - unzip file
   - Move XPlaneConnect (in XPlaneConnect-v1.2.0 folder) folder to /X-Plane 11/Resources/plugins
3. Check your menu bar in X Plane 11
    > plugins > show Plugin Admin
    if you can check X-Plane Connect [Version 1.2.0], it's done

<br>
<br>
<br>



# Setting 3_ FlyWithLua
1. FlyWithLua
   link >> (https://forums.x-plane.org/index.php?/files/file/38445-flywithlua-ng-next-generation-edition-for-x-plane-11-win-lin-mac/)
2. Change folder
   - unzip file
   - Move FlyWithLua foder to /X-Plane 11/Resources/plugins
3. Check your menu bar in X Plane 11
    > plugins > show Plugin Admin
    if you can check XLua 1.0.0r1, it's done

<br>
<br>
<br>



# Setting 4_ virtualenv
- $ python3.8 -m pip install virtualenv
- $ virtualenv --python=python3.8 myEnv (you can change myEnv what you want)
- $ cd myEnv
- $ source bin/activate
