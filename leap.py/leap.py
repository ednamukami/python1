year=range(1999,2070)
for n in year:
    if(n%4==0 or n%100==0 or n%400==0):
        print(f"{n} is a leap year")
    else:
        print(f"{n} is not a leap year")

def drinks(*products):
    spirits=["tank","pilsner"]
    
    for i in products:
        if i in spirits:
            print("go home")
        
            
        else :
            "lets party"
drinks("tank","pilsner","ratish","baileysy")                     