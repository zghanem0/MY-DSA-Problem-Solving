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
