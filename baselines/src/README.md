## How to use file

### File 
1. modelMake.py
   Custom env with OpenAI gym
2. learn.py
   learning model and save
3. predict.py
   Use save model for predict

### Activate your virtualenv

    python3.8 -m pip install virtualenv
    virtualenv --python=python3.8 myEnv #you can change myEnv what you want
    cd myEnv
    sudo su
    source bin/activate

### Run
    python3 learn.py
    #choose best model and modify 'model.load()' in predict.py
    python3 predict.py

### Log
Reward will save as csv file in models/PPO.
  
