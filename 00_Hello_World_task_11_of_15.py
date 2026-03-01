order_number=269

first_order_remainder = order_number%10
print(first_order_remainder)
#below is the same but with comments and str function which formally makes the solution incorrect
#print("first_order_remainder is equal to: "+str(first_order_remainder))
if first_order_remainder==0:
  first_order_coupon = "yes"
else:
  first_order_coupon = "no"

order_number=270
second_order_remainder = order_number%10
#second_order_remainder = 270%10
print(second_order_remainder)
if second_order_remainder==0:
  second_order_coupon = "yes"
else:
  second_order_coupon = "no"
print(second_order_coupon)

