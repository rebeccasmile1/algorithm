a=['a','b','c']
dicta=dict(zip(range(0,len(a)),a))
print(dicta)

# print(type(dicta.keys()))
if 'b' in dicta.values():
    print('True')

dictb={'a':'001','b':'002'}
redictb={v:k  for k,v in dictb.items()}
print(redictb)
