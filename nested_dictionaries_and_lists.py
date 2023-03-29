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

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

x[1][0] = 15
# print(x)

students[1]["last_name"] = "Bryant"
# print(students)

sports_directory['soccer'][0] = "Andres"
# print(sports_directory)

z[0]['y'] = 30
# print(z)

def iterateDictionary(some_list):
    for x in range(len(some_list)):
        for key, val in some_list[x].items():
            print(key, val)
# iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])
# iterateDictionary2("last_name", students)

def printInfo(some_dict):
    for each_key in some_dict:
        # print(each_key)
        print(len(some_dict[each_key]), " ", each_key)
        for x in range(len(some_dict[each_key])):
            # print(x)
            print(some_dict[each_key][x])

# printInfo(dojo)

