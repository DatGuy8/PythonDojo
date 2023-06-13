x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
print('===============1======================')
#1.1
x[1][0] = 15
print(x)
#1.2
students[0]['last_name'] = 'Bryant'
print(students[0])
#1.3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])
#1.4
z[0]['y'] = 30
print(z)
print('================1=====================')

print('================2=====================')
#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(0,len(students)):
        # print(i, students[i])
        for x, y in students[i].items():
            print(f'{x} - {y}')

iterateDictionary(students)
print('==================2===================')
print('=================3====================')

#3
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])


iterateDictionary2('first_name',students)

print('==================3===================')

print('===================4==================')
#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in some_dict:
        print(len(some_dict[i]),i)
        for j in some_dict[i]:
            print(j)


printInfo(dojo)

print('===================4==================')