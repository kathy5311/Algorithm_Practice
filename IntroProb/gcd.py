def gcd_sub(a,b):
    while a!=0 and b!=0:
        if a >=b:
            a=a-b
        elif a<b:
            b=b-a
    return a+b

def gcd_mod(a,b):
    if a>=b:
        mod_value=a%b
    elif a<b:
        mod_value=b%a
    return mod_value

def gcd_recur(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    if a>=b:
        return gcd_recur(b, a%b)
    else:
        return gcd_recur(a, b%a)
print(gcd_sub(12,8))
print(gcd_mod(64,12))
print(gcd_recur(60,12))
