import pandas as pd
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

def load_metadata():
    path = os.getcwd()
    file_name = os.path.join(path,'models/metadata.joblib')
    metadata = joblib.load(file_name)
    return metadata

def load_model():
    path = os.getcwd()
    file_name = os.path.join(path,'models/pipeline.joblib')
    pipeline = joblib.load(file_name)
    return pipeline

def preprocessing(metadata, form_dict):
    names = metadata['all_columns']
    schema = pd.DataFrame(data = 0.0, index = [0], columns = names)
    fields = metadata['entry_columns']
    nums = metadata['num_columns']
    df = pd.DataFrame(data = list(form_dict.values()), index = fields).transpose()
    for num in nums:
      df[num] = df[num].astype('float64')
    df = pd.get_dummies(df)
    aux = df.merge(schema.drop(columns = df.columns.to_list()), how = 'left', left_index=True, right_index=True)
    aux = aux.loc[:, metadata['all_columns']]
    return aux

def scale_and_predict(df, pipeline):
    a = pipeline.predict(df)
    b = pipeline.predict_proba(df)
    return a, b

def predict_attrition(form_dict):
    metadata = load_metadata()
    pipeline = load_model()
    df = preprocessing(metadata, form_dict)
    prediction, probability = scale_and_predict(df, pipeline)
    targets = {0: 'no se vaya', 1: 'se vaya'}
    message = f'El colaborador por ahora puede que {targets[prediction[0]]} con una probabilidad de dejar la compania de {probability[0][1]:.2f}'
    return message


    