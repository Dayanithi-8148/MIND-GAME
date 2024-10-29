print("\n                         Welcome to the Mind Game!\n\n\nInstruction :\n")
print('''    1)  Think any number between 1 to 30\n    2)  I will ask five question , please answer with "yes" or "no" \n\n''')
st=input("Enter start to Begin : ")
A=['31','29','27','25','23','21','19','17','15','13','11','09','07','05','03','01']
B=['31','30','27','26','23','22','19','18','15','14','11','10','07','06','03','02']
C=['31','30','29','28','23','22','21','20','15','14','13','12','07','06','05','04']
D=['31','30','29','28','27','26','25','24','15','14','13','12','11','10','09','08']
E=['31','30','29','28','27','26','25','24','23','22','21','20','19','18','17','16']
a=1
b=2
c=4
d=8
e=16
if(st.lower()=='start'):
    sum=0
    i=0
    for j in A:
        if(i%4==0):
            print("\n")
        print(j,end=" ")
        i+=1
    print("\n")
    check1=input("Is your number there...? (yes or no) : ")

    i1=0
    for j in B:
        if(i1%4==0):
            print("\n")
        print(j,end=" ")
        i1+=1
    print("\n")
    check2=input("Is your number there...? (yes or no) : ")


    i2=0
    for j in C:
        if(i2%4==0):
            print("\n")
        print(j,end=" ")
        i2+=1
    print("\n")
    check3=input("Is your number there...? (yes or no) : ")


    i3=0
    for j in D:
        if(i3%4==0):
            print("\n")
        print(j,end=" ")
        i3+=1
    print("\n")
    check4=input("Is your number there...? (yes or no) : ")

    i4=0
    for j in E:
        if(i4%4==0):
            print("\n")
        print(j,end=" ")
        i4+=1
    print("\n")
    check5=input("Is your number there...? (yes or no) : ")

    if(check1.lower()=='yes'):
        sum+=a
    if(check2.lower()=='yes'):
        sum+=b
    if(check3.lower()=='yes'):
        sum+=c
    if(check4.lower()=='yes'):
        sum+=d
    if(check5.lower()=='yes'):
        sum+=e

    print("\n")
    print("Your number is : ",sum)

