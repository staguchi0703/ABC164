def resolve():
    '''
    code here
    '''
    S, W = [int(item) for item in input().split()]

    if S <= W:
        print('unsafe')
    else:
        print('safe')

if __name__ == "__main__":
    resolve()
