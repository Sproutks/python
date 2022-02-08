from numpy import average


studentName=input("Enter Student Name:")
institute=input("Enter School/college Name:")
city=input("Enter City:")
subject1=int(input("Enter Subject 1 mark: "))
subject2=int(input("Enter Subject 2 mark: "))
subject3=int(input("Enter Subject 3 mark: "))
subject4=int(input("Enter Subject 4 mark: "))
subject5=int(input("Enter Subject 5 mark: "))
total=subject1+subject2+subject3+subject4+subject5
avg=int(total/5)
if avg>=91 and avg<=100:
    grade="A+"
elif avg>=86 and avg<=90:
    grade="A"
elif avg>=80 and avg<=85:
    grade="B+"
elif avg>=75 and avg<=79:
    grade="B"
elif avg>=70 and avg<=78:
    grade="C"
elif avg>=60 and avg<=69:
    grade="D"
elif avg>=50 and avg<=59:
    grade="E"
elif avg<50:
    grade="F"
else:
    grade="Somthing went wrong. Kindly check your inputs"

if grade!="F" or grade!="Somthing went wrong. Kindly check your inputs":
    result="PASS"
else:
    result="FAIL"
print("--------------------------------------")
print("           Your details                ")
print("--------------------------------------")
print(f'Name: {studentName}')
print(f'institute: {institute}')
print(f'City: {city}')
print(f'subject1 marks: {subject1}')
print(f'subject2 marks: {subject2}')
print(f'subject3 marks: {subject3}')
print(f'subject4 marks: {subject4}')
print(f'subject5 marks: {subject5}')
print("--------------------------------------")
print("           Mark details                ")
print("--------------------------------------")
print(f'TOTAL = {total}')
print(f'AVERAGE = {avg}')
print(f'GRADE = {grade}')
print(f'RESULT = {result}')
if result=="PASS":
    print("CONGRATULATIONS YOU HAVE PASSED THE EXAM")
else:
    print("BETTER LUCK NEXT TIME")




