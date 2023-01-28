import os
print("****************************************************************")
print("*                                                              *")
print("*                                                              *")
print("*                                                              *")
print("*                                                              *")
name = []
name = input("\t\t      Enter your name : ")
shomared = []
shomared = int(input("                    Enter shomare daaneshjui : "))
print("*                                                              *")
print("*\t\t    Plz press ",name[0]," to continue                  *")
print("*                                                              *")
print("*                                                              *")
print("*                                                              *")
print("*                                                              *")
print("****************************************************************")
skip = input()
while skip != name[0] :
    skip = input()
os.system('cls')
first_name = input("1. first_name : ")
last_name = input("2. last_name : ")
phone_number = int(input("3. phone number : "))
sex = input("4. sex : ")
tahol = input("5. tahol(mojarad///motahel) : ")
dad_name = input("6. dad name : ")
mom_name = input("7. mom name : ")
kodemeli = int(input("8. kode meli : "))
shomare_dan = int(input("9. shomare daneshjui : "))
addres = input("10. addres : ")
arrr = []
koler8 = []
faculty_name = input("12. faculty name : ")
riazi = [100,"riazi","azizi"]
ahkam = [101,"ahkam","moslemi"]
adabiat = [102,"adabiat","rezayi"]
zaban = [103, "zaban","biabani"]
eghtesad = [104, "eghtesad","najafi"]
tarbiat_badani = [105, "tarbiat badani","asadi"]
barname_nevisi = [106, "barnaame nevisi","asghari"]  
koler = [riazi,adabiat,zaban,eghtesad,tarbiat_badani,barname_nevisi]  
shabane_or_ruzane = input("11. shabane or ruzane : ")
koler2 = []
war = []
war2 = []
os.system( 'cls' )
mojudi = 0
def printmenu (ash) :
    nn = int(input("\n1. selection\n2. add and remove\n3. confirmation\n4. financial\n5. quit request\n6. about us\n7. exit\n"))
    if nn == 1 :
        os.system('cls')
        riazi = [100,"riazi","azizi"]
        ahkam = [101, "ahkam","moslemi"]
        adabiat = [102, "adabiat","rezayi"]
        zaban = [103, "zaban","biabani"]
        eghtesad = [104, "eghtesad","najafi"]
        tarbiat_badani = [105, "tarbiat badani","asadi"]
        barname_nevisi = [106, "barnaame nevisi","asghari"]  
        koler = [riazi,adabiat,zaban,eghtesad,tarbiat_badani,barname_nevisi]  
        def pop () :    
            ent = int(input("\n1. moshahede dorus\n2. bardashtane vahed\n3. go to main menu\n"))
            if ent == 1 :
                print(" ",riazi,"\n",adabiat,"\n",zaban,"\n",eghtesad,"\n",tarbiat_badani,"\n",barname_nevisi,"\n")
                pop()
            elif ent == 2 :
                tedad = int(input("tedad darsi ke mikhahid bardarid : "))
                arrr = []
                for gg in range(0,tedad) :
                    p = input("kode darse ra vared konid :")
                    arrr.append(p)
                for k6 in range(0,len(arrr)) :
                    for ll in range(0,len(koler)):
                        if int(arrr[k6]) == koler[ll][0]:
                            koler2.append(koler[ll])
                for lk in range(0,len(koler2)) :
                    print("your vaheds are : ",koler2[lk])
                pop()
            elif ent == 3 :
                printmenu(0)
        pop()
    if nn == 2 :
        riazi = [100,"riazi","azizi"]
        adabiat = [102, "adabiat","rezayi"]
        zaban = [103, "zaban","biabani"]
        eghtesad = [104, "eghtesad","najafi"]
        tarbiat_badani = [105, "tarbiat badani","asadi"]
        barname_nevisi = [106, "barnaame nevisi","asghari"]  
        koler = [riazi,adabiat,zaban,eghtesad,tarbiat_badani,barname_nevisi]  
        print(" ",riazi,"\n",adabiat,"\n",zaban,"\n",eghtesad,"\n",tarbiat_badani,"\n",barname_nevisi,"\n")
        def gcc ():
            kk = int(input("\n1. ezafe\n2. hazf\n3. back to main menu\n"))
            if kk == 1 :
                ez = int(input("tedade dars(ha)ye ezafe ra bezanid : "))
                for ii in range(0,ez):
                    kkk = int(input("kode dars ha ra vared konid : "))
                    war.append(kkk)
                koler8 = []
                for mnm in range(0,len(koler2)) :
                    koler8.append(koler2[mnm])

                
                koler2.clear()
                for kkp in range(0,len(koler)) :
                    for jj in range(0,len(war)) :
                        if war[jj] == koler[kkp][0] :
                            koler2.append(koler[kkp])
                koler2.append(koler8[0]) 
                print("ezafe shod")
                print(koler2)    
                gcc()
            elif kk == 2 :
                hazf = int(input("tedade dars(ha)ye ezafe ra bezanid : "))
                for ii2 in range(0,hazf):
                    kkk2 = int(input("kode dars ha ra vared konid : "))
                    war2.append(kkk2)
                for pip in range(0,len(war2)) :
                    for pi in range(0,len(koler2)-1) :
                        if war2[pip] == koler2[pi][0] :
                            koler2.remove(koler2[pi])
                print(koler2)
                gcc()  
            elif kk == 3 :
                printmenu(0)
        gcc()
        koler3 = koler2
    koler3 = koler2
    if nn == 3 :
        for lk66 in range(0,len(koler3)) :
            print("your vaheds are : ",koler3[lk66])
        printmenu(0)
    if nn == 4 :
        os.system('cls')
        if shabane_or_ruzane == "ruzane" :
            print("you are ruzane and don't need to pay money!!!") 
        if shabane_or_ruzane == "shabane" : 
            if ash != 7 :
                mojudi = 0
                def maali(moju) :
                    saw = int(input("1. moshahede mojudi\n2. afzayeshe mojudi\n3. bardashte vajh\n4. raftan be menu\n"))
                    if saw == 1 :
                        print("mojudie shoma : ",moju)
                        maali(moju)
                    if saw == 2 :
                        mab = int(input("Enter mablagh"))
                        int(input("Enter shomare kart : "))
                        int(input("Enter CVV2 : "))
                        int(input("Enter tarikhe engheza : "))
                        moju += mab
                        maali(moju)
                    if saw == 3 :
                        bar = int(input("Enter mablaghe bardashti ra : "))
                        moju = moju - bar
                        maali(moju)
                    if saw == 4 :
                        printmenu(0)
                maali(mojudi)
            else :
                print("you are quitted and there is no info to pay!!!")
                printmenu(7)
    elif nn == 5 :
        os.system('cls')
        aa = input("Are you sure you want to quit? (to quit press Q or q // to get back in menu press M or m)")
        if (aa == "q") or (aa == "Q") :
            input("Enter your reason to quit :")
            print("your reason will be observed it's finished ...\n...\n...\n...\n...\n...\nyou are quited well done!!!")
            ash = 7
            printmenu(7)
            ash = 7
        elif (aa == "m") or (aa == "M") :
            printmenu(0)
    elif nn == 6 :        
        print("your name is " ,first_name, last_name,"\nphone number is :",phone_number,"\ndad name : ",dad_name,"\nmomname : ",mom_name,"\nyour sex is : ",sex,"\nyou are ",tahol,"\nyour kode meli :",kodemeli,"\nshomare daneshjui : ",shomare_dan,"\nyour addres is : ",addres,"\nyour faculy name : ",faculty_name)
        for lk66 in range(0,len(koler3)) :
                    print("your vaheds are : ",koler3[lk66])
        if ash == 7 :
            print("basssse khaste shodam\nyou are quiitted")    
            printmenu(7)
        elif ash != 7 :
            printmenu(0)
    elif nn == 7 : 
        pass
    


printmenu(0)

