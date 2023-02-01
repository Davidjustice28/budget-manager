from budget import BudgetManager


familyBudget = BudgetManager(2500)
familyBudget.add_budget("Groceries",500)
familyBudget.add_budget("Rent",900)
familyBudget.spend("Groceries",35)
familyBudget.spend("Groceries", 15)

familyBudget.print_summary()

familyBudget.change_budget("Rent", 1000)
familyBudget.print_summary()