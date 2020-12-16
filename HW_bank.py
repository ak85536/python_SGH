class Customer:
    last_id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __repr__(self):
        return self.__class__.__name__ + "(" + str(
            self.customer_id) + "): " + self.first_name + " " + self.last_name + " (" + self.email + ")"


class Account:
    last_id = 0

    def __init__(self, customer):
        self.customer = customer
        self._balance = 0
        self.interest_rate = 0.05
        Account.last_id += 1
        self.account_id = Account.last_id

    def deposit(self, amount):
        # TODO - add validation to prevent misuse
        if amount <= 0:
            print("The amount to deposit should be a positive number. You entered: " + str(amount))
            return

        self._balance += amount
        print("Deposited: " + str(amount) + ". The new balance is: " + str(self._balance))

    def charge(self, amount):
        # TODO - add validation to prevent misuse
        if amount <= 0:
            print("The amount to charge should be a positive number. You entered: " + str(amount))
            return

        if self._balance < amount:
            print("Sorry, you do not have that much money on your account to withdraw: " + str(amount))
            return

        self._balance -= amount
        print("Charged: " + str(amount) + ". The new balance is: " + str(self._balance))

    def calc_interest(self):
        # TODO - add implementation based on self.interest_rate
        self._balance *= (1 + self.interest_rate)

    def get_balance(self):
        print("The balance is: " + str(self._balance))
        return self._balance

    def __repr__(self):
        return "{0} ({1}): {2} belonging to: {3} {4} ".format(self.__class__.__name__, self.account_id, self._balance,
                                                              self.customer.first_name, self.customer.last_name)
        # return self.__class__.__name__ + "(" +  + ")" + " belonging to: " + self.customer.first_name + " " + self.customer.last_name  + " (" + self.customer.email + ")"


class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def create_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        self.customers.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.accounts.append(a)
        return a

    def transfer(self, acc_id_from, acc_id_to, amount):
        # TODO - implement it (input parameters are account ids)
        if acc_id_from not in self.accounts:
            print("The account from which you are transferring is not valid.")
            return

        if amount <= 0:
            print("The amount to transfer should be a positive number. You entered: " + str(amount))
            return

        amount_from = acc_id_from.get_balance()
        if amount_from < amount:
            print("The account from which you want to transfer has insufficient funds.")
            return

        acc_id_from.charge(amount)
        acc_id_to.deposit(amount)

    def __repr__(self):
        return 'Bank(cust: {0}, acc: {1})'.format(self.customers, self.accounts)


bank = Bank()
bank2 = Bank()

c1 = bank.create_customer("Jan", "Kowalski", "j.kowalski@gmail.com")
c2 = bank.create_customer("Peter", "Jobs", "peter.j@gmail.com")
print(c1)
print(c2)
a1 = bank.create_account(c1)
a2 = bank.create_account(c2)
a3 = bank2.create_account(c2)
print(a1)
print(a2)
a1.deposit(200)

a1.charge(100)
print()

a1.deposit(-10)
a1.get_balance()
print()

a1.charge(-20)
a1.charge(500)
a1.get_balance()
print()

a1.calc_interest()
a1.calc_interest()
a1.calc_interest()
a1.get_balance()
a2.get_balance()
print()

bank.transfer(a1, a2, 50)
a1.get_balance()
a2.get_balance()
print()

bank.transfer(a1, a2, -3150)
a1.get_balance()
a2.get_balance()
print()

bank.transfer(a1, a2, 9990)
a1.get_balance()
a2.get_balance()
print()

a3.deposit(500)
bank.transfer(a3, a1, 50)
a1.get_balance()
a3.get_balance()
print()
