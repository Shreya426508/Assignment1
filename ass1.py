def average(a):
    sum=0
    count=0
    for i in range(len(a)):
       sum+=a[i]
       count+=1
    avg=sum/count
    print("total mrks",sum)
    print("average score is",avg)
def maximum(a):
    for i in range(len(a)):
        if a[i]!=-999:
            max=a[0]
    for i in range(len(a)):
        if a[i]>max:
            max=a[i]
    return(max)
def minimum(a):
    for i in range(len(a)):
        if a[i]!=-1:
            min=a[0]
    for i in range(len(a)):
        if a[i]<min:
            min=a[i]
    return(min)
def absent(a):
    count=0
    for i in range(len(a)):
        if a[i]==-1:
            count+=1
    return(count)
marklist=[]
s=int(input("enter number of students"))
for i in range(s):
    mark=int(input("enter the marks"))
    marklist.append(mark)
print(marklist)
flag=1
while flag==1:
    print("1.the average is")
    print("2.the maximum marks ")
    print("3.the minimum marks are")
    print("4.the number  of absent students are")
    print("5.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        print(average(marklist))
        m=input("wanna continue:(yes/no)")
        if m=='yes':
            flag=1
        else:
            flag=0
    elif ch==2:
        print(maximum(marklist))
        m=input("wanna continue:(yes/no)")
        if m=='yes':
            flag=1
        else:
            flag=0
    elif ch==3:
        print(minimum(marklist))
        m=input("wanna continue:(yes/no)")
        if m=='yes':
            flag=1
        else:
            flag=0
    elif ch==4:
        print(absent(marklist))
        m=input("wanna continue:(yes/no)")
        if m=='yes':
            flag=1
        else:
            flag=0
    elif ch==5:
        print("exit")
    else:
        print("!!Wrong Choice!! ")
        a=input("\n\nDo you want to continue (yes/no) :")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program!")