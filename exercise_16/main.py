area_to_paint = input('How many square meters is the area to be painted? ')
ink_liters = float(area_to_paint) / 3
INK_AMOUNTH_CAN = 18
INK_CAN_PRICE = 80
ink_to_be_buyed = None

if ink_liters >= INK_AMOUNTH_CAN:
    ink_to_be_buyed = ink_liters // 18
else:
    ink_to_be_buyed = 1

total_price = float(80 * ink_to_be_buyed)

print(f'You need to buy {ink_to_be_buyed:.0f} paint inks')
print(f'The total price is R$ {total_price:.2f}')