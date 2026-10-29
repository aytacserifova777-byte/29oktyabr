# ayliq geliri ve umumi xercleri daxil edin 
gelir=int(input("geliri daxil edin:"))
xercler=int(input("xercleri daxil edin:"))
if gelir<0 and  xercler<0:
 print("gelir ve xercler menfi ola bilmez:")
elif gelir==0: 
    print("hesablara duzgun deyil:")
else:    
    if xercler>gelir:
     print("budce kesiri var:")
    elif xercler>=gelir*0.8:
     print("xerclere diqqet et:")
    elif xercler>gelir*0.8 and xercler<gelir*0.5:
     print("bedce normaldir")
    elif xercler<gelir*0.5:
     print("yaxsi qenaet edirsiz:")
    else:
     print("hesablama duzgun deyil:")
#ayin sonunda qalan pulu ve qenaat faizini tapin
qalan_pul=float(input("qalan pul"))
faiz=float( input("qenaet faizi"))
qalan_pul= gelir- xercler
faiz=(qalan_pul/gelir)*100
print(f"ayin sonuna qalan pul:{qalan_pul}:")
print(f"qenaet faizini hesabla:{faiz}:")


 