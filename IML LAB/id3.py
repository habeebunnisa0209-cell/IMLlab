import pandas as pd
from math import log2

def entropy(s):
    p=s.value_counts(normalize=True)
    return -(p*(p.apply(log2))).sum()

def gain(df,a,t):
    return entropy(df[t]) - sum((len(df[df[a]==v])/len(df))*entropy(df[df[a]==v][t]) for v in df[a].unique())

def id3(df,attrs,t):
    if len(df[t].unique())==1: return df[t].iloc[0]
    best=max(attrs,key=lambda a:gain(df,a,t))
    tree={best:{}}
    for v in df[best].unique():
        tree[best][v]=id3(df[df[best]==v],[a for a in attrs if a!=best],t)
    return tree

df=pd.read_csv("play_tennis.csv")
print(id3(df,list(df.columns[:-1]),df.columns[-1]))
