# intro

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("J\'ai choisi un numero composé de 4 chiffres .")

print("Entrez un nombre a 4 chiffres differents (ne commence pas par 0) , la case m représente les bon chiffres au bonnes places , la case b représente les bon chiffres .")

nom = input("   Veuillez entrer votre nom :  ")

# End intro

#   function that searches for doubles

def count(list):
    l = []

    for e in list:

        if list.count(e) > 1 :

            l.append(1)

        elif list.count(e) == 1 :

            l.append(0)
         
    if 1 in l:

        return "double"

    elif 1 not in l:

        return "0 double"

# --------------------------------------------------------------

h = 0
r = 0

import random

# Start

while True :
   
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    print("___________________________________    ||  " + str( nom ) + " : " + str( h ) +"  --  "+"moi : " + str( r ) +" ||    ___________________________________")
    
    # creation of the random number

    n = []
    q = 0

    while len(n) < 4:
    
        num1 = random.randint(0 , 9)
        num2 = random.randint(1 , 9)

        if q == 0:

            n.append(num2)

        elif num1 not in n:

            n.append(num1)

        q += 1

    # -------------------------------  
      
    print("-------------->    Essayez de trouver mon numero ! ")
    print()
    print("----------------------------------------------------------------------------------------")
    print("                              ||            m             ||            b             ||")
    print("________________________________________________________________________________________")
    
    i = 0
    
    while i < 10 :

        x = []   
        m = 0
        b = 0

        print("                              ||                          ||                          ||")

        xi = int(input("    Numero :     "))
        
        if xi < 1023 or xi > 9876 or count(str(xi)) == "double":

            print("Entrez un nombre a 4 chiffres differents (ne commence pas par 0)")
          
        elif xi >= 1023 and xi <= 9876 and count(str(xi)) == "0 double": 

            y = str(xi)
           
            x = [ int(y[0]) , int(y[1]) , int(y[2]) , int(y[3]) ] 

            if x != n :

                for k in x:

                    if k in n and x.index(k) == n.index(k) :

                        m += 1
                
                    elif k in n and x.index(k) != n.index(k) :

                        b += 1

                print("                              ||            ", m ,"           ||            ", b ,"           ||", "vous avez encore " + str( 9 - i ) +" tentatives ")
               
                i = i + 1
               
            elif x == n :

                print()
                print("------------->Félicitations vous avez trouvé le numero ! :")
                print()
                print("  le numero est : " + str(n) )

                h += 1

                break

            if i == 10 :

                if x == n :

                    print()
                    print("----------->  Félicitations vous avez trouvé le numero ! :")
                    print()
                    print("                     le numero est : " + str(n) )

                    h += 1 

                else :

                    print()
                    print("----------->  Vous avez perdu !")
                    print()
                    print("                     le numero est : " + str(n) )

                    r += 1


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        

            