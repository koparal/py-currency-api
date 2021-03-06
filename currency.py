import requests
import json

api_key = "7357777cbdf536b54a696842"

def getRatesByBase(base):
    url = "https://prime.exchangerate-api.com/v5/"+api_key+"/latest/"+base
    response = requests.get(url) 
    data = response.text 
    parsed = json.loads(data)
    return parsed
  

print("-- Seçilebilir Döviz kurları --")

for field, key in enumerate(getRatesByBase("TRY")["conversion_rates"]):
    print(key)
            
while(1) :

    process = input("Choose a one \n 1- Currency Rates \n 2- Converter \n")

    base = input("Base Curreny : ").upper()

    if process == "1":
        
       rates = getRatesByBase(base)["conversion_rates"]
       for field, key in enumerate(rates):
            print(key+" => ", rates[key])
            
        
    elif process == "2":

        to = input("To Currency : ").upper()

        pair = base+to
        rates = getRatesByBase(base);
        
        if rates["result"] == "success" :
            rate = rates["conversion_rates"][to]
            amount = float(input("Amount: "))
            total = amount * rate
            print(pair + " : " +str(rate)+ " x "+str(amount)+" = "+str(total)+ " "+to)
        else :
            print("Not supported format. You can also -> Format "+to+base)  
       
    else :       
        print("Not supported format.")
