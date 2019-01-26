'''
这次错的是因为没有连续分配
'''
def book():
    num=int(input())
    if num<1 or num>70:
        return
    for i in range(num):
        book_num=int(input())
        temp_list=input().split()
        pages_list=[]
        for e in temp_list:
            if int(e)<1 or int(e)>250:
                return
            pages_list.append(int(e))
        student_num=int(input())
        if book_num<1 or book_num>50 or book_num<student_num:
            return
        if student_num<1 or student_num>50:
            return
        pages_list.sort(reverse=True)
        # print(pages_list)

        div_list=[]
        for j in range(student_num-1):
            div_list.append(pages_list[j])
        temp=0
        for t in range(j+1,len(pages_list)):
            temp+=pages_list[t]
        div_list.append(temp)
        # print(div_list)
        result=max(div_list[0],div_list[-1])
        print(result)

if __name__ == '__main__':
    book()
