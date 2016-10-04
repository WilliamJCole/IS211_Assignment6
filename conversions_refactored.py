#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 6"""

class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    temp = ["celsius", "fahrenheit", "kelvin"]
    #There is a separate way of converting temperature
    anyToCelsius = ["value", "(value-32)*5/9", "value-273.15"]
    celsiusToAny = ["value", "(value*9/5)+32", "value+273.15"]

    dist = ["meters", "miles", "yards"]
    #The way to convert distances
    anyTOMeters = ["value", "value/0.00062137", "value/1.0936"]
    meterToAny = ["value", "value*0.00062137", "value*1.0936"]

    if fromUnit.lower() in temp:
        if not(toUnit.lower() in temp):
            raise ConversionNotPossible
        else:
            #Valid temperature conversion request received
            try:
                value = float(value)
            except:
                raise ConversionNotPossible
            else:
                value = eval(anyToCelsius[temp.index(fromUnit.lower())])
                value = eval(celsiusToAny[temp.index(toUnit.lower())])
                return round(value, 2)

    elif fromUnit.lower() in dist:
        if not(toUnit.lower() in dist):
            raise ConversionNotPossible
        else:
            #Valid distance conversion request received
            try:
                value = float(value)
            except:
                raise ConversionNotPossible
            else:
                value = eval(anyTOMeters[dist.index(fromUnit.lower())])
                value = eval(meterToAny[dist.index(toUnit.lower())])
                return round(value, 2)
    else:
        #Wrong input parameters
        raise ConversionNotPossible
