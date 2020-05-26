import re

sample_list = ['4123456789123456', '5123-4567-8912-3456', '61234-567-8912-3456',
               '4123356789123456', '5133-3367-8912-3456', '5123 - 3567 - 8912 - 3456']
pattern = '^[456][0-9]{15}|[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$[\d]\1{3,}'


for eachnumber in sample_list:
    result = re.match(pattern, eachnumber)
    if result:
        print(eachnumber + "->" + "Valid card")
    else:
        print(eachnumber + "->" + "Invalid card")
