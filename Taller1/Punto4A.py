#Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de la temperatura.
temp=80         #ingreso de temperatura

ro=100          # 100 ohms a 0 grados
coe_pt=0.385    # coeficiente platino
ar=coe_pt*temp 
##{
##calculo de resistencia de RTD
##RT=ro+Δr
##Δr=(α+ro)*(Δt)
##%}
resistencia=ro+ar
print()
print(f'''El calculo de una resistencia de valor {temp} grados en funcion de la temperatura es {resistencia} aproximadamente''')
print()