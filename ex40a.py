personDict= {"Remus":"Mocanu","John":"Doe"}


class Employee:

    salary = 25000

    def __init__(self, firstName, lastName):
        self.fName = firstName
        self.lName  = lastName

    def __str__(self):
        return 'First Name : %s , Last Name: %s' % (self.fName, self.lName)
