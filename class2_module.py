class Class2:
    def __init__(self):
        self.var1 = 999
        self.var2 = 56

    def show_var1(self):
        print(self.var1)
        print('late change that I want to have included in the "Corrected Description" commit')
    def show_var2(self):
        print(self.var2)
        print('this function was added by mistake to master branch')

