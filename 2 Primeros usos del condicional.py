#se desea, primero reconer si dos numeros son impares o pares y segun a ello resolver los casos dados
A = int(input())
B = int(input())
#primero se definen las variables
if(A%2==0):
    if(B%2==0):
        print(A*B)
    else :
        print(A//B)
else :
    if(B%2==0) :
        print(A+B)
    else :
        print(A-B)
#despues del `print' lo que va entre corchetes debe estar sin comillas ya que si las llevase seria un string y no una operacion
        
    
