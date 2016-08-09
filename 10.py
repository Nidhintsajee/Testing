#For testing test2.py

import test2

total_tests = passed_tests = 0

for symbol in dir(test2):
    attr = getattr(test2, symbol)
    if (callable(attr) and attr.__name__.startswith('test')):
        if attr():
            passed_tests += 1
        total_tests += 1

print 'Total executed tests : '+ str(total_tests)
print 'Total passed tests : '+ str(tests_passed)

