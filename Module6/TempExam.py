from functions2 import readTemps
from functions2 import getAverages
from functions2 import countHotCold

def main():
    
    # temps should be list of dictionaries containing the
    # high and low temperaturs for each day (line)
    # in the specified file, the keys for each item 
    # in the dictionary should be 'high' and 'low'.
    # NOTE the temps should be integers.
    # example: [ {'high': 67, 'low': 49}, {'high': 72, 'low': 56} ]
    temps = readTemps("temps1.txt")
    print("Part 1: \n %s \n" % temps)
    
    print(len(temps))
    print(temps[3])
    print(temps[7])
    
    # averages should be a list containing the average
    # temperature on each day (line) in the file.
    # example: [53, 63, 69, 48]
    averages = getAverages(temps)
    print("Part 2: \n %s \n" % averages)
    
    # hotCold should be a single dictionary contining 
    # the number of days (lines) in which the high temperature
    # was >= 70 and the number of days (lines) in which the low
    # temperature was <= 50, ther keys for this dictionary should
    # be 'hot' and 'cold'.
    # example: {'hot': 4, 'cold': 7}
    hotCold = countHotCold(temps)
    print("Part 3: \n %s \n" % hotCold)    

main()
    
