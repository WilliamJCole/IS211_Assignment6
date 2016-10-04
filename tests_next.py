import conversions_refactored as con

#TEMPERATURE CONVERSION TESTS--------------------------------------------------------------------------------------
#TEST FOR convert Celsius To Kelvin
print "TEST FOR convert Celsius To Kelvin"
tests = [(500.00, 773.15), (490.00, 763.15), (450.00, 723.15), (410.00, 683.15), (380.00, 653.15)]
for i, o in tests:
    c = con.convert("Celsius", "Kelvin", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convert Celsius To Fahrenheit"
#TEST FOR convert Celsius To Fahrenheit
tests = [(500.00, 932.00), (490.00, 914.00), (450.00, 842.00), (410.00, 770.00), (380.00, 716.00)]
for i, o in tests:
    c = con.convert("Celsius", "Fahrenheit", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convert Fahrenheit To Celsius"
#TEST FOR convert Fahrenheit To Celsius
tests = [(500.00, 932.00), (490.00, 914.00), (450.00, 842.00), (410.00, 770.00), (380.00, 716.00)]
for o, i in tests:
    c = con.convert("Fahrenheit", "Celsius", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR conver tFahrenheit To Kelvin"
#TEST FOR convert Fahrenheit To Kelvin
tests = [(932.00, 773.15), (914.00, 763.15), (842.00, 723.15), (770.00, 683.15), (716.00, 653.15)]
for i, o in tests:
    c = con.convert("Fahrenheit", "Kelvin", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convert Kelvin To Fahrenheit"
#TEST FOR convert Kelvin To Fahrenheit
tests = [(932.00, 773.15), (914.00, 763.15), (842.00, 723.15), (770.00, 683.15), (716.00, 653.15)]
for o, i in tests:
    c = con.convert("Kelvin", "Fahrenheit", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convert Kelvin To Celsius"
#TEST FOR convert Kelvin To Celsius
tests = [(500.00, 773.15), (490.00, 763.15), (450.00, 723.15), (410.00, 683.15), (380.00, 653.15)]
for o, i in tests:
    c = con.convert("Kelvin", "Celsius", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""

#END OF TEMPERATURE TESTS---------------------------------------------------------------------------------------

print "-------------------------------------------------------------------------------\n"

#DISTANCE CONVERSION TESTS--------------------------------------------------------------------------------------
print "TEST FOR convert meters to miles"
#TEST FOR convert meters to miles
tests = [(0.48, 773.15), (0.47, 763.15), (0.45, 723.15), (0.42, 683.15), (0.41, 653.15)]
for o, i in tests:
    c = con.convert("meters", "miles", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convert meters to Yards"
#TEST FOR convert meters to Yards
tests = [(845.52, 773.15), (834.58, 763.15), (790.84, 723.15), (747.09, 683.15), (714.28, 653.15)]
for o, i in tests:
    c = con.convert("meters", "Yards", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convert miles to meters"
#TEST FOR convert miles to meters
tests = [(0.48, 772.49), (0.47, 756.39), (0.45, 724.21), (0.42, 675.93), (0.41, 659.83)]
for i, o in tests:
    c = con.convert("miles", "meters", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convert miles to Yards"
#TEST FOR convert miles to Yards
tests = [(0.48, 844.79), (0.47, 827.19), (0.45, 791.99), (0.42, 739.19), (0.41, 721.59)]
for i, o in tests:
    c = con.convert("miles", "Yards", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convert Yards to meters"
#TEST FOR convert Yards to meters
tests = [(772.49, 844.79), (756.39, 827.19), (724.20, 791.99), (675.92, 739.19), (659.83, 721.59)]
for o, i in tests:
    c = con.convert("Yards", "meters", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convert Yards to miles"
#TEST FOR convert Yards to miles
tests = [(0.48, 844.79), (0.47, 827.19), (0.45, 791.99), (0.42, 739.19), (0.41, 721.59)]
for o, i in tests:
    c = con.convert("Yards", "miles", i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


#END DISTANCE CONVERSION TEST---------------------------------------------------------------

print "-------------------------------------------------------------------------------\n"

#SAME UNIT TYPE CONVERSION------------------------------------------------------------
tests = [10.00, 10.00]

print "celsius to celsius"
c = con.convert("celsius", "celsius", tests[0])
if tests[1]==c:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(tests[0], tests[1], c)
else:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(tests[0], tests[1], c)
print ""

print "fahrenheit to fahrenheit"
c = con.convert("fahrenheit", "fahrenheit", tests[0])
if tests[1]==c:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(tests[0], tests[1], c)
else:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(tests[0], tests[1], c)
print ""

print "kelvin to kelvin"
c = con.convert("kelvin", "kelvin", tests[0])
if tests[1]==c:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(tests[0], tests[1], c)
else:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(tests[0], tests[1], c)
print ""

print "meters to meters"
c = con.convert("meters", "meters", tests[0])
if tests[1]==c:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(tests[0], tests[1], c)
else:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(tests[0], tests[1], c)
print ""

print "miles to miles"
c = con.convert("miles", "miles", tests[0])
if tests[1]==c:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(tests[0], tests[1], c)
else:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(tests[0], tests[1], c)
print ""

print "yards to yards"
c = con.convert("yards", "yards", tests[0])
if tests[1]==c:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(tests[0], tests[1], c)
else:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(tests[0], tests[1], c)
print ""

#END SAME UNIT TYPE CONVERSION------------------------------------------------------------

print "-------------------------------------------------------------------------------\n"

#INCOMPATIBLE UNIT TYPE CONVERSION-------------------------------------------------------
tests = [10.00, 10.00]

print "celsius to yards"
c = con.convert("celsius", "yards", tests[0])
if tests[1]==c:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(tests[0], tests[1], c)
else:
    print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(tests[0], tests[1], c)
print ""
