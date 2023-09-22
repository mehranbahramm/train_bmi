#a=heigh
#b=weight
#d=cm to m
a=float(input('hi!please enter your height in(cm): ' ))
b=float(input(' well , please now enter your weight in(kg) : '))

d=a*0.01
bmi =round((b/(d*d)), 2)

if bmi < 18.5:
    print ('your bmi is', bmi, 'so, you are underweight!')

elif bmi >= 18.5 and bmi <= 24.99:
    print ('your bmi is', bmi, 'so, you are healthy weight!')

elif bmi >25:
    print ('your bmi is', bmi, 'so, you are extremely obese!')






