#taking user's height and wheight input

height =float(input ("please enter your height in meters:"))
wheight = int(input("please enter your weight in kg"))

#bmi formula equal the wheight as intenger ,and and height as float multiplied times two.

bmi_convert= (wheight)/(height)**2

#controle structure to determine the correct statement or condition  to display to the user.
#bmi_convert  If the user’s BMI is 30 or greater the user is obese

if bmi_convert >= 30 :
       print("your BMI is" , bmi_convert,"You are obese !")

# if their bmi is 25 or more than 25 then the user is overwheight

elif bmi_convert >= 25:
       print("your BMI is" ,bmi_convert,"You are overwheight!")

# if their bmi is 18.5 or greater than 18.5 then the user is normal

elif bmi_convert >= 18.5 :
    print( "your BMI is" , bmi_convert , "you are normal ! ")

# if their bmi is 18.5 or less or below  18.5 then the user is underwheight

elif bmi_convert <= 18.5 :
    print( "your BMI is" , bmi_convert , "you are underweight ! ")