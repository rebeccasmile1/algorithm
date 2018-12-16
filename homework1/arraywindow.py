from typing import List, Any

if __name__ == '__main__':
    temp_list=input().split(' ')
    data_list=[]
    for element in temp_list:
        data_list.append(int(element))#int 不可以用extend,要用append
    # print(data_list)
    window_size=int(input())
    result_list=[]
    result=0
    for i in range(window_size-1,len(data_list)):
        result_temp_list=[]
        for j in range(i-(window_size-1),i+1):
            result_temp_list.append(data_list[j])
        result_temp_list.sort()
        result=result+result_temp_list[-1]

    print(result)


