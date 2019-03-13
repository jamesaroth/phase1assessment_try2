## Byte Academy Phase 1 Assessment

You can use any source of information that is not a human being. 70% is a passing score. Good luck!

#### Question 1: API to json

* Write a program that asks the user to input a stock ticker symbol. The program should download the chart data for that stock from IEX <https://iextrading.com/developer/docs/#chart> and save that data to a json file called "SYMBOL_chart.json" where SYMBOL is the stock ticker's symbol (tsla_chart.json, aapl_chart.json, etc.)

#### Question 2: Sum Grid & Grid Reversed

* Write a program that finds the sum of all values in grid.csv

* Write a program that writes a new csv called flipgrid.csv where the rows and
columns of grid.csv are reversed. That is this csv:
```
1,2,3,4,5
6,7,8,9,10,
11,12,13,14,15
```

would produce: 
```
15,14,13,12,11
10,9,8,7,6
5,4,3,2,1
```

#### Question 3: Database

* Using python's sqlite3 module write a schema.py file that creates two database tables modeling the following:

    * Branch: A branch has a city, a state, and a zip code

    * Employee: An employee has a first name, a last name, an employee ID, and a salary

    * A branch has many employees, an employee works at one branch

Using INSERT statements in a seed.py file create two branches with four 
employees each using the following data:

```
# Flushing, NY 11368 branch has:

last name, first name, employee ID, salary

Lockett, Walker, S000000001, $45000
Coleman, Casey, S000000002, $70000
Kilome, Franklyn, S000000003, $67000
Santiago, Hecton, S000000004, $100000

# Houston, TX 77002 branch has:

last name, first name, employee ID, salary

Valdez, Framber, S000000005, $39000
Peacock, Brad, S000000006, $51000
Guduan, Reymin, S000000007, $67000
Cole, Gerrit, S000000008, $55000
```

Write a SQL UPDATE statement to change Reymin Guduan's salary to 73000

Write a SQL SELECT statement to select all employees in New York that make over 70000 a year

#### Question 4 & 5: Terminal Trader API Key

##### This question counts double

* Modify your Terminal Trader so that accounts have an `api_key` column. This should be a random string of numbers and/or letters that is 15 characters long. Accounts should receive them when a new account is created. The new code should be in the Account class. For the purposes of the assessment, you CAN rely on the fact that a 1 in a quadrillion (literally) chance of two accounts having the same random key is unlikely to occur.

* Add a new option to your main menu (the menu after the user logs in) where the user can view their `api_key`. You don't need to give them the ability to generate a new one. 

* Create a class method called `api_authenticate` that returns the Account object that has a given api key. If 'a89077098a' is the api key for user mikebloom, then `Account.api_authenticate('a89077098a')` should return that user as an Account object. If api_authenticate is given an api key that is not in the database, it should return `None.`

#### Submission

* Create a new repository on github and push your work to it, submit the link. Do not post to the group chat, send the link in a private message.

* Proper submission is a bonus half-question

#### Good luck, you can do it!

* Thanks for a great phase 1!
