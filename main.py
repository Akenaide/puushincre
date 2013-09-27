'''
Created on 7 août 2013

@author: KMS
'''
from CharPuush import CharPuush
import webbrowser

if __name__ == '__main__':
    pass

entry = input('lien puush :')
link = entry[14:]
link = link.split('.')[0]
idPuush = list()
continu = 'True'

for charac in link :
    temp = CharPuush(charac)
    idPuush.append(temp)

while (continu == 1) :

    n = int(input("nombre de tour : "))
    
    for i in range(0,n):
        i = 1
        while (idPuush[-i].incre()):
            i += 1
        
        temp = "".join(x.getValue() for x in idPuush)
        webbrowser.open_new('http://puu.sh/'+temp)
    input("Continuer ? : ")
    continu = input("1. pour continuer")
    print(continu)
