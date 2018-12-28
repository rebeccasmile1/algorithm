'''
用归并，只要交换一次，就count+1
描述

有一个由Ñ个实数构成的数组，如果一对元素A [i]于和A [j]的是倒序的，即我置于<J但是A [1]> A [j]的则称它们是一个倒置，设计一个计算该数组中所有倒置数量的算法。要求算法复杂度为O（nlogn）


输入

输入有多行，第一行整数Ť表示为测试用例个数，后面是Ť个测试用例，每一个用例包括两行，第一行的一个整数是元素个数，第二行为用空格隔开的数组值。


产量

输出每一个用例的倒置个数，一行表示一个用例。


1
8
8 3 2 9 7 1 5 4

17
'''

# def merge_sort(list,count):
#     if len(list)==1:
#         return list
#     mid=len(list)//2
#     left=list[:mid]
#     right=list[mid:]
#     l1=merge_sort(left)
#     r1=merge_sort(right)
#     return merge_sort(l1,r1,count)
# def merge(left,right,count):
#     result=[]
#     while len(left)>0 and len(right)>0:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             count+=1
#             result.append(right.pop(0))
#
#     result+=left
#     result+=right
#     return result
#
#
# if __name__ == '__main__':
#     case_num=int(input())
#     for i in range(0,case_num):
#         data_num=int(input())
#         list=input().split()
#         data_list=[]
#         for e in list:
#             data_list.append(int(e))
#
#         num_swap=0
#         merge_sort(data_list,num_swap)
#         print(num_swap)

def merge_sort(li, count):
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    ll = merge_sort(left, count)
    rl = merge_sort(right, count)

    return merge(ll, rl, count)


# 这里接收两个列表
def merge(left, right, count):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result

    result = []
    while len(left) > 0 and len(right) > 0:
        # 为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            count[0] += len(left)
            result.append(right.pop(0))
    # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += left
    result += right
    return result


test_case = int(input())
for i in range(0, test_case):
    input_length = int(input())
    num_arr = list(map(int, input().strip().split(' ')))
    count = [0]
    merge_sort(num_arr,count)
    print(count[0])
