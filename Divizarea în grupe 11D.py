f=open('c:/Users/Aliona/Desktop/Lista_clasei_11D.txt',mode='r')
linii=f.readlines()
f.close()
#separare pe grupuri eng:
f=open('c:/Users/Aliona/Desktop/grupa1.txt',mode='w')
for i in range(0,len(linii)):
    if 'eng1'in linii[i]:
        f.write(str(linii[i]))
f.close() 
f=open('c:/Users/Aliona/Desktop/grupa2.txt',mode='w')
for i in range(0,len(linii)):
    if 'eng2'in linii[i]:
        f.write(str(linii[i]))
f.close()  
#media generala:
f=open('c:/Users/Aliona/Desktop/Lista_clasei_11D.txt',mode='r')
linii=list(f)
f.close()
media=0
note=[]
for linie in linii:
    campuri=linie.split()
    nota=int(campuri[2])
    note.append(nota)
    note=[int(i) for i in note]
media=(sum(note))/len(note)
med=round(media, 2)
f=open('c:/Users/Aliona/Desktop/Lista_clasei_11D.txt',mode='r')
linii2=f.read()
f.close()
f=open('c:/Users/Aliona/Desktop/Lista_clasei_11D_media.txt',mode='w')
f.write(str(linii2))
f.write('\n')
f.write('Media = ')
f.write(str(med))
f.close()        

