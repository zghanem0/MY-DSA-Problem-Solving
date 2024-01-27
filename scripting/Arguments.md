# Arguments

## *args and **kwargs

### *args
```
*args: can accept any number arguemnts
```
def foo(*args):
    for a in args:
        print(a)        

foo(1)
```
# 1
```

foo(1, 2, 3)
```
# 1
# 2
# 3
```

### **kwargs
```
Accepts any number or arguments too but convert them to dict
```
def bar(**kwargs):
    print(kwargs)

bar(name='ghanem', age=27)

```
{'name': 'one', 'age': 27}
```
