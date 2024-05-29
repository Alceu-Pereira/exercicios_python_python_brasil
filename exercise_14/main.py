weight = 65
penalty = None
excess = None

if weight > 50:
    excess = weight - 50
    penalty = excess * 4
    print(f'You caught {excess} kilograms more than authorized.')
    print(f'You will be penalized in R$ {penalty:.2f}')
else:
    print(f"For the quantity caught you will not be penalty")
