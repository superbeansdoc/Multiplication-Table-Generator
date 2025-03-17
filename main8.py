number = int(input("what number to make a table for"))
list = []
for i in range(10):
    Fun = number * i
    print (number), print ("times") , print(i) , print("=") , print (Fun)
    list.append(Fun)
print("mutplaction resluts") ; print(list)