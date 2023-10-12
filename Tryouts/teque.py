import sys

f_front = []
m_front = []
m_back = []
b_back = []

numElts = 0
numFront = 0
numBack = 0

numOps = int(sys.stdin.readline()[:-1])

for i in range(numOps):
    op, val = sys.stdin.readline()[:-1].split()


    if op == 'push_front':
        f_front.append(int(val))
        numFront += 1

    elif op == 'push_back':
        b_back.append(int(val))
        numBack += 1

    elif op == 'push_middle':
            
        if numFront < numBack:
            while numFront < numBack and len(m_back) > 0:
                m_front.append(m_back.pop())
                numBack -= 1
                numFront += 1

            temp = len(b_back)
            for i in range(temp):
                m_back.append(b_back.pop())

            while numFront < numBack and len(m_back) > 0:
                m_front.append(b_back.pop())
                numBack -= 1
                numFront += 1

        elif numFront > numBack:
            while numFront > numBack and len(m_front) > 0:
                m_back.append(m_front.pop())
                numBack += 1
                numFront -= 1

            temp = len(f_front)
            for i in range(temp):
                m_front.append(f_front.pop())

            while numFront > numBack and len(m_front) > 0:
                m_back.append(m_front.pop())
                numBack += 1
                numFront -= 1

        if numFront == numBack:
            m_back.append(int(val))
            numBack += 1

        else:
            m_front.append(int(val))
            numFront += 1



    elif op == 'get':
        val = int(val)

        if val < len(f_front):
            print(f_front[-(val+1)])

        elif val < len(f_front) + len(m_front):
            print(m_front[val - len(f_front)])

        elif val < len(f_front) + len(m_front) + len(m_back):
            val -= numFront
            print(m_back[-(val+1)])

        else:
            print(b_back[val - (numFront + numBack)])




    
