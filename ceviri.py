from googletrans import Translator

# pip install googletrans==3.1.0a0  

while True :
    veri = input ("1-)tr->en \n2-)en-tr \n3-)exit\n")

    if(veri == "1"):
        
        t =  Translator()
        cumle = input("cümleyi yada kelimeyi giriniz : \n")
        output = t.translate(cumle,dest="en")
        print(output.text)

    if(veri=="2"):

        t =  Translator()
        cumle = input("cümleyi yada kelimeyi giriniz : \n")
        output = t.translate(cumle,dest="tr")
        print(output.text)

    if(veri == "3"):
        exit()


# googletrans 3.0.0 sürümünde hata verdiği için kaldırdım.
# pip install googletrans==3.1.0a0 sürümünde rahatlıkla çalıştı.
