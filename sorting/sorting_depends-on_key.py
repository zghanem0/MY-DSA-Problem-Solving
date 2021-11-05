# NOTES: 
# key in sorting : is a function that will be called to transform the collection's items before they are compared. The parameter passed to key must be something that is callable.
# what hppen in the background is soring algo go through each element and then campare, now with key u can tell him to go theough or sorting depend on sub sub value in the array that u gonna sort 

# with dictionary
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)



# --------------------------

# using list 

def myFunc(e):
    return e[1]


cars = [
    ['Ford', 2005, 500000000000000],
    ['Mitsubishi', 2000, 200000],
    ['BMW', 2019, 100],
    ['VW', 2011, 11000]
]

cars.sort(reverse=True,key=myFunc)

print(cars)



# using lambda func

def myFunc(e):
    return e[1]


cars = [
    ['Ford', 2005, 500000000000000],
    ['Mitsubishi', 2000, 200000],
    ['BMW', 2019, 100],
    ['VW', 2011, 11000]
]

cars.sort(reverse=True,key=lambda x: x[1])

print(cars)


############################### The Most Interesting Example ############################

# sorting using custom key
employees = [
    {'Name': 'Ahmed Ghanem', 'age': 25, 'salary': 10000},
    {'Name': 'El-Sayed Ghanem', 'age': 30, 'salary': 8000},
    {'Name': 'khaled samer', 'age': 18, 'salary': 10000},
    {'Name': 'mohammed', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee["Name"]


def get_age(employee):
    return (employee["age"],employee["salary"])   # to sorting debends on 2 factors if the age are the same will look at the salary


def get_salary(employee):
    return employee["salary"]


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)  
print(employees, end='\n\n', reverse=True)

employees.sort(key=lambda employee: (employee["salary"],employee["age"]))  # here soring using saray if multiple employee has the same slalary  can be sorted by age
# sort by salary (Descending order)
print(employees, end='\n\n')

'''
>>> there are 2 way to sorting using the key :
1- your own custom function
2- lambda function:
>>> u can sorting against multiple factor, so the function should return 2 things or more: return (employee["age"],employee["salary"])
 - in case of lambda (prefered): employees.sort(key=lambda employee: (employee["salary"],employee["age"]))
 - in case of custome function:                               return (employee["age"],employee["salary"])

'''


# -------------------------- sorting each letter in the word and then sorting the words it's self to get similar items nearest to each other -----------------
words=["ghanem","haedm","aenhgm","ahmed","ahmedghanem"]
# first step sorting them : sorted_words=[sorted(i) for i in words]
# then join them because sorting spliting each char seperatly to sort them
sorted_words=["".join(sorted(i)) for i in words]
# then sorting the words will if found 2 words identicals will campare ach other it means will have to go deeper in  sorting to letter level not just the words 
print(sorted(sorted_words))

# ---------- sort sting depends on key ----------------
logs = """ahmed=10
ghanem=15
ayman=25
abd=20
ghanem=15
ayman=25"""
sorted_list = [tuple(i.split('=')) for i in logs.splitlines()]
sorted_list.sort(key=lambda x: x[1], reverse=True)
seen = []
print(sorted_list)
print("\n".join(['='.join(i) for i in sorted_list if i not in seen  and not seen.append(i)]))

# -----------------------------------------------
#sorting list againest/depends on other list

words=["ghanem","haedm","aenhgm","ahmed","ahmedghanem"]
# first step sorting them : sorted_words=[sorted(i) for i in words]
# then join them because sorting spliting each char seperatly to sort them
sorted_words=["".join(sorted(i)) for i in words]
num_list=[0,1,2,3,4]
num_list.sort(key=lambda x: sorted_words[x])
print(num_list)

