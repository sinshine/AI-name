import pandas as pd


json_shijing=pd.read_json('shijing.json')

dict_shijing=[]
for i in json_shijing.index:
    for j in json_shijing['content'][i]:
        for n in j.split('。'):
            for m in n:
                for k in n:
                    dict_shijing.append([m,k,n,json_shijing['title'][i]])
df_shijing=pd.DataFrame(dict_shijing).drop_duplicates()
df_shijing=df_shijing.rename(columns={0:'字1',1:'字2',2:'诗词',3:'题目'})



