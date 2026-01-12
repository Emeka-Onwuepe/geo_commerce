import pandas as pd
import numpy as np
import pickle

base_file = 'static/model'
model_file = f'{base_file}/cluster_model.pkl'
cluster_file = f'{base_file}/cluster_details.csv'




def get_outlets(lat,lon):
    # cluster_model = pickle.load(open(model_file, 'rb'))
    # df = pd.read_csv(cluster_file)
        
    # lat = float(lat)
    # lon = float(lon)
    # geo_data = np.deg2rad([lat, lon]).reshape(-1, 2)
    # pre_df = pd.DataFrame(data=geo_data,
    #                       columns= ['latitude_rad', 'longitude_rad']
    #         )

    # [cluster_label] = cluster_model.predict(pre_df)
    # reg = df[df['cluster_label']==cluster_label]['registration_area'].unique()
    # return reg
    return ['emeka','onwuepe']
    
