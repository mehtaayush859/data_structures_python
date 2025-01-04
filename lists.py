# lists = ['abc','erf','red']
# lists.remove('red')
# print(lists)

# import random
# l = [3,4,5,20,5,25,1]
# print(len(l))
# l.extend([34,5])
# print(l)
# print(random.shuffle(l))

# l1=[1,2,23]
# l2=[2,11,23]
# print(l1==l2)
# print(list("pqrs"))

# def x(values):
#     values[0]=33

# v = [1,2,3]
# x(v)
# print(v)

# l=[3,4,5,20,5,25,1,3]
# l.pop(1)
# print(l)

# m = [0,1,2,3,4,5]
# for x in range(1,5):
#     m[x-1] = m[x]
#     print(m)

# for x in range(0,5):
#     print(m[x],end=" ")

# from time import process_time_ns


# l=[0.5 * a for a in range(0,4)]
# print(l)

# print(list("a#b#c#d".split('#')))


# def x(value,values):
#     v=1
#     values[0]=33

# y=3
# v=[1,2,3]
# print(v)
# x(y,v) 
# print(y,v[0])

# l1=[11,2,23]
# l2=[11,2,2]
# print(l1<l2)

# l1=[0,3,2]
# print(sum(l1))
# l1.insert(2,5)
# print(l1)

# def x(i,values=[]):
#     values.append(i)
#     return values

# x(2)
# x(3)
# y=x(4)
# print(y)

# p = [1,3,5,7,7,1]
# q = p[0]
# a = 0
# for a in range(1,len(p)):
#     if p[a]>q:
#         q=p[a]
#         q=a
# print(q)

# values = [[4,5,6,2],[44,7,2,3]]

# x = values[1][0]
# for lst in values:
#     for element in lst:
#         if x>element:
#             x = element
# print(x)

# x=[20,33,60,[88]]
# y=list(x)
# x[3][0]=90
# x[1] = 35
# print(y)

# x = [2,3,4,5,6]
# for y in range(1,5):
#     x[y-1] = x[y]
#     print(x)
# for y in range(0,5):
#     print(x[y], end ="")

# l1 = [12,3,25,3]
# l2=[12,3,2,5]

# print(len(l1+l2))

# n = [2,4,5]
# n.append([1,2,3,4])
# print(len(n))
# print(n)

# n1 = ['B','D','M']
# if 'b' in n1:
#     print (1)
# else:
#     print(2)

# def increment_i(L, increment):
#     i=0
#     while i < len(L):
#         L[i] = L[i] + increment
#         i= i+1
# values = [2,4,6]
# print(increment_i(values , 2))
# print(values)

# x =[[]]*3
# x[1].append(5)
# print(x)

# m = [4,5,7,2,3]
# m[1:2] = [8,9]
# print(m)

# print(list(zip((2,3,4),('p'),('aaa','bbb'))))
# print(list(zip((3,5),('q','r'),('bb','aa'))))

# def add(l):
#     l += [1]
# my = [2,4,6,8]
# add(my)
# print(len(my))
# print(my)

d=[[[2,3],[4,5]],[[6,7],[8,9]]]
print(d[1][0][0])

f = [[a,a+2,a+3] for a in range(0,3)]
print(f)

x = [[a,b] for a in range(0,2) for b in range(0,2)]
print(x)


c=['aaa','ffff','r']
c.sort(key=len)
print(c)

p = [[2,3],[4,2.5],[0.7,0.7]]
p.sort()
print(p)

x=[[2,3],[4,5]]
print(sum(x,[]))

# def abc(y):
#     x=y[0][0]

#     for row in y:
#         for element in row:
#             if x < element:x = element

#     return x

# print(abc(d[0]))

# list1 = [0.5 * x for x in range(0, 5)]
# print(list1)