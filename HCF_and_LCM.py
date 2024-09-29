def hcf(x,y):
  if x==y:
    return x
  elif x>y:
    return hcf(x-y,y)
  else:
    return hcf(x, y-x)

a,b= input("Enter  two numbers:").split()
a,b=int(a),int(b)
print("the HCF is"+str(hcf(a,b)))
print("the LCM is"+str(a*b//hcf(a,b)))