List_Number =[50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
sort_list =sorted(List_Number)
print (sort_list)
r1_even =[i for i in sort_list if i %2 == 0]
r1_odd =[i for i in sort_list if i %2 != 0]
print ("Even number",r1_even)
print("Odd_number",r1_odd)








# r1_even =[]
# r1_odd =[]
# for i in sort_list :
#     if i%2 ==0 :
#         l =("i am a even number", i)
#         p1 = r1_even.append
#         print (p1)
#     elif i %2 != 0:
#       print("i am a odd number",i)