# --- ¡Encuentra el error!


def g( a , b ):
     return a  -  b


def f( a , b , c , d ):
     t0  =  a  +  b  -  g ( a , 0 )
     t1  =  g ( c , d )
     if c != d:
        t3  =  2  * ( t0  /  t1 )
        return t0  +  2 * t1  +  t3 * t3
     else:
         return"Can not calculate that"


# - Programa principal
print( "Resultado 1:" , f ( 5 , 2 , 5 , 0 ))
print( "Resultado 2:" , f ( 0 , 2 , 3 , 3 ))
print( "Resultado 3:" , f ( 1 , 3 , 2 , 3 ))
print ( "Resultado 4:" , f ( 1 , 9 , 22.0, 3 ))