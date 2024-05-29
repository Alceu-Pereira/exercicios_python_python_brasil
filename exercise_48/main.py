from func import by_to_mb, percentage

with open('exercise_48\\usuarios.txt', 'r', encoding='UTF-8') as file:
    dados_geral = []
    dados_bytes = []

    for line in file:
        name, space = line.strip().split()

        space = by_to_mb(int(space))

        dados_geral.append(name)
        dados_bytes.append(space)

    total, values_in_list, media = percentage(dados_bytes)

with open('exercise_48\\relatorio.txt', 'w+', encoding='UTF-8') as file_rel:
    file_rel.write(f"{'ACME Inc.':<25}{'Uso do espaço em disco pelos usuários'}\n")
    file_rel.write(f"{'-' * 85}\n{'-' * 15}\n")
    file_rel.write(f"{'Nr.':<6}{'Usuário':<20}{'Espaço Utilizado':<30}{r'% do uso'}\n\n")
    for k, v in enumerate(dados_geral):
        file_rel.write(f"{k:<6}{v:<20}{dados_bytes[k]:>8} MB{values_in_list[k]:>25}{" %"}\n")
    file_rel.write(f'\nEspaço total ocupado: {total} MB\n')
    file_rel.write(f'Espaço médio ocupado: {media} MB')
