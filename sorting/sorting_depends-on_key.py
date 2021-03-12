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


# -------------------------- sorting each letter in the word and then sorting the words it's self to get similar items nearest to each other -----------------
words=["ghanem","haedm","aenhgm","ahmed","ahmedghanem"]
# first step sorting them : sorted_words=[sorted(i) for i in words]
# then join them because sorting spliting each char seperatly to sort them
sorted_words=["".join(sorted(i)) for i in words]
# then sorting the words will if found 2 words identicals will campare ach other it means will have to go deeper in  sorting to letter level not just the words 
print(sorted(sorted_words))

# -----------------------------------------------
#sorting list againest/depends on other list

words=["ghanem","haedm","aenhgm","ahmed","ahmedghanem"]
# first step sorting them : sorted_words=[sorted(i) for i in words]
# then join them because sorting spliting each char seperatly to sort them
sorted_words=["".join(sorted(i)) for i in words]
num_list=[0,1,2,3,4]
num_list.sort(key=lambda x: sorted_words[x])
print(num_list)
