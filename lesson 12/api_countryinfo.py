from countryinfo import CountryInfo as Info
while True:
    country = Info(input('Enter country: ')).info()
    print(f'''
Name : \033[1m{country['name']}\033[0m
Capital : \033[33m{country['capital']}\033[0m
Region : \033[33m{country['region']}\033[0m  
Population : \033[33m{country['population']}\033[0m
Language : \033[33m{country['languages']}\033[0m
TimeZones : \033[33m{country['timezones']}\033[0m
Area : \033[33m{country['area']} km²\033[0m
Wiki : \033[33m{country['wiki']}\033[0m
''')
