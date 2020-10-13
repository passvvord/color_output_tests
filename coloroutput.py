COLORS = {
    'r':[255,43,11],
    'g':[33,209,66],
    'b':[30,60,206],
    'y':[255,208,2],
    'c':[42,221,212],
    'p':[207,42,176]
}

GRADIENTS = {
    'lgbt': [[255,43,11],[255,132,25],[255,208,2],[33,209,66],[30,60,206],[105,37,183]],
    'basic': [COLORS['r'],COLORS['y'],COLORS['g']],
    'fullrgb': [COLORS['r'],COLORS['y'],COLORS['g'],COLORS['c'],COLORS['b'],COLORS['p']],
    'fullrgb1': [[255,0,0],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[255,0,255]]
}

def cNum(a):
    return str(int(a)%256)

def colEnd():
    print("\x1b[0m",end="")

# A = [r,g,b]
def colBg(A):
    print("\x1b[48;2;"+cNum(A[0])+";"+cNum(A[1])+";"+cNum(A[2])+"m",end="")  

# A = [r,g,b]    
def colText(A):
    print("\x1b[38;2;"+cNum(A[0])+";"+cNum(A[1])+";"+cNum(A[2])+"m",end="")

# A = [r,g,b]
def col(text,A,type = 'text'):
    if type == 'text':
        return "\x1b[38;2;"+cNum(A[0])+";"+cNum(A[1])+";"+cNum(A[2])+"m"+str(text)+"\x1b[0m"
    else:
        return "\x1b[48;2;"+cNum(A[0])+";"+cNum(A[1])+";"+cNum(A[2])+"m"+str(text)+"\x1b[0m"

# A = [r,g,b]
def colPro(text,A,B):
    return "\x1b[38;2;"+cNum(A[0])+";"+cNum(A[1])+";"+cNum(A[2])+"m"+"\x1b[48;2;"+cNum(B[0])+";"+cNum(B[1])+";"+cNum(B[2])+"m"+str(text)+"\x1b[0m"

def colGradMaxMin(a,max,min,gradient):
    b = ((a-min)/(max-min)*(len(gradient) -1))%(len(gradient))
    br = round(b)%(len(gradient))
    if br < b:
        return [(gradient[br][i] + (gradient[br+1][i]-gradient[br][i])*(b-br))%256 for i in range(3)]
    else:
        return [(gradient[br][i] + (gradient[br-1][i]-gradient[br][i])*(br-b))%256 for i in range(3)]

# A - одновимірний масив
# A2 - двовимірний масив

def getMaxMinA2(A):
    minv = A[0][0]
    maxv = A[0][0]
    for i in A:
        for j in i:
            if j > maxv:
                maxv = j
            elif j < minv:
                minv = j
    return {'max':maxv,'min':minv}

def sortA2(A):
    i = 0
    while i < len(A)-1:
        if sum(A[i]) > sum(A[i+1]):
            temp = A[i]
            A[i] = A[i+1]
            A[i+1] = temp
            i = -1
        i+=1
    for i in range(len(A)):
        j = 0
        while j < len(A[i])-1:
            if A[i][j] > A[i][j+1]:
                temp = A[i][j]
                A[i][j] = A[i][j+1]
                A[i][j+1] = temp
                j = -1
            j+=1
    return A

# Виведення масиву з фоном певного кольору
def printA2Col(A,gradient = GRADIENTS['basic'],contrastText = 0):
    mm = getMaxMinA2(A)
    for i in A:
        for j in i:
            col = colGradMaxMin(j,mm['max'],mm['min'],gradient)
            colBg(col)
            if contrastText:
                if sum(col) > 384:
                    colText([0,0,0])
                else:
                    colText([255,255,255])
            print(('%4d'% j),end='')
        print('')
    colEnd()