age = 18
height = 5.11
num = int(input('Enter your number :'))
length = float(input('Enter the required length:'))
breadth = float(input('Enter the required height:'))
area = 0.5 * length * breadth
print(area)

years = int(input('Enter the number of years you have lived '))
 
# 60sec = 1 min , 60 mins = 1hr, 24hr = 1day, 30 days = 1Month, 12Months = 1year
# So 18 years is 18*30*24*60*60
print(years*30*60*60*24)

first_name = 'Shrivatsa'
last_name = 'Johsi'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)


a = b = 2
print(f'{a} +{b}= {a+b}')


# language = 'Python'
# pto = language[0:6:2]
# print(pto)

# c1 = 'Thirty days of python'
# print(c1.capitalize())
# print(c1.swapcase())

name1 = 'Thirty'
name2 = 'Days of '
name3 = 'python'
sentence ='i have started {} {} {}'.format(name1,name2,name3)
print(sentence)