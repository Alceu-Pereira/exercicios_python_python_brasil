def data_por_extenso(data):
    data_lista = data.split('/')

    MESES = {
        '01' :'Janeiro',
        '02': 'Fevereiro',
        '03': 'Março',
        '04': 'Abril',
        '05': 'Maio',
        '06': 'Junho',
        '07': 'Julho',
        '08': 'Agosto',
        '09': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro'
    }

    try:
        if (1 <= int(data_lista[0]) <= 31) and (1 <= int(data_lista[1]) <= 12) and (int(data_lista[2])):
            return f'{data_lista[0]} de {MESES[data_lista[1]]} de {data_lista[2]}'
        else:
            return f'Null'
    except:
        return f'Null'


