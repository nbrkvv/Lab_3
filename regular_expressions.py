import re

postcode_regex = r'^\w{4,} .{1,}'

ru_postcode_regex = r'^\d{6}$'
usa_postcode_regex = r'^\d{5}$'
uk_postcode_regex = r'^[a-z]{1,2}\d[a-z\d]? \d[a-z]{2}$'
french_postcode_regex = r'^\d{5}$'

def get_region(postcode):
    res = ''
    i = 0
    while(postcode[i] != ' '):
        res += postcode[i]
        i += 1
    return res

def is_valid_postcode(postcode):
    region = get_region(postcode)
    if(region == 'ru'):
        return re.match(ru_postcode_regex, postcode) is not None
    elif(region == 'usa'):
        return re.match(usa_postcode_regex, postcode) is not None
    elif(region == 'uk'):
        return re.match(uk_postcode_regex, postcode) is not None
    elif(region == 'french'):
        return re.match(french_postcode_regex, postcode) is not None
    else:
        return False
    
    
    