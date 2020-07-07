
'''
# Question
Using our web scraping tutorial, you’ve built a great weather scraper. However, it loads string information in a list of lists, each holding a unique row of information you want to write out to a CSV file:

[
    ['Boston', 'MA', '76F', '65% Precip', '0.15 in'],
    ['San Francisco', 'CA', '62F', '20% Precip', '0.00 in'],
    ['Washington', 'DC', '82F', '80% Precip', '0.19 in'],
    ['Miami', 'FL', '79F', '50% Precip', '0.70 in']
]
Your output should be a single string that looks like this:

"""
Boston,MA,76F,65% Precip,0.15in
San Francisco,CA,62F,20% Precip,0.00 in
Washington,DC,82F,80% Precip,0.19 in
Miami,FL,79F,50% Precip,0.70 in
"""
'''

input_list = [
    ['Boston', 'MA', '76F', '65% Precip', '0.15 in'],
    ['San Francisco', 'CA', '62F', '20% Precip', '0.00 in'],
    ['Washington', 'DC', '82F', '80% Precip', '0.19 in'],
    ['Miami', 'FL', '79F', '50% Precip', '0.70 in']
]
# when u join  u join an iterable "row" ,
# here i want u to put an ','  between every element in that iterable (row)
joined = [','.join(row) for row in input_list] # for every row, that is a complicated way of [row for row in input_list]
output = '\n'.join(joined)

print(output)

