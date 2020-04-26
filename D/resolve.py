def resolve():
    '''
    code here
    '''

    S = input()

    def chk(num_str):
        temp = int(num_str) % 2019

        if temp == 0:
            return True
        else:
            return False

    ans_set = [ str((i+1) * 2019) for i in range(2*10**5//2019)]

    cnt = 0
    temp = ''
    for i in range(len(S)):
        for j in range(i, len(S)):
            if chk(S[i:j]) and j > 1:
                cnt += 1


    print(cnt)

if __name__ == "__main__":
    resolve()
