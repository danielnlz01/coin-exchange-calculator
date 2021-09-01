# \n \n
#convertir de pesos a usd, eur, yen, libras, y cad. una funcion para cada conv. con las sig cond. 1 usd = 23 mxn, 1 eur = 26 mxn, 1 yen = 0.3 mxn, 1 libra = 1.2 eur y 1 cad = .80 usd

def mxn_usd(mxn):
  return mxn/23

def mxn_eur(mxn):
  return mxn/26

def mxn_yen(mxn):
  return mxn/0.3

def mxn_lib(mxn):
  return (mxn_eur(mxn))/(1.2)

def mxn_cad(mxn):
  return (mxn_usd(mxn))/(0.8)
  
mxn=float(input("Dame la cantidad de pesos que deseas convertir \n"))

print("Tus pesos a convertir: $"+str(mxn))
print("Tus pesos en dólares: $"+str(mxn_usd(mxn)))
print("Tus pesos en euros: $"+str(mxn_eur(mxn)))
print("Tus pesos en yen: $"+str(mxn_yen(mxn)))
print("Tus pesos en libras: $"+str(mxn_lib(mxn)))
print("Tus pesos en dólares canadiénses: $"+str(mxn_cad(mxn)))
  


