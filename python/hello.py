print('Hello World!')
_name = 'Eric'
age = 23
city = 'Yangon'
my_statement = "He lives in Yangon."
about_me = """This is about me.
            How are you?"""
#Single line comment
print(_name,age,city,my_statement,about_me)

if(age>20):
    print('Age is over 20.')
else:
    print('Age is less than 20.')

#with  {},[],()
fruits = ['banana', 'mango',
        'orange','grapes']
print(fruits)
myInfo = _name + \
        city + \
        my_statement + \
        about_me
print(myInfo)