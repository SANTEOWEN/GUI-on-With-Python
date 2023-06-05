#format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# - this one is used to round to that many decimal places

# :(number)f = allocate that many spaces
# - this one is used to allocate that many spaces

# :03 = allocate and zero pad that many spaces
# 

# :< = left justify

# :> = right justify

# :+ = use a plus sign to indicate positive values

# := = placec sign to left most position

# :  =  insert a space before positive numbers

# :, = comma separator.

price1 = 3000.14159
price2 = -9870.65
price3 =  1200.34

print(f"price1 is {price1:+,.2f}")
print(f"price1 is {price2:}")
print(f"price1 is {price3: }")
