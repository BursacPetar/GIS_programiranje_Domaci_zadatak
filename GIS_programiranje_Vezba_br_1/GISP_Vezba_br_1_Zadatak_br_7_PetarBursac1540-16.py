# Kodiranje skripta
# -*- coding: utf-8 -*-


####### Zadatak br. 7

# definisanje metode kojom se racunaju povrsine tri trougla koja gradi uneta tacka sa temenima,
# uslov je da zbir povrsina bude jednak povrsini glavnog trougla

def daLiTackaPadaUTrougao(M,A,B,C): #tacka koja se ispituje P, ostalo su temena trougla
    xm,x1,x2,x3 = M[0],A[0],B[0],C[0]
    ym,y1,y2,y3 = M[1],A[1],B[1],C[1]
    ceo = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    prvi = 0.5 * abs(x1 * (y2 - ym) + x2 * (ym - y1) + xm * (y1 - y2))
    drugi = 0.5 * abs(x1 * (ym - y3) + xm * (y3 - y1) + x3 * (y1 - ym))
    treci = 0.5 * abs(xm * (y2 - y3) + x2 * (y3 - ym) + x3 * (ym - y2))
    return abs(prvi + drugi + treci - ceo) == 0


if daLiTackaPadaUTrougao((0,0),(-10,0),(10,0), (0,10)) == True:
    print "DA"
else:
    print "NE"
