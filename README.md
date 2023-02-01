# Budget Manager

Created a reusable module to create new budgets





Here's an example of usage:

```Python
from budget import BudgetManager

myBudget = BudgetManager(3000)
myBudget.add_budget("food",500)
myBudget.add_budget("gas",300)
myBudget.spend("gas",100)
myBudget.spend("food",250)
print(myBudget.available) # prints 2200 (remaining income to budget out)
print(myBudget.budgets) # prints {'food':500, 'gas':300}

```
Using the print_summary method, will print out a similiar formatted table (as the example below) to the terminal displaying the budget and in more easily read format:

|Budget  |  Budgeted|   Spent|  Remaining|
|--------|----------|--------|-----------|
|food|500.00|250.00|250.00|
|gas|300.00|100.00|200.00
|--------|----------|-------|------------|
|Total|800.00|350.00|450.00|

\**This project is part of the *Beginner's Step By Step Coding Course* Book*