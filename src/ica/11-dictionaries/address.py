betsy_info = {'Name': 'Betsy Foobar',
              'Phone': 'x8012',
              'Street': '1600 Grand Avenue',
              'City': 'Saint Paul',
              'State': 'MN',
              'Email': 'bfoobar@macalester.edu'}

tom_info = {'Name': 'Tom Riddle',
            'Phone': 'x8512',
            'Street': '1600 Grand Avenue',
            'City': 'Saint Paul',
            'State': 'MN',
            'Email': 'triddle@macalester.edu'}
address_book = [ betsy_info, tom_info,
                {'Name': 'Susan Fox',
                 'Phone': 'x6553',
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'},
                 {'Name': 'Apiu',
                  'Phone':'802302',
                  'Street':'345 Main Street',
                  'City':'Minneapolis',
                  'State':'MN',
                  'Email':'apiu@gmail.com'},
                 {'Name':'Helen',
                  'Phone':'54823975',
                  'Street':'2500 College Street',
                  'City':'San Francisco',
                  'State':'CA',
                  'Email':'hlevy@gmail.com'}]
print(address_book)

def filter_by_city(city_name,address_book):
    newlist=[]
    for info in address_book:
        if info['City'] == city_name:
            newlist.append(info)
    return newlist

print(filter_by_city('Saint Paul',address_book))