# script2.py
vlan = int(input("Ingresa el número de VLAN: "))
if vlan <= 1005:
    print("VLAN en rango normal.")
else:
    print("VLAN en rango extendido.")
