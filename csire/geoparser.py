from mordecai import Geoparser
import pandas as pd

def main(df, country_code):
    print("======Geoparsing...======")
    geo = Geoparser()

    listText = df['text']
    df['result'] = geo.batch_geoparse(listText)

    df['correct'] = 0
    coordPoints = []

    for i in range(len(df['text'])):
        for dict in df['result'][i]:

            if df['correct'][i] == 0 and country_code == dict['country_predicted']:

                df['correct'][i] = 1
                coordPoints.append((float(dict['geo']['lat']),float(dict['geo']['lon']),dict['geo']['place_name'],df['dead_number'][i],df['injured_number'][i],df['missing_number'][i]))
            
    df = df.loc[df['correct']==1]

    df.to_csv("processed.csv")

    return coordPoints
