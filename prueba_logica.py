#Prueba de logica DaCodes

#Tomando en cuenta que el programa se basa en "casos"

print('Ingrese el número de casos que se evaluarán en la cuadrícula:')

casos = int(input())

print('\n')

for i in range(0, casos) :
	
	print('Caso numero: ' +  str(i+1) + '\n')	
	print('Ingresa el numero de filas de la cuadricula:')
	
	filas = int(input())
	
	print('Ingresa el numero de columnas de la cuadricula:')
	
	columnas = int(input())

	print('\n')

	if filas == columnas and filas > 1:

		if filas % 2 == 0:
			print('AL TERMINAR DE RECORRER LA CUADRICULA TERMINASTE VIENDO HACIA LA IZQUIERDA\n')
		else:
			print('AL TERMINAR DE RECORRER LA CUADRICULA TERMINASTE VIENDO HACIA LA DERECHA\n')
	elif filas > columnas and columnas > 1:
		if columnas % 2 == 0:
			print('AL TERMINAR DE RECORRER LA CUADRICULA TERMINASTE VIENDO HACIA ARRIBA\n')
		else:
			print('AL TERMINAR DE RECORRER LA CUADRICULA TERMINASTE VIENDO HACIA ABAJO\n')
	elif columnas > filas :
		if filas % 2 == 0:
			print('AL TERMINAR DE RECORRER LA CUADRICULA TERMINASTE VIENDO HACIA LA IZQUIERDA\n')
		else:
			print('AL TERMINAR DE RECORRER LA CUADRICULA TERMINASTE VIENDO HACIA LA DERECHA\n')
	elif columnas == 1:
		if filas == 1:
			print('AL TERMINAR DE RECORRER LA CUADRICULA TERMINASTE VIENDO HACIA LA DERECHA\n')
		else:
			print(' AL TERMINAR DE RECORRER LA CUADRICULA TERMINASTE VIENDO HACIA ABAJO\n')