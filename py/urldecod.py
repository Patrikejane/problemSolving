burl=input()
N=int(input())
benco=burl.encode('utf-8')
BA=[hex(x) for x in benco]
lBA=len(BA)
C=[]

def base10toN(num,n):
    
    num_rep={10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f',
         16:'g',
         17:'h',
         18:'i',
         19:'j',
         20:'k',
         21:'l',
         22:'m',
         23:'n',
         24:'o',
         25:'p',
         26:'q',
         27:'r',
         28:'s',
         29:'t',
         30:'u',
         31:'v',
         32:'w',
         33:'x',
         34:'y',
         35:'z',
         36:'A',
         37:'B',
         38:'C',
         39:'D',
         40:'E',
         41:'F',
         42:'G',
         43:'H',
         44:'I',
         45:'J',
         46:'K',
         47:'L',
         48:'M',
         49:'N',
         50:'O',
         51:'P',
         52:'Q',
         53:'R',
         54:'S',
         55:'T',
         56:'U',
         57:'V',
         58:'W',
         59:'X',
         60:'Y',
         61:'Z'
             }
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        if 62>remainder>9:
            remainder_string=num_rep[remainder]
        elif remainder>=62:
            remainder_string='('+str(remainder)+')'
        else:
            remainder_string=str(remainder)
        new_num_string=remainder_string+new_num_string
        current=current//n
    return new_num_string

for i in range(N):

    tarurl=input()
    tenco=tarurl.encode('utf-8')
    TA=[hex(x) for x in tenco]
    lTA=len(TA)

    if lBA>lTA:
        CA=BA[0:lTA]
    elif lBA<lTA:

        CA=BA[:]
        u=0
        while len(CA)!=lTA:
            
            CA.append(BA[u%lBA])
            u=u+1

    for j in range(len(CA)):
        C.append("%#0.2x"%(int(CA[j],16)^int(TA[j],16)))

    

    D=C[len(C)-8:len(C)]
    st='0x'
    for k in D:
        st=st+k[2:]
    L=int(st,16)
    print (burl+"/"+base10toN(L,62))
    st=''
    C=[]
    D=[]
    TA=[]
