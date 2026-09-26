   #PONDERA: int
  # ESTADO: int #(1=ocupado,2=desocupado,3=inactivo)
  # CAT_OCUP: int #categoríaocupacional
  # EDAD: int
  # REGION: int #numero por alguna razon
  # AGLOMERADO: int
  # MAS_500: str #Aglomerados según tamaño: N = Conjunto  de  aglomerados de menos de 500.000 habitantes,
  #             #   S = Conjunto de aglomerados  de 500.000 y más habitantes
  # ANO4 = int #año
  # TRIMESTRE = int #1 -4
  # ITF: int
  # GDECCFR: int #grupo del decil por ingreso


def ordenar_columnas (rol,columnas,lista_roles):
    if (rol in lista_roles):
        print( 'oh si ')
        nuevo_diccionario = {k:columnas[k] for k in columnas if k in lista_roles[rol][0]}
        #recorre los k elementos de columnas en la lista de roles, en la posicion de columnas
                
        if lista_roles [rol][1] == 'alfabeticamente':
            print ('ordenando alfabeticamente la nueva columna...')
            nuevo_diccionario = sorted (nuevo_diccionario.items() ) #ordena alfabeticamente
            lista_roles[rol].append(nuevo_diccionario)
            

        elif lista_roles [rol][1] == 'porcentaje':
            print ('ordenando por porcentaje la nueva columna...')
            nuevo_diccionario = sorted (nuevo_diccionario.items(), key=lambda item:item[0][1]) #ordena alfabeticamente
            lista_roles[rol].append(nuevo_diccionario)

        if lista_roles [rol][2] == 'A' :
            print ('la columna fue ordenada de manera ascendente')
            lista_roles[rol][4] = sorted(lista_roles[rol][4], reverse = False)
        elif lista_roles [rol] [2] == 'B':
            print ('la columna fue ordenada de manera descendente')
            lista_roles[rol][4] = sorted(lista_roles[rol][4], reverse = True)
            print(lista_roles[rol][4])
            
            
    else:
        print ('el rol de ', rol ,' no se encuentra en la lista')
    
        



columnas = {'estado':[range(1,4),0.54], 'año':[int,1.00],
                  'cat_ocup':[int,0.15],    'edad':[int,0.45],  'region':[str,0.32]}

lista_roles = {'docente':[['año','estado','region'],'alfabeticamente','A',None],
         'investigador':[['año','estado','cat_ocup'],'porcentaje','B',0.35],
         'analista':[['año','edad','cat_ocup'],'alfabeticamente','B',None]}





rol_input = input('ingrese rol a buscar: ')
ordenar_columnas (rol_input,columnas,lista_roles)


print(lista_roles[rol_input])


