#PROJECT ABOUT A ONLINE RIDE BOOKING APP


#empty strings
d=[]
p=[]
#permenet riders time slote
g=["13-14","14-16"]



#main loop
def mainloop():
    while True:
        print("*" * 30 + "WHEEL ROUTE" + "*" * 30 + "\n") 
        print("*" * 30 + "LOGIN" + "*" * 30 + "\n"     
              "\t(G) GIVE A RIDE\n"                              
              "\t(B) BOOK A RIDE\n"
              "\t(F) TOTAL FAIR\n"
               "\t(R) BOOKED RECEIPT\n"
                "\t(E) EXIT \n" 
                  "\t(Z) REVIEW \n"+
              "_" * 72)
        
        
        x=input('Enter the choice=').upper()
        if x=="G":
            givearide()
            break
        elif x=="B":
            bookaride()
            break
        elif x=="F":
            wages()
            break
        elif x=="R":
            ticketrecipt()
            break
        elif x=="E":
            print("")
            break
        elif x=="Z":
            RATING()
            break
            
        else:
            print("invalid value")
            mainloop()
            break



        

#cancellation function
        
def gh():
    
    print("\n"*2)
    x=input("*******************CONFIRM CANCELATION PRESS (Y)  OR (N)=********************").upper()
    print("\n"*2)
    
    if x=="Y":
     k=input("Enter The Time Slot (24hr)(hh-hh)=")
     if k in d:
      d.remove(k)
      print("\n"*2)
      print("***************CANCELLATION SUCCESSFUL******************")
      print("\n"*2)
      v=input("To EXIT(E),                              Login (L)").upper()
      if v=="E":
        print("")
      elif v=="L":
        mainloop()
      else:
        print("error")
        
     else:
        print("        There is No Such Time Slot pls re-check         ")
        gh()
        print("\n"*2) 
    else:
        ca()
        print("\n"*2)

#RATING
def RATING():

    print("*********HOW DO YOU RATE US IN THE SCALE OF 1-5*********")
    print("1-*")
    print("2-* *")
    print("3* * *")
    print("4-* * * *")
    print("5-* * * * *")
    rate=input("ENTER YOUR CHOICE=")
    print("***THANK YOU FOR RATING",rate,"STAR\n***")
    print("\n")
    print("PLEASE SHARE YOUR EXPERIENCE")
    
    rat=input(":)")
    v=input("EXIT(E)                                                   Login(L):").upper()
    if v=="E":
        print("")
    else:
        mainloop()






#last after ticket (exit)

def ca():
    print("\n"*2)
    v=input("To EXIT(E),               Cancel(C)                         Login (L)").upper()
    if v=="E":
        print("")
    elif v=="C":
        gh()
        print("\n"*2)
    elif v=="L":
        mainloop()
        print("\n"*2)
    else:
        print("               Invalid Input                   ")
        ca()
        print("\n"*2)
           

        

def sd():
            print("\n")
            print("         FORMAT=HH-HH                  H-HOUR          ")
            print("\n")
            start=input("Time(24hr):")
            if start in g:
                print("\n"*2)
                print("                    ***************RIDERS ARE AVAILABLE****************                     ")
                print("                                   TIME SLOT IS BOOKED                                      ")
                d.append(start)
            
                c()
            else:
                print("\n"*2)
                print("                   *******************SLOT IS CURRENTLY UNAVAILABLE**********************             ")
                print("                     PLS CHOOSE OTHER TIME SLOT OR WAIT FOR THE RIDERS                   ")
    
                sd()  

#BOOK A RIDE

 
 
 
         
def bookaride():
    print("*" * 34 +"BOOK A RIDE"+"*" * 34 +"\n")
    print("-" * 34 +"Please Enter The Details"+"-" * 34 +"\n")
    name=input("Enter Your Name=")
    d.append(name)
    if len(name)>=1:
        location=input('Enter The Current Location=')
        d.append(location)
    else:
        print('Complete The Following Data')
        d.clear()
        bookaride()
    if len(location)>=1:
        duration=input('Enter The Destination=') 
        d.append(duration)   
    else:
        print("Complete the following data")
        d.clear()
        bookaride()
    if len(duration)>=1:
        Phone_number=input("Enter Phoneno:")
    if len(Phone_number)==10:
        d.append(Phone_number)
        
        phone()
        
    else:
        print("Should be 10 digit no")
        d.clear() 
        bookaride()
    if len(Phone_number)==10:
        print("\n")
        print("******Enter the time slot to book*********")
        
        sd()
  
        
            



#C FUNCTION TO PRINT THE BALACE CONTENTS IN BOOK A RIDE   


        
def c():             
    print("\n"*2)
    print("*"*5+"'Y' if the given answer is correct or press 'N' to re-enter" +"*"*5+"\n")
    c=input('Click Y/N=')
    print("\n"*2)
    
    if c=="y" or c=="Y":
        ticketrecipt()
       
    else:
        print("booking error")
        bookaride()



#F FUNCTION TO PRINT THE BALACE CONTENTS IN GIVE A RIDE



def f():
    print("\n"*2)
    print("*"*5+"'Y' if the given answer is correct or press 'N' to re-enter" +"*"*5+"\n")
    c=input('Click Y/N=')
    print("\n"*2)
    
    if c=="y" or c=="Y":
        print("*" *5+"Your Booking Has Confirmed"+"*"*5+"\n"*2+"*"*5+"Wait For The Rider"+"*"*5+"\n"*2+
              "THANKYOU FOR CHOOSING US"+"\n"*2+"ENJOY THE RIDE" )
        
        
       
    else:
        print("booking error")
        givearide()

#GIVE A RIDE 


              
def givearide():
    print("*" * 34 +"GIVE A RIDE"+"*" * 34 +"\n")
    print("\n"*2)
    print("^" *10+"RIDERS ARE REQUESTED TO REACH AT THRISSUR ROUND BEFORE BOOKING YOUR RIDE"+"^"*10)
    print("\n"*2)
    print("-" * 34 +"Please Enter The Details"+"-" * 34 +"\n")
    name=input("Enter Your Name=")
    if len(name)>=1:
        print("PLS ENTERT THE DETAILS IN FOLLOWING ORDER"+" \n"*2+
              "******   ""HH-HH"    "24HR""   ****** "+"\n"*2 )
        slot=input('Enter The slot=')
        g.append(slot)
    else:
        print('Complete The Following Data')
        givearide()
    if len(slot)>=1:
        Licenceno=input('Enter The Licence No=')    
    else:
        print("Complete the following data")
        givearide()
    if len(Licenceno)>=1:
        address=input("Enter Address=")
    else:
        print("Complete the following data")
        givearide()        
    if len(address)>=1:
        Phone_number=input("Enter Phoneno:")
    if len(Phone_number)==10:
        
        phone2()
        
    else:
        print("Should be 10 digit no") 
        givearide()
    print("\n"*2)
    print("------------------------------------------------------------------------------")
    print("                             WHEEL ROUTE                                      ")
    print("------------------------------------------------------------------------------")
    print("                                                                              ")
    print(" e_Ticket :", "     Address                : Near Thrissur Round""               ")
    print("           ", "Phone No\Mob No             : 8000800088,8888880000               ")
    print("-------------------------------------------------------------------------------")
    print("                                                                              ")
    print("Name:",name,"            ""Slot:",slot,"         ","      Licence No:",Licenceno,"                  ")
    print("                                                                              ")
    print("Address:",address,"                          Phone no:",Phone_number,"                            ")
    print("______________________________________________________________________________")
    print("                                                                              ")
    print("           ***           Your Booking Has Confirmed       ***                 ")
    print("                                                                              ")
    print("                          ENSURE SAFTY MEASURES                         ")
    print("                        THANKYOU FOR CHOOSING US                             ")
    print("                            ENJOY THE RIDE                                     ")
    print("                                                                              ")
    print("------------------------------------------------------------------------------")
    v=input("EXIT(E)                     Cancel(C)                       Login(L):").upper()
    if v=="E":
        print("")
    else:
        mainloop()    
        

    
    
def wages():
    print("\n"*2)
    print("*"*24+"TOTAL FAIR"+"*"*24)
    print("\n"*2)
    B=int(input("STARTING KM="))
    L=int(input("ENDING KM="))
    S=L-B
    p.append(S)
    m=15
    n=m+S*10
    p.append(n)
    fair()

    
#FAIR CALCULATION RECEIPT
#FAIR CALCULATION RECEIPT
def fair():
    print("\n"*2)
    print("------------------------------------------------------------------------------")
    print("                             WHEEL ROUTE                                      ")
    print("------------------------------------------------------------------------------")
    print("                                                                              ")
    print(" e_Ticket :", "      Address              : Near Thrissur Round""               ")
    print("           ", "Phone No\Mob No             : 8000800088,8888880000               ")
    print("------------------------------------------------------------------------------")
    print("                                                                              ")
    print("Fair Price=15/-""        ""Total Km Travelled=",p[0],"      1km= 10/-"     "                 ")
    print("                                                                              ")
    print("           ***          Total Fair:",p[1],"/-""           ***                      ")
    print("______________________________________________________________________________")
    print("                                                                              ")
    print("           ***                  THANKYOU                  ***                 ")
    print("                                                                              ")
    print("                          HOPE U ENJOYED THE RIDE                             ")
    print("                                                                              ")
    print("------------------------------------------------------------------------------")
    print("\n"*2)
    print("-------------------------------PAYMENT METHOD--------------------------------")
    print("(M) CASH""----------------------------------------------""(U) UPI")
    
    g=input("").upper()
    if g=="M":
        print("")
    elif g=="U":
        z=input("Enter your upi id:")
        if len(z)>=1:
            print("-----------------PAYMENT SUCCESSFUL--------------")
            ca()    
    v=input("EXIT(E)                                                   Login(L):").upper()
    if v=="E":
        print("")
    else:
        mainloop()





#TO CHECK IF THE GIVEN VALUE IS A DIGIT

 
    
def phone():
    x="10"
    y=x.isdigit
    return
def phone2():
    x="10"
    y=x.isdigit
    f()



#TICKET
     
     
     
       
def ticketrecipt():
    if d==[]:
        print("****** YOU HAVE NOT BOOKED******")
        v=input("To EXIT(E),                              Login (L)").upper()
        if v=="E":
            print("")
        elif v=="L":
            print("\n"*2)
            mainloop()
        else:
            print("error")
    else:    
        print("\n"*2)
        print("------------------------------------------------------------------------------")
        print("                             WHEEL ROUTE                                      ")
        print("------------------------------------------------------------------------------")
        print("                                                                              ")
        print(" e_Ticket :", "    Address                 : Near Thrissur Round""               ")
        print("           ", "Phone No\Mob No             : 8000800088,8888880000               ")
        print("------------------------------------------------------------------------------")
        print("                                                                              ")
        print("Location=>",d[0],"------------->",d[2],"      ","      Passenger Name:",d[1],"                 ")
        print("                                                                              ")
        print("                 Phone no:",d[3],"           Booked Time Slot=",d[4], "     ")
        print("______________________________________________________________________________")
        print("                                                                              ")
        print("           ***           Your Booking Has Confirmed       ***                 ")
        print("                                                                              ")
        print("                       Our Rider Will Reach in 10 min                         ")
        print("                         THANKYOU FOR CHOOSING US                             ")
        print("                           ENJOY THE RIDE                                     ")
        print("                                                                              ")
        print("------------------------------------------------------------------------------")
        ca()         
            

        

mainloop()        


