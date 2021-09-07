import csv as c

f=open("files/merge_sort.csv", "r")
liste1 = f.read()
f.close()
liste1 = liste1.split(", ")
liste1 = int(len(liste1[0]))

#Eine Liste in zwei Unteristen
def merge_sort(liste1, linker_index, rechter_index):  
    if linker_index >= rechter_index:  
        return  
  
    mitte = (linker_index + rechter_index)//2  
    merge_sort(liste1, linker_index, mitte)  
    merge_sort(liste1, mitte + 1, rechter_index)  
    merge(liste1, linker_index, rechter_index, mitte)  
      
      
#Definieren einer Funktion zum Zusammenführen der Liste     
def merge(liste1, linker_index, rechter_index, mitte):  
      
#Erstellen von Unterteilen einer Liste      
    linke_unterliste = liste1[linker_index:mitte + 1]  
    rechte_unterliste = liste1[mitte+1:rechter_index+1]

#Anfangswerte für Variablen, die wir zum Beibehalten verwenden      

    linke_unterliste_index = 0  
    rechte_unterliste_index = 0  
    sotierter_index = linker_index  
      
#Durchlaufen der Liste bis zum passenden Element        
    while linke_unterliste_index < len(linke_unterliste) and rechte_unterliste_index < len(rechte_unterliste):  

# Wenn unsere linke_unterliste das kleinere Element hat, in das sortierte setzen
  
        if linke_unterliste[linke_unterliste_index] <= rechte_unterliste[rechte_unterliste_index]:  
            liste1[sotierter_index] = linke_unterliste[linke_unterliste_index]  
            linke_unterliste_index = linke_unterliste_index + 1  

# Sonst in die rechte_unterliste           

        else:  
            liste1[sotierter_index] = rechte_unterliste[rechte_unterliste_index]  
            rechte_unterliste_index = rechte_unterliste_index + 1  

#Vorwärts im sortierten Teil     
      
        sotierter_index = sotierter_index + 1  
      
#Durch dir übriggebliebenen Elemente gehen und hizufügen      
       
    while linke_unterliste_index < len(linke_unterliste):  
        liste1[sotierter_index] = linke_unterliste[linke_unterliste_index]  
        linke_unterliste_index = linke_unterliste_index + 1  
        sotierter_index = sotierter_index + 1  
      
    while rechte_unterliste_index < len(rechte_unterliste):  
        liste1[sotierter_index] = rechte_unterliste[rechte_unterliste_index]  
        rechte_unterliste_index = rechte_unterliste_index + 1  
        sotierter_index = sotierter_index + 1  

#Ausführen



merge_sort(liste1, 0, len(liste1) -1)  
f = open("files/merge_sort.csv", "w")
f.write()
f.close()