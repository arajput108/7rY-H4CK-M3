Using "if statements" allows programs to make decisions. They let a program chose a decision based on a 
condition. Below is an example of how an if statement can be used to determine the section of code 
(which print statement) to use.

Example:
if age < 17:
    print('You are NOT old enough to drive')
else:
    print('You are old enough to drive')

In the example, if you are younger than 17, the program will output the text "You are NOT old enough to drive"; 
however, if you are over the age of 17, the program will output "You are old enough to drive". Depending on a 
condition (in this example, it's the age variable), the program will run different code sections.

There are some key components we note from our code example above:

1.) The if keyword indicates the beginning of the if statement, followed by a set of conditions.

2.) The if statement is only run if the condition (or sets of conditions) is true. In our example, 
it's age < 17; if that condition is true (age is below 17), the code within the if statement runs. 
Per the example, if certain conditions are not met, the program can default to running code shown in 
the else part of the if statement. 

3.) A colon : marks the end of the if statement.

4.) Note the indentation. Anything after the colon that is indented, is considered part of the if statement, 
which the program will execute.




Answer the questions below: 

1.) Once you've written the application in the code editor's shipping.py tab, a flag will appear, 
    which is the answer to this question.
Code:
    customer_basket_cost = 34
    customer_basket_weight = 44

    # Write if statement here to calculate the total cost
    shipping_cost = 0
    if customer_basket_cost>=100:
     shipping_cost=0
    else:
     shipping_cost = customer_basket_weight * 1.2
    total_cost = shipping_cost + customer_basket_cost
    print(total_cost)


    Flag is: THM{IF_STATEMENT_SHOPPING}
    Code O/p: 86.8

2.) In shipping.py, on line 12 (when using the Code Editor's Hint), change the customer_basket_cost 
    variable to 101 and re-run your code. You will get a flag (if the total cost is correct based on your code); 
    the flag is the answer to this question.
Code:
    customer_basket_cost = 101
    customer_basket_weight = 44

    # Write if statement here to calculate the total cost
    shipping_cost = 0
    if customer_basket_cost>=100:
     shipping_cost=0
    else:
     shipping_cost = customer_basket_weight * 1.2
    total_cost = shipping_cost + customer_basket_cost
    print(total_cost)

    The flag is: THM{MY_FIRST_APP}
    Code O/p: 101   