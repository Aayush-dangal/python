# def sum_by_team(a):
#     return a+10
# s=lambda a:a+10
# print(s(10))
# # print(sum_by_team(2))

def myfuc(n):
    return lambda x:x*n
    
doubler=myfuc(2)
tripler=myfuc(3)
tripler=myfuc(4)

print(doubler(10))
print(doubler(30))
