texto='Hola mi nombre es Brenda'
txt=texto.split(' ')

print('Texto del archivo:')
with open('texto.txt', encoding='utf-8') as f:
        print(f.read())
        
with open('texto.txt', encoding='utf-8') as f2:
        x=f2.readline().split(' ')

print('\nOración ordenada')
for i in txt:
    for j in x:
        if j==i:
            print(i)
    
    

