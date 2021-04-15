
class Budget:
    """"
        This is the Budget class. It helps to create objects that can create funds allocation
        in different categories for user.

        Attributes
       ------------
        balance: float|int
            Total funds that the user has.

        name: string
            the name of the user. Defaults to None.

        food_balance: float|int
            Stores the balance of funds allocated for food by the user

        entertainment_balance: float|int
            Stores the balance of fund allocated for entertainment by the user

        clothing_balance: float|int
            Stores the balance of fund allocated for clothing by the user

        HOW IT WORKS:
       --------------
            tunde = Budget('Tunde')
            tunde.deposit(23.12, 'clothing')
            tunde.deposit(34.16, 'entertainment')
            tunde.withdraw(14, 'clothing')
            tunde.transfer(20.13, 'entertainment', 'clothing')
            tunde.category_balance()


            ₦23.12 deposited to clothing category.
            ₦34.16 deposited to entertainment category.
            ₦14 withdrawn from clothing category.
            ₦20.13 withdrawn from entertainment category.
            ₦20.13 deposited to clothing category.
            Tunde has the following balances:"
                        food:   ₦0,
                        clothing: ₦29.25,
                        entertainment: ₦14.03
                    TOTAL: ₦43.28
    """

    balance = 0

    def __init__(self, name=None):
        self.name = name
        self.food_balance = 0
        self.entertainment_balance = 0
        self.clothing_balance = 0

    def deposit(self, amount, category):
        """
        A method of the Budget class that is used to add funds to a specific category

            :param amount: The amount to be added.
            :type amount: int|float

            :param category: The specific category the fund is added to.
            :type category: string
        """

        if category in ['food', 'clothing', 'entertainment']:
            if category == 'food':
                self.food_balance += amount
            elif category == 'clothing':
                self.clothing_balance += amount
            else:
                self.entertainment_balance += amount

            print('₦{} deposited to {} category.'.format(amount, category))
            self.balance += amount
            return
        else:
            print("Enter one of 'food, clothing or entertainment' as the category")
            return

    def withdraw(self, amount, category):
        """
        A method of the Budget class that is used to remove funds from a specific category

            :param amount: The amount to be removed.
            :type amount: int|float

            :param category: The specific category the fund is removed from.
            :type category: string
        """

        if category in ['food', 'clothing', 'entertainment']:
            if category == 'food':
                if amount > self.food_balance:
                    print("Amount too much. Your food balance is ₦{}".format(round(self.food_balance, 2)))
                    return False
                self.food_balance -= amount
            elif category == 'clothing':
                if amount > self.clothing_balance:
                    print("Amount too much. Your clothing balance is ₦{}".format(round(self.clothing_balance, 2)))
                    return False
                self.clothing_balance -= amount
            else:
                if amount > self.entertainment_balance:
                    print("Amount too much. Your entertainment balance is"
                          " ₦{}".format(round(self.entertainment_balance, 2)))
                    return False
                self.entertainment_balance -= amount

            self.balance -= amount
            print('₦{} withdrawn from {} category.'.format(amount, category))
            return True

        else:
            print("Enter one of 'food, clothing or entertainment' as the category")
            return

    def transfer(self, amount, from_category, to_category):
        """
        A method of the Budget class that is used to transfer/move funds to a specific category
        to another category.

            :param amount: The amount to be transferred.
            :type amount: int|float

            :param from_category: The specific category the fund is removed from.
            :type from_category: string

            :param to_category: The category the fund is move to
            :type to_category: string
        """

        if not self.withdraw(amount, from_category):
            return

        self.deposit(amount, to_category)

    def category_balance(self):
        """
        A method of the Budget class that is used to compute category balances
        """
        print("""{} has the following balances:"
            food:   ₦{},
            clothing: ₦{},
            entertainment: ₦{}
        TOTAL: ₦{}""".format(self.name or 'No Name',
                             round(self.food_balance, 2),
                             round(self.clothing_balance, 2),
                             round(self.entertainment_balance, 2),
                             round(self.balance, 2)))
