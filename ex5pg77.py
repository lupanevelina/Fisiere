f=open('c:/Users/Aliona/Desktop/text.txt',mode='r')
cr=f.read()
f.close()

print('text: ',cr) 
vc=[]
vocale=set()
for i in range(0,len(cr)):
    if str(cr[i])=='o' or str(cr[i])=='a' or str(cr[i])=='e' or str(cr[i])=='i' or str(cr[i])=='u' or str(cr[i])=='O' or str(cr[i])=='A' or str(cr[i])=='E' or str(cr[i])=='I' or str(cr[i])=='U':
        vc.extend(cr[i]) 
        vocale.update(cr[i])      
lungimea=len(vc)       

f=open('c:/Users/Aliona/Desktop/vocale.txt',mode='w')
f.write(str(lungimea))
f.write('\n')
f.write('Vocalele sunt: ')
f.write(str(vocale))
f.close()

f=open('c:/Users/Aliona/Desktop/vocale.txt',mode='r')
print(f.read())
f.close()

