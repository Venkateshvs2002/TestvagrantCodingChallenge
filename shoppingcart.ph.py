
total=0
maxgst=0

price={"leather_wallet":1100,"Umbrella":900,"Cigarette":200,"Honey":100}
gst={"leather_wallet":18,"Umbrella":12,"Cigarette":28,"Honey":0}
Quantity={"leather_wallet":1,"Umbrella":4,"Cigarette":3,"Honey":2}
for i in price:
    gs=gst[i]
    quan=Quantity[i]
    if price[i]>500:
         pric= price[i]-(price[i]*5/100)
    else:
         price[i]=price

    maxgst=maxgst+(gs*pric*quan/100)
    total=(pric*quan)+maxgst+total
    
    
print("MAX GST Value:",maxgst)
print("Total Amount to be Paid :",total)

