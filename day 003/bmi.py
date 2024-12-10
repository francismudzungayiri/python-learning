### this is an upgraded version of BMI Calculator 


print('Welcome to MY BMI CALCULATOR')

height = float(input('ENTER YOUR HEIGHT HERE. \n'))
weight = float(input('ENTER YOUR WEIGHT HERE. \n'))

bmi = weight / (height * height)

print(f'YOUR BMI IS {round(bmi,2)}')

if bmi < 18.5:
    print('YOUR ARE UNDERWEIGHT.')

elif bmi < 25:
    print('YOUR HAVE A NORMAL BMI')
    
elif bmi < 30:
    print('YOUR ARE OVERWEIGHT')
    
elif bmi < 35:
    print('YOUR ARE OBESE')

else:
    print('YOU ARE CLINICAL OBESE')