class Class1:
    def __init__(self):
        self.var1 = 122
        self.var2 = 2

    def show_var1(self):
        print(self.var1)
        # branch 1 modifications
        print('test 1 branch 1 modifications')
        print('test 2 branch 1 modifications')
        print('late change that I want to have included in the "Corrected Description" commit')
        print('late change that I want to have included in the "Corrected Description" commit')
        print('late change that I want to have change included in the "Corrected Description" commit')
        print('late change that I want to have included in the "Corrected Description" commit class1_module.py:14')
        print('late change that I want to have included in the "Corrected Description" commit ')

    def flowrate (self, q:'flow, m3', t:'time period, h') -> 'flowrate, m3/h':
        print(locals())
        return q/t

c1 = Class1()
print(c1.flowrate.__annotations__['return'])
print(c1.flowrate(4, 7))


