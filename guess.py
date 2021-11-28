print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
nom = input("   Veuillez entrer votre nom :  ")
h = 0
r = 0
import random
while True :
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("___________________________________    ||  " + str( nom ) + " : " + str( h ) +"  --  "+"moi : " + str( r ) +" ||    ___________________________________")
    
    n = random.randint( 0 , 20 )

    print("Essayez de trouver mon numero ! ")


    i = 0
    while i < 6 :

        x = int(input("  Entrez un numero entre 0 et 20 :  "))

        if x > 20:
            print("       fin ghadi ?!")

        elif x != n :

            if ( x - n > 5 and x - n < 10 ) :
                print()
                print("++++  votre numero est grand ")

            if ( x - n >= 10 ) :
                print()
                print("++++  votre numero est trop grand ")

            if ( x - n <= 5 and x - n > 3 ):
                print()
                print("++++  votre numero est proche ")

            if ( x - n <= 3 and x - n > 0 ):
                print()
                print("++++  votre numero est tres proche ")

        #---------------------------------------------------------------------------------------------

            if ( n - x > 5 and n - x < 10 ) :
                print()
                print("++++  votre numero est petit ")  

            if ( n - x >= 10 ) :
                print()
                print("++++  votre numero est trop petit ") 

            if ( n - x <= 5 and n - x > 3 ) :
                print()
                print("++++  votre numero est proche")

            if ( n - x <= 3 and n - x > 0 ):
                print()
                print("++++  votre numero est tres proche ")


            print()
            print("vous avez encore " + str( 5 - i ) +" tentatives ")
            print()
            i += 1
        
        elif x == n :
            print()
            print("------------->Félicitations vous avez trouvé le numero ! :")
            print("  le numero est : " + str(n) )
            h += 1
            
            break
        
        if i == 6 :

            if x == n :
                print("----------->  Félicitations vous avez trouvé le numero ! :")
                print("                     le numero est : " + str(n) )
                h += 1 

            else :
                print("----------->  Vous avez perdu !")
                print("                     le numero est : " + str(n) )
                r += 1

