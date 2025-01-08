# a) Nick Blexrud 
# b) status = Complete 
# c) This program asks the end user for a month, a day, and a two digit year. It then determines whether the 
# month multiplied by the day equals the year, if it does equal the year it says 'magic' otherwise it will say
# 'not magic'

# for every input, cast string to int
month = int(input("Enter a month (in numeric form): "))
day = int(input("Enter a day (in numeric form): "))
year = int(input("Enter a two-digit year: "))

# use ternary operator to return magic if month times day equals year, otherwiser return not magic
is_date_magic = "magic" if (month * day) == year else "not magic"

# output the result
print(f"The date is {is_date_magic}.")