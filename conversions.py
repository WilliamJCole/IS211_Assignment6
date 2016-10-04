#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 6"""

def convertCelsiusToKelvin(celsiusFloat):
    return round(celsiusFloat + 273.15, 2)

def convertCelsiusToFahrenheit(celsiusFloat):
    return round((celsiusFloat*9/5) + 32, 2)

def convertFahrenheitToCelsius(fahrenheitFloat):
    return round((fahrenheitFloat-32)*5/9, 2)

def convertFahrenheitToKelvin(fahrenheitFloat):
    return round((fahrenheitFloat+459.67)*5/9, 2)

def convertKelvinToFahrenheit(kelvinFloat):
    return round((kelvinFloat*9/5)-459.67, 2)

def convertKelvinToCelsius(kelvinFloat):
    return round(kelvinFloat-273.15, 2)
