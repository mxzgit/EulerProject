def convertIntToRomain(inputint):
    dictIntToRomain = {
        1000 : 'M', 500 : 'D', 100 : 'C',  50 : 'L', 11 : 'XI',  10 : 'X', 9 : 'IX', 5 : 'V', 4 : 'IV', 1 : 'I'
    }

    stringOutput = ""

    for element in dictIntToRomain:
        q = int(inputint/element)
        r = int(inputint%element)
        stringOutput  = stringOutput + q*dictIntToRomain[element]
        ##print(stringOutput)
        if q:
            inputint = r

    return stringOutput

print(convertIntToRomain(298))