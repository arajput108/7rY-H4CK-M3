As programs start to get bigger and more complex, some of your code will be repetitive, writing the 
same code to do the same calculations, and this is where functions come in. A function is a block of 
code that can be called at different places in your program.

You could have a function to work out a calculation such as the distance between two points on a map 
or output formatted text based on certain conditions. Having functions removes repetitive code, as the 
function's purpose can be used multiple times throughout a program.
Example:
        def sayHello(name):
             print("Hello " + name + "! Nice to meet you.")

        sayHello("ben") # Output is: Hello Ben! Nice to meet you

There are some key components we can note from this function:

1.) The def keyword indicates the beginning of a function. The function is followed by a name that the 
    programmer defines (and is a function parameter). In our example, it's sayHello.
2.) Following the function name is a pair of parenthesis () that holds input values, data that we can 
    pass into the function. In our example, it's a name.
3.) A colon : marks the end of the function header.

In the function, notice the indentation. Similar to if statements, anything after the colons that is 
indented is considered part of the function.

A function can also return a result, see the code block below:

def calcCost(item):
     if(item == "sweets"):
          return 3.99
     elif (item == "oranges"):
          return 1.99
     else:
          return 0.99

spent = 10
spent = spent + calcCost("sweets")
print("You have spent:" + str(spent))

If we call the calcCost function and pass in "sweets" as the item parameter, the function will return a 
decimal number (float). In the code above, we take a variable called spent and add the cost of "sweets" 
through the calcCost function; when we call calcCost, it will return the number 3.99.

Answer the questions below: 
You've invested in Bitcoin and want to write a program that tells you when the value of Bitcoin falls 
below a particular value in dollars.

In the code editor, click on the bitcoin.py tab. Write a function called bitcoinToUSD with two 
parameters: bitcoin_amount, the amount of Bitcoin you own, and bitcoin_value_usd, the value of bitcoin in USD. 
The function should return usd_value, which is your bitcoin value in USD (to calculate this, in the function, 
you times bitcoin_amount variable by bitcoin_value_usd variable and return the value). The start of the function 
should look like this:
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):

1.) Once you've written the bitcoinToUSD function, use it to calculate the value of your Bitcoin in USD, and 
then create an if statement to determine if the value falls below $30,000; if it does, output a message to 
alert you (via a print statement).
#<---------------------Code------------------>
"""
    In this project, you'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000, print a message.

    You can assume that 1 Bitcoin is worth $40,000

"""

investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

# 1) write a function to calculate bitcoin to usd

# 2) use function to calculate if the investment is below $30,000

#<---------------------Main-Code---------------------->

def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
 usd_value= bitcoin_amount * bitcoin_value_usd
 return usd_value
answer = bitcoinToUSD(1.2,40000)
if answer <= 30000:
 print(alert)

2.) 1 Bitcoin is now worth $24,000. In the code editor on line 14, update the bitcoin_to_usd variable value 
    to 24000 and see if your Python program recognises that your investment is below the $30,000 threshold.