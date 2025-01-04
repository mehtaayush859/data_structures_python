# x = {}
# x[3] = 2
# x[2] =[3,4,5]
# del x


# import collections
# x=dict()
# x=collections.defaultdict(int)
# print(x[1])


# count = 0
# for f in x:
#     count += x[f]
#     print(count)





# y = {'jack':10, 'henry':22}
# print(y.get(1,4))

# x1 = {'a':1 , 'b':2}
# x2 = {'a':3 , 'b':2}
# print(x1 == x2)

# z= {f: f*f for f in range(5)}
# print(z)

# f={}
# print(f.fromkeys([2,4,5],'gg'))

# a={'a':1,'b':2,'c':3,'a':4}
# print(any(a))

# import collections
# y=collections.Counter([3,3,4,5,5,5])
# print(y)


# x={}
# x['x']=2
# x['y'] = [3,4,5]


# x={}
# x[2]=2
# x['2']=3
# x[2.0]=5
# count = 0
# print(x)
# for f in x:
#     count+= x[f]
# print(count)

# total={}
# def insert(items):
#     if items in total:
#         total[items] +=1
#     else:
#         total[items] = 1

# insert('Mango')
# print(total)
# insert('Pen')
# print(total)
# insert('Mango')
# print(total)
# print(len(total))


# import collections
# x=collections.Counter([2,2,3,4])
# print(x)
# y=collections.Counter([2,3,3,4,4,4])
# print(x&y)

# d={1:'x',2:'y',3:'z'}
# for a,b in d.items():
#     print(a,b,end=" ")


# x = {'a':15 , 2:'b'}
# y = {'a':25 , 2:'b' }
# print(x == y)

# x={f:'x' + str(f) for f in range(5)}
# print(x)

# t={1:'j', 2:'k', 3:'l'}
# t={}
# print(len(t))

# import collections
# f=collections.OrderedDict((str(p),p) for p in range(3))
# print(f)

f={1:'x',2:'y',3:'z'}
for i in f:
    print(i,end=" ")

import collections
f=dict()
f=collections.defaultdict(lambda:7)
print(f)
print(f[8])


# counts={} 
# counts[(2,3,5)] = 6 
# print(counts)
# counts[(5,3,2)] = 8 
# print(counts)
# counts[(2,3)] = 7 
# print(counts)
# counts[(5,3,2)] = 3 
# print(counts)
# tot = 0 
# for f in counts:
#    tot=tot+counts[f] 
# print(len(counts)+tot)