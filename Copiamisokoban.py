class Sokoban: 

    mapa =[
        [2,2,2,2,2,2,2,2],
	[2,2,1,2,2,2,2,2],
	[2,1,1,1,0,1,2,2],
	[2,1,1,3,1,4,2,2],
	[2,1,1,1,3,1,1,2],
	[2,2,4,1,1,1,1,2],
	[2,2,2,2,2,2,2,2]
	]
		     
    posicion_fila = 2 #arriba,abajo#
    posicion_columna = 4 #abajo,izquierda#
    #derecha, posicion_cont+1#
    #izquierda, posicion_cont-1#
    #arriba,posicion_fila -1#
    #abajo,posicion_fila+1#

    #0 - personaje#
    #1 - pasillo#
    #2 - pared#
    #3 - caja#
    #4 - meta#
    #5 - caja/meta#
        
    #constructor#
    def _init_(self):
        print("Sokoban")
    print '\n****Bienvenido a Sokoban****\n'
        
    #metodo imprimir mapa#
    def imprimir_mapa(self):
            for f in range(7):#ciclo que marca cada cuando se repetira cada uno de los numeros en la fila#
                linea=''#ciclo que marca cada cuando se repite un numero#

                for c in range(8):#ciclo que marca cada cuando se repetira cada uno de los numeros en la columna#
                    linea=linea + ''  + str(self.mapa[f][c])  
                print linea #ciclo que marca cada cuando se repite un numero#

           #Mover Derecha# 
    def mover_derecha(self):
        if self.mapa[self.posicion_fila][self.posicion_columna+1]== 1: #Derecha#
            self.mapa[self.posicion_fila][self.posicion_columna+1]=0 #coloca monito posicion adelante#
            self.mapa[self.posicion_fila][self.posicion_columna]=1#coloca un espacio donde estaba el monito#
            self.posicion_columna += 1#Actualiza la posicion monito#
        #EMPUJAR CAJA HACIA LA DERECHA#
        elif self.mapa[self.posicion_fila][self.posicion_columna+1]==3 and self.mapa[self.posicion_fila][self.posicion_columna+2]==1: #verifica si hay un espacio y caja#
            self.mapa[self.posicion_fila][self.posicion_columna+2]=3#posicion de la caja hacia la derecha#
            self.mapa[self.posicion_fila][self.posicion_columna+1]=0#coloca monito espacio adelante#
            self.mapa[self.posicion_fila][self.posicion_columna]=1#coloca un espacio donde estaba el  monito#
            self.posicion_columna+=1 #actualiza la posicion del monito#
            #COLOCAR CAJA DERECHA EN META#
        elif self.mapa[self.posicion_fila ][self.posicion_columna+1] == 3 and self.mapa[self.posicion_fila ][self.posicion_columna+2] == 4:
            self.mapa[self.posicion_fila][self.posicion_columna+1] = 0
            self.mapa[self.posicion_fila][self.posicion_columna+2] = 5
            self.mapa[self.posicion_fila][self.posicion_columna] = 1 
            self.posicion_columna += 1
        
            #MOVER IZQUIERDA#
    def mover_izquierda(self):
        if self.mapa[self.posicion_fila][self.posicion_columna-1]== 1:#izquierda
            self.mapa[self.posicion_fila][self.posicion_columna-1]=0#coloca monito posicion adelante
            self.mapa[self.posicion_fila][self.posicion_columna]=1 #coloca un espacio donde estaba el monito
            self.posicion_columna -=1 #Actualiza la posicion monito#
            #EMPUJAR HACIA LA izquierda#
        elif self.mapa[self.posicion_fila][self.posicion_columna-1]==3 and self.mapa[self.posicion_fila][self.posicion_columna-2]==1: #verifica si hay un espacio y caja#
            self.mapa[self.posicion_fila][self.posicion_columna-2]=3
            self.mapa[self.posicion_fila][self.posicion_columna-1]=0
            self.mapa[self.posicion_fila][self.posicion_columna]=1
            self.posicion_columna-=1

            #COLOCAR CAJA EN IZQUIERDA#
        elif self.mapa[self.posicion_fila ][self.posicion_columna-1] == 3 and self.mapa[self.posicion_fila ][self.posicion_columna-2] == 4:
            self.mapa[self.posicion_fila][self.posicion_columna-1] = 0
            self.mapa[self.posicion_fila][self.posicion_columna-2] = 5
            self.mapa[self.posicion_fila][self.posicion_columna] = 1 
            self.posicion_columna -= 1
        
            #MOVER ARRIBA#
    def mover_arriba(self):
        if self.mapa[self.posicion_fila-1][self.posicion_columna]==1:#mover arriba
            self.mapa[self.posicion_fila-1][self.posicion_columna]=0#coloca monito posicion arriba
            self.mapa[self.posicion_fila][self.posicion_columna]=1#coloca un espacio donde estaba el monito
            self.posicion_fila -=1 #Actualiza la posicion monito
            #empujar caja hacia ARRIBA#
        elif self.mapa[self.posicion_fila-1][self.posicion_columna]==3 and self.mapa[self.posicion_fila-2][self.posicion_columna]==1: #verifica si hay un espacio y caja#
            self.mapa[self.posicion_fila-2][self.posicion_columna]=3
            self.mapa[self.posicion_fila-1][self.posicion_columna]=0
            self.mapa[self.posicion_fila][self.posicion_columna]=1
            self.posicion_fila-=1
            #COLOCAR CAJA EN META HACIA ARRIBA#
        elif self.mapa[self.posicion_fila -1][self.posicion_columna] == 3 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 4:
            self.mapa[self.posicion_fila-1][self.posicion_columna] = 0
            self.mapa[self.posicion_fila -2][self.posicion_columna] = 5
            self.mapa[self.posicion_fila][self.posicion_columna] = 1 
            self.posicion_fila -= 1
            

            #MOVER abajo#
    def mover_abajo(self):
        if self.mapa[self.posicion_fila+1][self.posicion_columna]==1: #Mover abajo
            self.mapa[self.posicion_fila+1][self.posicion_columna]=0#coloca monito posicion arriba
            self.mapa[self.posicion_fila][self.posicion_columna]=1 #coloca un espacio donde estaba el monito
            self.posicion_fila +=1 #Actualiza la posicion monito

            #EMPUJAR Hacia abajo#
        elif self.mapa[self.posicion_fila+1][self.posicion_columna]==3 and self.mapa[self.posicion_fila+2][self.posicion_columna]==1: #verifica si hay un espacio y caja#
            self.mapa[self.posicion_fila+2][self.posicion_columna]=3#posicion de la caja hacia la derecha#
            self.mapa[self.posicion_fila+1][self.posicion_columna]=0#coloca monito espacio adelante#
            self.mapa[self.posicion_fila][self.posicion_columna]=1#coloca un espacio donde estaba el  monito#
            self.posicion_fila+=1 #actualiza la posicion del monito#

            #COLOCAR CAJA EN META ABAJO#
        elif self.mapa[self.posicion_fila +1][self.posicion_columna] == 3 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 4:
            self.mapa[self.posicion_fila+1][self.posicion_columna] = 0
            self.mapa[self.posicion_fila +2][self.posicion_columna] = 5
            self.mapa[self.posicion_fila][self.posicion_columna] = 1 
            self.posicion_fila += 1
        
            


objeto = Sokoban()#crea el objeto de tipo sokoban

while True:
        objeto.imprimir_mapa()
        movimiento = raw_input("d-derecha,a-izquierda,w-arriba,s-abajo")
        if movimiento== "a":
            objeto.mover_izquierda()
        elif movimiento=="d":
            objeto.mover_derecha()
        elif movimiento=="w":
            objeto.mover_arriba()
        elif movimiento== "s":
            objeto.mover_abajo()