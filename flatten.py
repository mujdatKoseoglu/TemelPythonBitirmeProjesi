''' www.patika.dev
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]'''

liste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def duz(liste):
    yeniListe = []
    for i in liste:
        if type(i) != type([]):
            yeniListe.append(i)    
        else: 
            yeniListe.extend(duz(i))    
    return yeniListe
print(duz(liste))

        

