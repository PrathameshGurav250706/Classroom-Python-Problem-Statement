# w.a.p to sort given array asending or desending order
# asending order
# n=7
# import array as s
# p=s.array('i',[4,3,5,7,1,2,9])
# for i in range(n):
#     for j in range(n-i-1):
#         if p[j]>p[j+1]:
#             temp=p[j]
#             p[j]=p[j+1]
#             p[j+1]=temp
            
# print(p)
import array as s
p=s.array('i',[4,3,5,7,1,2,9])
# a=s.array('i',sorted(p))
# print(a)


print(sorted(p))

#----------------------------
# desending order

# import array as s
# p=s.array('i',[4,3,5,7,1,2,9])
# p=s.array('i',sorted(p))
# p.reverse()
# print(p)