"""
Print table of 2 in following format using For loop.
Expected Output: 
Prod-1=2 
Prod-2=4 
. . . 
Prod-10=20

"""

n = 2
rng = 10
nt = 0
for i in range(1,rng+1):
  nt = 2 * i
  print(f"Prod - {i} = {nt}")
