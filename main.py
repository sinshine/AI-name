import pandas as pd

def df_s(pth):
    data_s=pd.read_csv(pth)
    #data_s=pd.read_json(pth).dropna()
    data_hanzi=pd.read_csv('./data/kangxi-strokecount.csv')[['Character','Strokes']]
    data_wuxing=pd.read_csv('./data/wuxing.csv')
    dict_s=[]
    for i in data_s.index:
        for m in data_s['content'][i]:
            for n in data_s['content'][i]:
                dict_s.append([m,n,data_s['content'][i],data_s['title'][i]])
        #for j in data_s['content'][i].split('。'):
            #for n in j:
                #for m in j:
                    #dict_s.append([n,m,j,data_s['title'][i]])
    df_s=pd.DataFrame(dict_s).drop_duplicates()
    df_s=df_s.rename(columns={0:'one',1:'two',2:'content',3:'title'})
    df_s['wuxing_one']='0'
    df_s=df_s.merge(data_wuxing,how='inner',left_on='one',right_on='hanzi')
    df_s=df_s.merge(data_wuxing,how='inner',left_on='two',right_on='hanzi')
    df_s=df_s.merge(data_hanzi,how='inner',left_on='one',right_on='Character')
    df_s=df_s.merge(data_hanzi,how='inner',left_on='two',right_on='Character')
    df_s['Strokes']=df_s['Strokes_x']+df_s['Strokes_y']
    return df_s

df_s('./data/shijing_fanti.csv').to_csv('shijing.csv')
