Logical operators allow assignment and comparisons to be made and are used in conditional 
testing (such as if statements).

Logical Operation	                             Operator	                           Example
Equivalence	                                        ==	                              if x == 5
Less than	                                        <	                              if x < 5
Less than or equal to	                            <=	                              if x <= 5
Greater than	                                    >	                              if x > 5
Greater than or equal to	                        >=	                              if x >= 5

Boolean operators are used to connect and compare relationships between statements. 
Like an if statement, conditions can be true or false.

Boolean Operation	                             Operator                           Example
1.) Both conditions must be                        AND                         if x >= 5 AND x <= 100
    true for the statement 	                                                     Returns TRUE if x is
     to be true.                                                               a number between 5 and 100

2.) Only one condition of the                      OR                            if x == 1 OR x == 10
    statement needs to be true                                                Returns TRUE if X is 1 or 10

3.) If a condition is the opposite                NOT                             if NOT y
    of an argument                                                           Returns TRUE if the y value is False 


Let's look at a few Python code examples:

a = 1
if a == 1 or a > 10:
     print("a is either 1 or above 10")
     

name = "bob" 
hungry = True
if name == "bob" and hungry == True:
     print("bob is hungry")
elif name == "bob" and not hungry:
     print("Bob is not hungry")
else: # If all other if conditions are not met
     print("Not sure who this is or if they are hungry") 

 	



	


