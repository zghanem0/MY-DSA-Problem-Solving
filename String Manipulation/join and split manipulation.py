'''
You were recently handed a comma-separated value (CSV) file that was horribly formatted. Your job is to extract each row into an list, with each element of that list representing the columns of that file. What makes it badly formatted? The “address” field includes multiple commas but needs to be represented in the list as a single element!

Assume that your file has been loaded into memory as the following multiline string:

Name,Phone,Address
Mike Smith,15554218841,123 Nice St, Roy, NM, USA
Anita Hernandez,15557789941,425 Sunny St, New York, NY, USA
Guido van Rossum,315558730,Science Park 123, 1098 XG Amsterdam, NL
Your output should be a list of lists:

[
    ['Mike Smith', '15554218841', '123 Nice St, Roy, NM, USA'],
    ['Anita Hernandez', '15557789941', '425 Sunny St, New York, NY, USA'],
    ['Guido van Rossum', '315558730', 'Science Park 123, 1098 XG Amsterdam, NL']
]
Each inner list represents the rows of the CSV that we’re interested in, while the outer list holds it all together.

'''
input_string = """Name,Phone,Address
Mike Smith,15554218841,123 Nice St, Roy, NM, USA
Anita Hernandez,15557789941,425 Sunny St, New York, NY, USA
Guido van Rossum,315558730,Science Park 123, 1098 XG Amsterdam, NL"""

def string_split_ex(unsplit):
    results = []

    # Bonus points for using splitlines() here instead,
    # which will be more readable
    for line in unsplit.split('\n')[1:]:
        results.append(line.split(',', maxsplit=2))

    return results

print(string_split_ex(input_string))
# -------------------------------------------------------------------------------------------------------
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

