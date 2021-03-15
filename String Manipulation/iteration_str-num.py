# how to iterate through the dictionary : https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas?rq=1

# how to interate through the string and split it into line so u can iterate it as line by line not a char by char : 
Here are three possibilities:

foo = """
this is 
a multi-line string.
"""

def f1(foo=foo): return iter(foo.splitlines())

def f2(foo=foo):
    retval = ''
    for char in foo:
        retval += char if not char == '\n' else ''
        if char == '\n':
            yield retval
            retval = ''
    if retval:
        yield retval

def f3(foo=foo):
    prevnl = -1
    while True:
      nextnl = foo.find('\n', prevnl + 1)
      if nextnl < 0: break
      yield foo[prevnl + 1:nextnl]
      prevnl = nextnl

if __name__ == '__main__':
  for f in f1, f2, f3:
    print list(f())
