def removSame(string):
    chars = []
    for e in string:
        chars.append(e)
    length=len(chars)

    if (length > 2):
        index=2
        while(index<len(chars)):


            if chars[index]==chars[index-1] and chars[index]==chars[index-2]:
                chars.pop(index)
                index=2

            elif index+1<len(chars) and chars[index-2]==chars[index-1] and chars[index]==chars[index+1]:
                chars.pop(index+1)
                index=2

            else:
                index+=1
                continue

        stt = ''
        for t in chars:
            stt += str(t)
        print(stt)
    else:
        stt = ''
        for t in chars:
            stt += str(t)
        print(stt)

if __name__ == '__main__':
    cases=int(input())
    string_list=[]
    for i in range(cases):
        string_list.append(str(input()))
    for i in range(cases):
        removSame(string_list[i])

'''
3
helloo
wooooooow
hellooocc
'''