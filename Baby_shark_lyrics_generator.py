"""
Create a function, as short as possible, that returns this lyrics.
Your code should be less than 300 characters.

Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt!
Run away,…
Good Luck!
"""

def baby_shark_lyrics():
  b = ' shark'
  a = {'Baby': b,'Mommy': b,'Daddy': b,'Grandma': b,'Grandpa': b,'Let\'s go hunt': ''}
  c = ''
  for k,v in a.items():
    c += '{}{},{}\n'.format(k, v, ' doo'*6)*3
    c += '{}{}!\n'.format(k,v)
  c += 'Run away,…'
  return c
      
    

"""
This is a solution done by serguma on CodeWars and modified by kaizenhwk
"""