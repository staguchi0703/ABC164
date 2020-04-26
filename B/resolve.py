def resolve():
    '''
    code here
    '''
    A, B, C, D = [int(item) for item in input().split()]

    turn = 0
    while A > 0 and C > 0:
        turn += 1
        # print(turn, A, C)

        if turn % 2 == 1:
            C -= B
        else:
            A -= D
        
        # print(A, C)
    
    
    if A <= 0:
        print('No')
    else:
        print('Yes')

if __name__ == "__main__":
    resolve()
