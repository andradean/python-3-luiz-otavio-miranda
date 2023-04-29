cpf = input('Digite um cpf valido: ')
cpf = cpf.split('-')
cpf_part_um = cpf[0].replace('.', '')
cpf_part_dois = cpf[1]

contador_regressivo_um = 10

resultado_um = 0

for digito in cpf_part_um:
    resultado_um += int(digito) * contador_regressivo_um
    contador_regressivo_um -= 1



digito_um = ((resultado_um * 10) % 11)
digito_um = digito_um if digito_um <= 9 else 0


cpf_nove_digi = cpf_part_um
cpf_part_dois_calc = cpf_part_dois[0]
cpf_part_um = cpf_part_um + cpf_part_dois_calc


contador_regressivo_dois = 11


resultado_dois = 0

for digito in cpf_part_um:
    resultado_dois += int(digito) * contador_regressivo_dois
    contador_regressivo_dois -= 1
    
digito_dois = ((resultado_dois * 10) % 11)
digito_dois = digito_dois if digito_dois <= 9 else 0


cpf_gerado_pelo_calculo = f'{cpf_nove_digi}{digito_um}{digito_dois}'

cpf_str = cpf_nove_digi + cpf_part_dois

if cpf_str == cpf_gerado_pelo_calculo:
    print(f'{cpf_str} é válido')
else:
    print('CPF inválido')