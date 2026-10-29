# siparisin meblegin daxil edin
mebleg =float(input(" mebleg daxil edin:"))
if mebleg>=200:
    endirim = mebleg*0.2
    print("sifarifinizin meblegi:", mebleg)
elif mebleg>=100 and mebleg<=199.99:
    endirim = mebleg*0.1
    print("sifarifinizin meblegi:", mebleg)
elif mebleg<100:
    endirim = 0 
    print ("sifarisinizin meblegi:", mebleg)    
elif mebleg<0:
    print("xeta:")
result = "endirim qazandiriz" if mebleg>200 else "endirim yoxdu"