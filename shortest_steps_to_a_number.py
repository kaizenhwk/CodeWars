"""
Summary:
Given a number, num, return the shortest amount of steps it would take from 1, to land exactly on that number.

Description:
A step is defined as:

Adding 1 to the number: num += 1
Doubling the number: num *= 2
You will always start from the number 1 and you will have to return the shortest count of steps it would take to land exactly on that number.

1 <= num <= 10000

Examples:

num == 3 would return 2 steps:

1 -- +1 --> 2:        1 step
2 -- +1 --> 3:        2 steps

2 steps
num == 12 would return 4 steps:

1 -- +1 --> 2:        1 step
2 -- +1 --> 3:        2 steps
3 -- x2 --> 6:        3 steps
6 -- x2 --> 12:       4 steps

4 steps
num == 16 would return 4 steps:

1 -- +1 --> 2:        1 step
2 -- x2 --> 4:        2 steps
4 -- x2 --> 8:        3 steps
8 -- x2 --> 16:       4 steps

4 steps
"""
"""
Test.it("Simple Tests")
Test.assert_equals(shortest_steps_to_num(1), 0);
Test.assert_equals(shortest_steps_to_num(12), 4);
Test.assert_equals(shortest_steps_to_num(16), 4);
Test.assert_equals(shortest_steps_to_num(71), 9);
"""

def shortest_steps_to_num(num):
    # Good Luck!
    count = 0
    while num > 1:
	    if num % 2 == 0:             
		    num = num // 2
	    else:
		    num = num - 1              
	    count += 1
    return count
    pass
"""
Found a code online and modified it to get this
"""

"""
Best:
def shortest_steps_to_num(num):
    return num.bit_length() + bin(num).count('1') - 2
"""
"""
Liked:
def shortest_steps_to_num(num):
    steps = 0
    
    while num != 1:
        if num % 2:
            num -= 1
        else:
            num //= 2
        
        steps += 1
    
    return steps
"""