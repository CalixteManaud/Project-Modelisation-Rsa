while True:
    print("Choisissez un nombre premier 'p'");
    p = int(input());
    if p % 2 == 0:
        print("Ce n'est pas un nombre premier, réessayez");
    else:
        break;

while True:
    print("Choisissez un nombre premier 'q'");
    q = int(input());
    if q % 2 == 0:
        print("Ce n'est pas un nombre premier, réessayez");
    else:
        break;

n = p*q;
print (n);

fi = (p-1) * (q-1);
print (fi);

def pgcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)

while True:
    print("Choisissez un nombre 'd' premier avec fi", fi);
    d = int(input());
    if (pgcd(d, fi) != 1):
        print("Ce n'est pas un nombre premier avec fi, réessayez");
    else:
        break;

print("bj");