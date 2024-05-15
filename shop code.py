#------------array_dictionuary-------------
myfile=open("shop deta.txt","r")
data=myfile.read()
PRODUCT=[]
product_list=data.split("\n")
for i in range(len(product_list)):
    product_info=product_list[i].split(",")
    mydict={}
    mydict["code"]=product_info[0]
    mydict["name"]=product_info[1]
    mydict["price"]=product_info[2]
    mydict["count"]=product_info[3]
    PRODUCT.append(mydict)

#-----------def_menu------------
from pyfiglet import Figlet
f=Figlet(font="standard")
def show_menu():
    print("1-Add product")
    print("2-Edit product")
    print("3-Delete product")
    print("4-Search product")
    print("5-Show list")
    print("6-Buy")
    print("7-exit")


#---------------------------------------Add product---------------------------------------
def Addproduct ():
    while True:
        check=input("agar ghasd ezafe kardadn mahsol ra darid benevisid (y)  va agar na benevisid (n)   :")
        if check=="y":
            mydict={}
            mydict["code"]=input("code mahsol ra vared konid    :")
            mydict["name"]=input("name mahsol ra vared konid    :")
            mydict["price"]=input("gheymat mahsol ra vared konid    :")
            mydict["count"]=input("tadade mahsol ra vared konid    :")
            PRODUCT.append(mydict)
        else:
            break


#---------------------------------------------------------------Edit product----------------------------------------------------------------------
def Editproduct():
    while True:
        check=input("agar ghasd edit ra darid benevisid (y)  va agar na benevisid (n)    :")
        if check=="y":
            i=0
            for i in range(len(PRODUCT)):
                print(PRODUCT[i]["code"]," , ",PRODUCT[i]["name"])
            edit=input("(name) ya (code) mahsol ra vared konid    :")
            i=0
            for i in range(len(PRODUCT)):
                if edit==PRODUCT[i]["name"] or PRODUCT[i]["code"]:
                    PRODUCT[i]["code"]=input("code mahsol ra vared konid    :")
                    PRODUCT[i]["name"]=input("name mahsol ra vared konid    :")
                    PRODUCT[i]["price"]=input("gheymat mahsol ra vared konid    :")
                    PRODUCT[i]["count"]=input("tadade mahsol ra vared konid    :")
                    break
            print("edit anjam shod")
        else:
            break


#-----------------------------------------Delete product------------------------------------------------
def Deleteproduct():
    while True:
        check=input("agar ghasd hazf ra darid benevisid (y)  va agar na benevisid (n)    :")
        if check=="y":
            i=0
            for i in range(len(PRODUCT)):
                print((PRODUCT[i]["code"]) ,(PRODUCT[i]["name"]))
            delet=input("(name) ya (code) mahsol ra vared konid    :")
            i=0
            for i in range(len(PRODUCT)):
                if delet==PRODUCT[i]["name"] or delet==PRODUCT[i]["code"]:
                    break
            del PRODUCT[i]
            print("mahsol pak shod")
        elif check==("n"):
            break


#---------------------------------------------------Search product-------------------------------------------------------
def Searchproduct():
        while True:
            check=input("agar ghasd jost va jo mahsol ra darid benevisid (y)  va agar na benevisid (n)    :") 
            if check=="y":
                search=input("(name) ya (code) mahsol ra vared konid    :")
                i=0
                for i in range(len(PRODUCT)):
                    if search==PRODUCT[i]["name"] or search==PRODUCT[i]["code"]:
                        break
                print(PRODUCT[i])
            else:
                break


#--------------------------------------------------Show list---------------------------------------------------------------
def Showlist():
    check=input("agar ghasd tamasha list ra darid benevisid (y)  va agar na benevisid (n)    :")
    if check=="y":
        print("code", " - ", "name", " - ","pric", " - ","count")
        for i in range(len(PRODUCT)):
            print(PRODUCT[i]["code"]," -",PRODUCT[i]["name"]," -",PRODUCT[i]["price"]," -",PRODUCT[i]["count"])
        

#------------------------------------------------Buy----------------------------------------------------
def Buy():
    while True:
        check=input("agar ghasd kharid ra darid benevisid (y)  va agar na benevisid (n)    :")
        if check=="y":
            for i in range(len(PRODUCT)):
                print(PRODUCT[i]["code"]," , ",PRODUCT[i]["name"]) 
            i=0
            buy=input("(name) ya (code) mahsol ra vared konid    :")
            for i in range(len(PRODUCT)):
                if buy==PRODUCT[i]["name"] or buy==PRODUCT[i]["code"]:
                    break
            while True:
                count1=PRODUCT[i]["count"]
                icount=int(PRODUCT[i]["count"])
                count=int(input("tedadi ke mikhahid az in mahsil bekharid    :"))
                price1=int(PRODUCT[i]["price"])*count
                if icount>=count:
                    print("geymat mahsol barabar ast ba", price1 , "agar hamchenan ghasd kharid ra darid benevisid  (y)")
                    gheymat=input(":        ")
                    if gheymat==("y") :
                        icount-=count
                        fcount=str(icount)
                        PRODUCT[i]["count"]=fcount
                        print("kharidari shod")
                        break
                    else:
                        break
                else:
                    print("mojodi dar anbar kafi nist")
        else:
            break


#---------------------------Exit---------------------------
def Exit():
    myfile = open ("shop deta.txt" , "a")
    myfile.write(PRODUCT)
    myfile.close()
    print("az barname kharej shodid")




#----------------------------run--------------------------------
while True:


    #-----------------menu-------------------
    print(f.renderText("Behdad Store"))
    show_menu()
    user=int(input("please chosse a number:    "))

    #---------if----------
    if user==1:
        Addproduct()
    elif user==2:
        Editproduct()
    elif user==3:
        Deleteproduct()
    elif user==4:
        Searchproduct()
    elif user==5:
        Showlist()
    elif user==6:
        Buy()
    elif user==7:
        Exit()

#------------------------------------------------------------End------------------------------------------------------------
