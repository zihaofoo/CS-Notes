# Comment techniques 
# This is a single line comment.
# Put beside a code to tell others what it is
"""
This is a multi line comment  (1)
This is a multi line comment  (2)
This is a multi line comment  (3)
People start codes with multi-line comment to tell other people what the code does. 
"""

# Variable in Python
"""
Apple = 5.0  --> Apple is the name of a variable.
'=' assigns value to a variable.

Dos and Don'ts
1. Alphabets, numbers and underscores. No spaces are allowed. 
    E.g. yingjie_45 
2. Variable cannot start with a number.
    E.g. 1apple = 50; (ERROR)
    E.g. 22 = 1 (ERROR)    
    E.g. Apple1 is okay.
3. Variables are case sensitive.
    E.g. As1 =/= AS1
"""

# Basic Data Types in Python
"""
4 basic data types
1. Integer
    1, 2, 3, 4 etc. No decimals
    E.g. Var1 = 2 (integer)
    E.g. Var1 = 2.0 (Not an integer)  
    Typecasting: Var1 = int(2.0)    Var1 is now 2
    
2. Float
    1.0, 2.661, 3.1415 (Got decimals)
    E.g. Var1 = 3.3 (float)
    E.g. Var1 = 3 (NOT a float)
    Typecasting:  Var1 = float(3) (FLOAT)   Var1 is now = 3.0
    
3. Boolean (Logic)
    True, False
    E.g. Var1 = True
    Typecasting: bool1 = bool(1)   --> True
                 bool2 = bool(0)   --> False
        
4. String (Character string)
    Enclosed within " " or ' ' 
    E.g. str1 = "Ying jie is smart."
    E.g. str1 = Ying Jie is smart (ERROR)    
    Typecasting: Str1 = str('Hello')
"""

# Operators
"""
Things that act on variables are called operators
1. Mathematical Operators   (returns either int or float)
    * - Multiply
    / - Divide
    + - Add
    - - Subtract
    ** - Exponentiate (power)            E.g. 2 ** 3 = 2 power 3.
    % - Remainder after division         E,g, 13 % 2 = 1
    // - Integer Division                E.g 13 // 2 = 6

2. Logical Operators (returns only boolean, True False data)
    == - Is equals to       E.g. 1 == 1  returns True
    > - Greater than        E.g. 1 > 2  return False
    < - Lesser than         E.g. 1.0 < 1.1 return True
    >= Greater than or equals to
    <= Lesser than or equals to
    != Not equals to        E.g. 3 != 2 return True.    E.g. 2.0 != 2 return True
"""

# Printing and Scanning
"""
1. Printing
Accepts all datatypes. But must have commas between different data types
    E.g. print("The durian is $5.")   Sentence is a string
    E.g. print(Durianprice)        Sentence prints out value of Durianprice
    E.g. Durianprice = 5.0;     print("The durian is $", Durianprice, ".")
    
2. Reading Values
User tells me durian price
Function is input. Always reads a string only. 
Rectify by typecasting

E.g. String input:   Durianprice_today = input("Tell me the price of the Durian \n")
     Float input:    Durianprice_today = float(input("Tell me the price of the Durian \n"))
     Integer input:  Durianprice_today = int(input("Tell me the price of the Durian \n"))
"""

# Conditional Statements
"""
Operates on boolean type

if <boolean condition>:
    <Statements for IF>
elif <boolean condition>:      READ as elseif
    <Statements for elseif>   
else:                        Executes when all IF and ELIF statements fail
    <Statement for ELSE>    
"""