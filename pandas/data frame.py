import pandas as pd
Data={
    'std1':
    {'Name':'Jyothi',
     'Branch':'Bioinfromatics',
     'Id':'221FA14067',
     'Skills':['Python','DSA','SQL','C']
     },
     'std2':
    {'Name':'Amulya',
     'Branch':'Bioinfromatics',
     'Id':'221FA14074',
     'Skills':['Python','DSA','SQL','C']
     }
}
Data=pd.DataFrame(Data)
print(Data)
print(type(Data))