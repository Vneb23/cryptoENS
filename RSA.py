from random import randrange, getrandbits

# algo déjà implémenté dans python avec "pow". mais cette fonction est changé si on import math. dans ce cas ça peut être utile (même si je crois que ça marche pas tout a fais bien comme il faudrai c’est pour ça que je privilégie la fonction de python de base).
def exmod(x,k,n):
     resultat=1
     k=int((format(k,'b')))
     while k>0:
         if 1==k%2:
             resultat=(resultat*x)%n
         k=(int(k/10))
         x=x*x %n
     return(resultat)

# Test de primalité de Miller Rabin

def est_premier(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n%2 == 0 :
        return False
    s = 0
    r = n-1
    while r%2 == 0:
        s+=1
        r //=2
    for _ in range(k):
        a = randrange(2, n-1)
        x = pow(a, r, n)
        if x != 1 and x != n-1 :
            j=1
            while j < s and x != n-1:
                x = pow(x, 2, n)
                if x==1:
                    return False
                j+=1
            if x != n-1 :
                return False
    return True

#Pour se trouver un nombre premier d’une certaine longueure (en bits; idéaliment 1024 bits pour ce programme)

def premier(l):
    p = 4
    while not  est_premier(p):
        p = getrandbits(l)
        p|= (1 << l-1)|1
    return(p)

# Pour avoir le pgcd et l’inverse modulaire de deux entiers :

def Bezout(a,b):
    r, u, v, r2, u2, v2 = a, 1, 0, b, 0, 1
    while r2 != 0 :
        q = r // r2
        r, u, v, r2, u2, v2 = r2, u2, v2, r - (q*r2), u- (q*u2), v- (q*v2)
    return(r,u,v)

def premieravec(n):
    e = randrange(2,n-1)
    pgcd,u,v = EE(e,n)
    while pgcd !=1 or u <= 0:
        e = randrange(2, n-1)
        pgcd, u, v = EE(e,n)
    return(e, pgcd, u, v)

# Générateur de clef. avec l la «compléxité» (la longueur de la clef) en bits donc

def clef(l):
    p = premier(l)
    q = premier(l)
    while q == p :
        q = premier(l)
    n = p*q
    phi = (p-1)*(q-1)
    e, r, d, v = premieravec(phi)
    return e,n,d

def test(e,n,d):
    M = randrange(3,n//2)
    C = pow (M,e,n)
    dec = pow(C,d,n)
    if M== dec:
        return True
    return False

def code(m, e, n):
    return(pow(m,e,n))

def decode(m, d, n):
    return(pow(m, d, n))
