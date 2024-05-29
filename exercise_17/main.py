import math

square_are_in_meters = input('How many square meters is the area? ')


needed_liters = float(square_are_in_meters) / 6
needed_liters_rounded = math.ceil(needed_liters)

INK_CAN_LITERS = 18
INK_CAN_PRICE = 80


INK_GALLONS_LITERS = 3.6
INK_GALLONS_PRICE = 25


print(f'You need to buy {needed_liters_rounded} ink liters')

print(f'If you JUST BUY INK CANS, you need to buy {math.ceil(needed_liters_rounded / 18)} ink cans per R$ {math.ceil((needed_liters_rounded / 18)) * 80:.2f}')

print(f'If you JUST BUY INK GALONS, you need to buy {math.ceil(needed_liters / 3.6)} ink gallons per R$ {math.ceil(needed_liters / 3.6) * 25:.2f}')


# needed_liters = math.ceil(needed_liters + (0.1 * needed_liters))
ink_cans = ink_gallons = 0

if needed_liters_rounded > 18:
    ink_cans = needed_liters // 18
    ink_gallons = math.ceil((needed_liters_rounded % 18) / 3.6)


elif needed_liters_rounded == 18:
    ink_cans = math.ceil(needed_liters_rounded / 18)


else:
    ink_gallons = math.ceil(needed_liters_rounded / 3.6)

print(f'If you want to buy INK CANS and the rest in GALLONS you need to buy {ink_cans} ink cans and {ink_gallons} ink gallons per R$ {float((ink_cans * 80) + (ink_gallons * 25)):.2f}')
