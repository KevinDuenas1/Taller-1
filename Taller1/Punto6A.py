#Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble efecto. 
#Debe establecer previamente los valores de presión,así como las dimensiones físicas del cilindro para realizar el cálculo.
import numpy as np
embolo = 50                             # diametro embolo unidad en milimetros
vastago = 20                            # diametro del vastago debe ser menor a la del embolo mm
presiontrabajo = 6                      # unidad presion en bar

D=embolo*0.001                          #pasa de mm a metros el embolo
superficie= np.pi*(D**2/4)              #calcula superficie del embolo
presion= presiontrabajo*(10**5/1)       #pasa de bar a pascal
fuerza_avance=presion*superficie        #la fuerza de avance en newton

D1=vastago*0.001                        #pasa de mm a metros el vastago
superficie2= np.pi*(D1**2/4)            #calcula superficie del vastago
s=superficie-superficie2                #calcula area util
fuerza_retroceso=presion*s              #la fuerza de retroceso en newton
print()
print(f'''caracteristica del cilindro neumatico
      Embolo {embolo} mm.
      Vastago {vastago} mm.
      Presion de trabajo {presiontrabajo} bar.
      la fuerza de avance para el cilindro con estas caracteriticas es {fuerza_avance:.2f} Newtons.
      la fuerza de retroceso para el cilindro es {fuerza_retroceso:.2f} Newtons.''')