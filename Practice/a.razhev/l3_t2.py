#s=raw_input("������� ����������� �����: ")

#as string
'''for i in range(0, 5):
    print "{} ����� ����� {}".format(i+1,s[i])'''

#as digit
'''s=int(s)
znam=10000
for i in range(1, 6):
    print "{} ����� ����� {}".format(i,s//znam)
    s=s%znam
    znam=znam//10'''

#any digit
s=raw_input("������� ����� �����: ")
s=int(s)
t=s
znam=1
n=1
while int(t//10)>0:
    znam=znam*10
    t=t//10
    n=n+1
for i in range(1, n+1):
    print "{} ����� ����� {}".format(i,s//znam)
    s=s%znam
    znam=znam//10
