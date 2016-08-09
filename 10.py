#For testing test2.py

import test2

total_tests = 0
tests_passed = 0

for symbol in dir(test2):
    attr = getattr(test2, symbol)
    if (callable(attr) and attr.__name__.startswith('test')):
        if attr():
            tests_passed += 1
        total_tests += 1

print 'Executed %d tests' % total_tests
print 'Total tests passed = %d' % tests_passed

