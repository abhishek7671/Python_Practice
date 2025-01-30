# a='abhi bhargav vamsi shankar sai revi shiva muni'

# l= a.split()
# print(l)
# for i in range(len(l)):
#     if i%2 != 0:
#         l[i]=l[i][::-1]
# print(l)


# s = 'one two three four five six'
# l = s.split()
# l1= []
# l2 = [ ]
# print(l)
# for i in range(len(l)):
#     if i%2 == 0:
#         l1.append(l[i])
#     else:
#         l2.append(l[i][::-1])
# print(l1)
# print(l2)



# a="www.facebook.com?name=rajiv&gender=male"
# a = a.split("?")[1]
# a= a.split('&')
# a1=a[0].split('=')
# a2 = a[1].split('=')
# print(a,a1,a2)
# freq = {}
# freq[a1[0]] = a1[1]
# freq[a2[0]] = a2[1]
# print(freq)



# a='http:abc.com?name?vasu?deg?20'

# a= a.split("?")
# print(a)
# dic={}
# dic[a[1]]= a[2]
# dic[a[3]] = a[4]
# print(dic)



# s='qsdfghjkjhgfdsssdfvghjhgfdssdfghjkjhgfdsasdrtgyujijhgfds'

# d={}
# for i in s:
#     if i not in d.keys():
#         d[i] = 1
#     else:
#         d[i]+=1
# print(d)


# s='qsdfghjkjhgfdsssdfvghjhgfdssdfghjkjhgfdsasdrtgyujijhgfds'

# d={}
# for i in s:
#     if i  in d:
#         d[i]+= 1
#     else:
#         d[i]=1
    
# print(d)



# l = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# l1 = []
# for i in l:
#     for j in i.values():
#         l1.append(j)
# print(l1)
# print(set(l1))


# l=[{'name':'ravi','age':12,'sal':20000},{'name':'sai','age':13,'sal':30000},{'name':'mani','age':32,'sal':10000}]
# l1= []
# for i in l:
#     if i['sal']>=20000:
#         print(i)
#         l1.append(i['sal'])
# print(l1)


# d={1:10,3:30,5:50,1:10,4:40,6:60,7:70}
# a=sorted(d.items(),key=lambda x:x[1])
# print(a)


# d={1:10,3:30,5:50,1:10,4:40,6:60,7:70}

# data = sorted (d.items())
# y = dict(data)
# print(y)


# f={}
# a= []
# b=[]
# for i,j in d.items():
#     a.append(i)
#     b.append(j)
# print(a)
# print(b)
# a.sort()
# b.sort()
# for k in range(len(a)):
#     f[a[k]]= b[k]
    

# print(f)


d= {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
items = list(d.items())

n = len(items)
for i in range(n):
    for j in range(n):
        if items[i][0] < items[j][0]:
            items[i], items[j] = items[j], items[i]

a = items

print(a)