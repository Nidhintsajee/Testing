#Modified
#For testing any program

pgm=raw_input("Enter name of file to be Tested:")
import pgm

total_tests = passed_tests = 0

for symbol in dir(pgm):
    attr = getattr(pgm, symbol)
    if (callable(attr) and attr.__name__.startswith('test')):
        if attr():
            passed_tests += 1
        total_tests += 1

print 'Total executed tests : '+ str(total_tests)
print 'Total passed tests : '+ str(tests_passed)

