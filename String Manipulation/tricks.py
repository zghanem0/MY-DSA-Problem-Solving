#split at multiple delimiter
word="ahmed_ghanem/is-happy"
folder= word.replace('/', '_').split("_")
print(folder)
