import os
os.environ['KAGGLE_CONFIG_DIR'] = os.path.join(os.getcwd(),'.kaggle') # to change where the kaggle.json file is located
commands= ['kaggle datasets download -d vjchoudhary7/hr-analytics-case-study', \
    'unzip \*.zip -d datasets && rm *.zip']

for command in commands:
    os.system(command)

    