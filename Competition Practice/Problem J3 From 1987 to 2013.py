# This program calculates the first distinct year from user input using strings.

def distinct(year):
    
    year_str = str(year)
    
    if year > 999:
        
       if year_str [0] == year_str [1]:
           return False
       if year_str [0] == year_str [2]:
           return False
       if year_str [0] == year_str [3]:
           return False
       if year_str [1] == year_str [2]:
           return False
       if year_str [1] == year_str [3]:
           return False
       if year_str [2] == year_str [3]:
           return False
        
        
    if year > 99:
       
        if year_str [0] == year_str [1]:
            return False
        if year_str [0] == year_str [2]:
            return False
        if year_str [1] == year_str [2]:
            return False
        
        
        
    if year > 9:
        
         if year_str [0] == year_str [1]:
             return False
        
    return True
            
        
year = int(input("Enter a year"))

year += 1


while distinct(year) == False:
    year += 1
    
print year
