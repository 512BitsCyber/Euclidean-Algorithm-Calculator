print("Euclidean Algorithm Calculator")

def numask(x):
    RawUserData = input("Number "+x+": ")
    try:
        Localnum = int(RawUserData)
    except:
        print("input must only contain numbers [0-9]")
        numask()
        return
    if (str(Localnum) == RawUserData):
        return Localnum
    else:
        print("mismatch", Localnum, RawUserData)


num1 = numask("1")

num2 = numask("2")

print("#1: ",num1, "\n#2: ",num2)
if (num1 < num2):
    tmp = num1
    num1 = num2
    num2 = tmp

print(num1, "/", num2)
num1old = num1 
num2old = num2
r = num1
print("\n")
while (r != 0):
    r = num1 % num2
    p = num1 // num2
    print(num1, "/", num2, "=", p, "R", r)
    num1 = num2
    num2 = r

print("gcd of",num1old,"and",num2old,"is",num1)
