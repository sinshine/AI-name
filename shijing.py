import pandas as pd
from jin import jin
from mu import mu
from shui import shui
from huo import huo
from tu import tu

def df_shijing():
    json_shijing=pd.read_json('shijing.json')

    json_hanzi=pd.read_json('hanzi.json')

    dict_shijing=[]
    for i in json_shijing.index:
        for j in json_shijing['content'][i]:
            for n in j.split('。'):
                for m in n:
                    for k in n:
                        dict_shijing.append([m,k,n,json_shijing['title'][i]])
    df_shijing=pd.DataFrame(dict_shijing).drop_duplicates()
    df_shijing=df_shijing.rename(columns={0:'one',1:'two',2:'content',3:'title'})

    df_shijing=df_shijing.merge(json_hanzi,how='inner',left_on='one',right_on='word')
    df_shijing=df_shijing.merge(json_hanzi,how='inner',left_on='two',right_on='word')

    df_shijing['wuxing_one']='0'
    for i in df_shijing.index:
        if df_shijing['one'][i] in jin:
            df_shijing['wuxing_one'][i]='金'
        elif df_shijing['one'][i] in mu:
            df_shijing['wuxing_one'][i]='木'
        elif df_shijing['one'][i] in shui:
            df_shijing['wuxing_one'][i]='水'
        elif df_shijing['one'][i] in huo:
            df_shijing['wuxing_one'][i]='火'
        elif df_shijing['one'][i] in tu:
            df_shijing['wuxing_one'][i]='土'

    df_shijing['wuxing_two']='0'
    for i in df_shijing.index:
        if df_shijing['two'][i] in jin:
            df_shijing['wuxing_two'][i]='金'
        elif df_shijing['two'][i] in mu:
            df_shijing['wuxing_two'][i]='木'
        elif df_shijing['two'][i] in shui:
            df_shijing['wuxing_two'][i]='水'
        elif df_shijing['two'][i] in huo:
            df_shijing['wuxing_two'][i]='火'
        elif df_shijing['two'][i] in tu:
            df_shijing['wuxing_two'][i]='土'

    return df_shijing
