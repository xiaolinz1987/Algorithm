import random

class MyRedPackage:

    def __init__(self, money, people):
        self.money = money
        self.people = people
        self.packages = []

    def divide(self):
        rest_money = self.money
        rest_people = self.people

        for i in range(0, self.people-1):
            temp_money = random.randint(1, int(rest_money/rest_people * 2)-1)
            rest_money -= temp_money
            rest_people -= 1
            self.packages.append(temp_money)
        self.packages.append(rest_money)

    def output(self):
        for package in self.packages:
            print("Money: %.2f" % (package/100))

red_package = MyRedPackage(1000, 10)
red_package.divide()
red_package.output()

