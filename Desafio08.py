larg = float(input('Qual é a largura da parede? '))
alt = float(input('Qual é a altura da parede? '))
area = larg * alt
tinta = area/2
print('A Area a ser coberta é de: {:.2f}m²'.format(area))
print('Você precisará de {:.2f} litros de tinta.'.format(tinta))
