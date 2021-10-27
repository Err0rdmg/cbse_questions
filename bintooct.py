# Covert binary to decimal number 
def covertbinoct(num, base = 2):
  str1 = ""
  while num != 0 :
    str1 = str1+ str(num%base)
    num = num//base
  str1 = str1[::-1]
  
  print(str1)

num = int(input("Enter the number here:"))
covertbinoct(num)
covertbinoct(num, 8)