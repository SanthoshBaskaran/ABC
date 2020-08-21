integers=list(map(int,input().split()))
characters=input()
dict1={}
j=0
solution=""
for i in integers:
    dict1[characters[j]]=i
    j=j+1
if(dict1['A']>dict1['B']):
    a=dict1['A']
    b=dict1['B']
    dict1['A']=b
    dict1['B']=a
if(dict1['B']>dict1['C']):
    b=dict1['B']
    c=dict1['C']
    dict1['B']=c
    dict1['C']=b
if(dict1['A']>dict1['B']):
    a=dict1['A']
    b=dict1['B']
    dict1['A']=b
    dict1['B']=a
for j in characters:
    solution=solution+str(dict1[j])+' '
print(solution)
    
