import pandas as pd
import numpy as np
import pickle


filename = 'frontend/cluster_model.pkl'


def get_outlets(lat,lon):
    cluster_model = pickle.load(open(filename, 'rb'))
    df = pd.read_csv('frontend/cluster_details.csv')
        
    lat = float(lat)
    lon = float(lon)
    geo_data = np.deg2rad([lat, lon]).reshape(-1, 2)
    pre_df = pd.DataFrame(data=geo_data,
                          columns= ['latitude_rad', 'longitude_rad']
            )

    [cluster_label] = cluster_model.predict(pre_df)
    reg = df[df['cluster_label']==cluster_label]['registration_area'].unique()
    return reg
    
