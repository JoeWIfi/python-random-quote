def main():
  # Ajout d'une ligne
  f = open("quotes.txt","a")
  f.write("ligne supplémentaire 5")
  f.close()
  
  #Lecture et affichage des lignes
  f = open("quotes.txt","r")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  
  for i in range(0,last + 1): 
    print(quotes[i])
  
  print ("*******************************************************")
  
  # Suppression de la dernière ligne écrite
  derniere_ligne = quotes[i]
  quotes.remove(derniere_ligne)
   
  # Ecriture du fichier et affichge 
  last = len(quotes) - 1
  
  f = open("quotes.txt","w")
  for i in range(0,last + 1):
    f.write(quotes[i])
    print(quotes[i])
  f.close()

if __name__== "__main__":
  main()
