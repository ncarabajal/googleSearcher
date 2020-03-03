#!/usr/bin/env python3

import random
import googlesearch

wordlist = ['quicksort', 'binary', 'flood fill', 'dfs', 'bfs', 'hex', ]

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

query = random.choice(wordlist) + " python" 

print(query) 

for j in search(query, tld="co.in", num=20, stop=10, pause=2): 
    print(j) 