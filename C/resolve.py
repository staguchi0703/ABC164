def resolve():
    '''
    code here
    '''
    N = int(input())
    S_list = [input() for _ in range(N)]

    print(len(set(S_list)))

if __name__ == "__main__":
    resolve()
