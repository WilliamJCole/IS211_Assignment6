import conversions as con

#TEST FOR convertCelsiusToKelvin()
print "TEST FOR convertCelsiusToKelvin()"
tests = [(500.00, 773.15), (490.00, 763.15), (450.00, 723.15), (410.00, 683.15), (380.00, 653.15)]
for i, o in tests:
    c = con.convertCelsiusToKelvin(i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convertCelsiusToFahrenheit()"
#TEST FOR convertCelsiusToFahrenheit()
tests = [(500.00, 932.00), (490.00, 914.00), (450.00, 842.00), (410.00, 770.00), (380.00, 716.00)]
for i, o in tests:
    c = con.convertCelsiusToFahrenheit(i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convertFahrenheitToCelsius()"
#TEST FOR convertFahrenheitToCelsius()
tests = [(500.00, 932.00), (490.00, 914.00), (450.00, 842.00), (410.00, 770.00), (380.00, 716.00)]
for o, i in tests:
    c = con.convertFahrenheitToCelsius(i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convertFahrenheitToKelvin()"
#TEST FOR convertFahrenheitToKelvin()
tests = [(932.00, 773.15), (914.00, 763.15), (842.00, 723.15), (770.00, 683.15), (716.00, 653.15)]
for i, o in tests:
    c = con.convertFahrenheitToKelvin(i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convertKelvinToFahrenheit()"
#TEST FOR convertKelvinToFahrenheit()
tests = [(932.00, 773.15), (914.00, 763.15), (842.00, 723.15), (770.00, 683.15), (716.00, 653.15)]
for o, i in tests:
    c = con.convertKelvinToFahrenheit(i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""


print "TEST FOR convertKelvinToCelsius()"
#TEST FOR convertKelvinToCelsius()
tests = [(500.00, 773.15), (490.00, 763.15), (450.00, 723.15), (410.00, 683.15), (380.00, 653.15)]
for o, i in tests:
    c = con.convertKelvinToCelsius(i)
    if o==c:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST PASS"%(i, o, c)
    else:
        print "Input given: %.2f | Expected output: %.2f | Resultant output: %.2f | TEST FAIL"%(i, o, c)

print ""

