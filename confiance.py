import math
def calc():
    print("confiance")
    # fibre neutre
    n = float(input("effectif total: "))
    xn = float(input("effectif choisis: "))


    f = (xn/n)
    f = (round(f,4))
    print("frequence observer f=",f)
    
    Ic1 = (f-(1/math.sqrt(n)))
    Ic1 = (round(Ic1,2))

    Ic2 = (f+(1/math.sqrt(n)))
    Ic2 = (round(Ic2, 2))

    print("Ic","=","[",Ic1,";",Ic2,"]")
    print(" ")
    Ic1r = Ic1 * 100 
    Ic1r = (round(Ic1r,0))
    Ic2r = Ic2 * 100
    Ic2r = (round(Ic2r,0))
    print("la proportion theorique p est comprise entre ",Ic1r,"%"" et",Ic2r,"%")
calc()