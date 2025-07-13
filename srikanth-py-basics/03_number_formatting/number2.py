x = 4863.4343091

print(f"{x:.3}")
# If we specify fewer figures than we have in the integer 
# portion of the float, we end up with an exponent 
# representation instead:

print(f"{x:.3f}")

# f indicates that we want our float displayed as a 
# "fixed point number": in other words, we want a specific 
# number of digits after the decimal point. We can use f on
#  its own as well, which defaults to 6 digits of precision:

print(f"{x:f}")