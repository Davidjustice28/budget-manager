    
class BudgetManager:
    def __init__(self,amount): 
        self.available = amount
        self.budgets = {}
        self.expenditure = {}


    def add_budget(self,name,amount):
        if name in self.budgets:
            raise ValueError("Budget exists")
        if amount > self.available:
            raise ValueError("Insufficient funds")
        self.budgets[name] = amount
        self.available -= amount
        self.expenditure[name] = []
        # print(self.available, "is available in budget")
        return self.available

    def change_budget(self,name,new_amount):
        if(name not in self.budgets):
            raise ValueError("No budget exists to update")
        old_amount = self.budgets[name]
        if(new_amount > old_amount + self.available):
            raise ValueError("Insufficent funds")
        self.budgets[name] = new_amount
        if new_amount > old_amount:
            self.available -= new_amount - old_amount
        else:
            self.available += old_amount - new_amount
        return self.available
        

    def spend(self,name,amount):
        if name not in self.expenditure:
            raise ValueError("No such budget")
        self.expenditure[name].append(amount)
        budgeted = self.budgets[name]
        spent = sum(self.expenditure[name])
        return budgeted - spent

    def print_summary(self):
        print("Budget            Budgeted      Spent  Remaining")
        print("--------------- ---------- ---------- ----------")
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = sum(self.expenditure[name])
            remainder = budgeted - spent
            print(f"{name:15s} {budgeted:10.2f} {spent:10.2f} {remainder:10.2f}")
            total_budgeted += budgeted
            total_spent += spent
            total_remaining += remainder
        print("--------------- ---------- ---------- ----------")
        print(f'{"Total":15s} {total_budgeted:10.2f} {total_spent:10.2f} {total_budgeted - total_spent:10.2f}')