import re
List = [(25, 13), (22, 19)]
print("Orignal list : ", List)
temp = re.sub(r'[\[\]\(\), ]', '', str(List))
result =  [int(i) for i in set(temp)]
print("Digits Extracted: ",result)
