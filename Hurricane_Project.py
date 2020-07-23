
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II',
         'CubaBrownsville', 'Tampico', 'Labor Day', 'New England',
         'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo',
         'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina',
         'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma',
         'Maria', 'Michael']


months = ['October', 'September', 'September', 'November',
          'August', 'September', 'September', 'September',
          'September', 'September', 'September', 'October',
          'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September',
          'August', 'October', 'September', 'September',
          'July', 'August', 'September', 'October', 'August',
          'September', 'October', 'September', 'September', 'October']


years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953,
         1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005,
         2005, 2007, 2007, 2016, 2017, 2017, 2018]


max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175,
                       175, 160, 160, 175, 160, 175, 175, 190, 185, 160,
                       175, 180, 165, 165, 160, 175, 180, 185, 175, 175,
                       165, 180, 175, 160]

areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'],
                  ['Mexico'], ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'],
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'],
                  ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'],
                  ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'],
                  ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]


damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M',
           'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B',
           '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B',
           '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,
          107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:


def calculate_damage(entry):
    conversion = {"M": 1000000,
              "B": 1000000000}
    if entry != "Damages not recorded":
        length = len(entry)
        number = float(entry[0:length - 1])
        new_entry = number * conversion.get(entry[-1])
    else:
            new_entry = entry
    return new_entry




# write your construct hurricane dictionary function here:

def construct_hurricane_dictionary(names):
    hurricane_info = {}
    num_hurricanes = len(names)
    for index in range(num_hurricanes):
        hurricane_info[names[index]] = {"Names": names[index], "Month": months[index], "Year": years[index],
                                          "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index],
                                          "Damage": calculate_damage(damages[index]), "Death": deaths[index]}
    return hurricane_info

hurricanes_dictionary = (construct_hurricane_dictionary(names))
   




# write your construct hurricane by year dictionary function here:


def hurricanes_by_year(dictionary):
    hurricanes_by_year = dict()
    for cane in dictionary:
        current_year = dictionary[cane]['Year']
        current_cane = dictionary[cane]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_cane]
        else:
            hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year

hurricanes_by_year_dict = (hurricanes_by_year(hurricanes_dictionary))








# write your count affected areas function here:


def count_areas(dictionary):
    area_frequency = dict()
    for cane in dictionary:
        areas = dictionary.get(cane).get("Areas Affected")
        for area in areas:
            if area not in area_frequency:
                area_frequency[area] = 1
            else:
                area_frequency[area] += 1 
    return area_frequency

all_areas = (count_areas(hurricanes_dictionary))









# write your find most affected area function here:

def most_affected_area(dictionary):
    all_areas = count_areas(dictionary)
    most = 0
    locations = all_areas.keys()
    for location in locations:
        current = all_areas.get(location)
        if current > most:
            most = current
            top_dog = location
        else:
            continue
    return top_dog, most


        





# write your greatest number of deaths function here:

def most_deaths(dictionary):
    most = 0
    for cane in dictionary:
        current_cane = dictionary[cane]['Names']
        current_deaths = dictionary[cane]['Death']
        if current_deaths > most:
            most = current_deaths
            top_dog = current_cane
    return top_dog, most




# write your catgeorize by mortality function here:

def add_mortality_scale(dictionary):
    lst_1 = []
    lst_2 = []
    lst_3 = []
    lst_4 = []
    lst_5 = []
    mortality_dict = {1: lst_1, 2: lst_2, 3: lst_3, 4: lst_4, 5: lst_5}
    for cane in dictionary:
        name = dictionary[cane]['Names']
        x = dictionary[cane]['Death']
        if x >= 0 and x < 100:
            lst_1.append(name)
        if x >= 100 and x < 500:
            lst_2.append(name)
        if x >= 500 and x < 1000:
            lst_3.append(name)
        if x >= 1000 and x < 10000:
            lst_4.append(name)
        if x >= 10000:
            lst_5.append(name)
    return mortality_dict

        
            
        



# write your greatest damage function here:

def most_damage(dictionary):
    most = 0
    for cane in dictionary:
        current_cane = dictionary[cane]['Names']
        current_damages = dictionary[cane]['Damage']
        if current_damages == "Damages not recorded":
            continue
        elif current_damages > most:
                most = current_damages
                top_dog = current_cane
    return top_dog, most

print(most_damage(hurricanes_dictionary))





# write your catgeorize by damage function here:

def categorize_by_damages(dictionary):
    lst_0 = []
    lst_1 = []
    lst_2 = []
    lst_3 = []
    lst_4 = []
    lst_5 = []
    damages_dict = {"Damages not recorded" : lst_0 ,1: lst_1, 2: lst_2, 3: lst_3, 4: lst_4, 5: lst_5}
    for cane in dictionary:
        current_name = dictionary[cane]['Names']
        x = dictionary[cane]['Damage']
        if type(x) == str:
            lst_0.append(current_name)
            continue
        if x >= 0 and x < 100000000:
            lst_1.append(current_name)
        if x >= 100000000 and x < 1000000000:
            lst_2.append(current_name)
        if x >= 1000000000 and x < 10000000000:
            lst_3.append(current_name)
        if x >= 10000000000 and x < 50000000000:
            lst_4.append(current_name)
        if x >= 50000000000:
            lst_5.append(current_name)
    return damages_dict


print(categorize_by_damages(hurricanes_dictionary))
            
