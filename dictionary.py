# dictionaryname = {key1:value1,key2:value2}

pricecam = {"sony":500,"nikon":600,"canon":"700"}
print(pricecam)
pricecam["nickon"]=800
print(pricecam)
pricecam.keys()
pricecam.values()
demo = pricecam.copy()
print(demo)
del pricecam["sony"]
pricecam.clear()