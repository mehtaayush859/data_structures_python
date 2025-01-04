"""
    Dictionaries

Operations of dict-
1. Clear()
	It clears all the keys and values in the dictionaries.

2. Copy()
	It copies all the key and value pair into it and make a new dictionaries.

3. Values()
	It generally gives the value of the present keys which is present into dictionaries.

4. Update()
	It gives the updates which are made to the dictionaries.

5.Get()
	It is the most important which gives the value of keys accordingly.

6. Items()
	It is also an important method which actually gives the tuple of the key and value pair which 	are in the dictionary..!!

7. Keys()
	It provides the all keys present in the dictionary.

8. pop()
	It pops out the specified key into the tuples in output.

9. popitem()
	It provides both key and value in the output as a tuple.

10. setdefault()
	It actually gives the value of the key specified in the dictionary.

"""

#Practice
from webbrowser import BackgroundBrowser
import pandas as pd
a = {
    'key1':'ABC',
    'key2':'PQR',
    'key3':'XYZ',

}

b = a.copy()

#print(a.setdefault('key4'))
#print(a.get('key1'))

"""
    Constructor of Dict
"""

#my_dict = dict(key1 = 'q' , key2 ='w')
#print(my_dict)

# !-- Nested dict --!

squad = {'Batsmen' :{'Rohit Sharma' : {'Matches' : 10,
                                         'Runs' : 8010,
                                         'Avg' : 47.4},
                    'Shikar Dhawan' : {'Matches' : 20,
                                         'Runs' : 4510,
                                         'Avg' : 41.4},

                    'Virat Kohli'   : {'Matches' : 30,
                                         'Runs' : 6710,
                                         'Avg' : 22.4},

                    },
        'Bowler'    :{'Bhuvi' : {'Matches' : 63,
                                 'Wickets' : 25},
                     'Yuzi' : {'Matches' : 23,
                                 'Wickets' : 45}

        }
        
    }


#print(squad['Bowler'])
pd1 = pd.DataFrame(squad['Batsmen']['Rohit Sharma'], index=[0])
print(pd1)

print('\n')
d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key])



print("\n")

x = {'jack' :40 , 'vd':90 }
del x
print("\n")


numbers= {}
comb={}
letters = {}

numbers[2] = 10
numbers[3] = 9
letters[5] = 'A'

comb['Numbers'] = numbers
comb['Letters'] = letters

print(comb)
print("\n")

x= {}
x[3] = 2
x[2] = [3,4,5]

print(x[2][2])