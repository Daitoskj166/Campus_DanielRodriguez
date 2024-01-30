def calculaPrecio(precioOriginal, porcentajeDescuento):
    descuento = precioOriginal -  porcentajeDescuento
    return precioOriginal - descuento

def calculoImpuesto(precioConDescuento, porcentajeImpuesto):
    IVA = precioConDescuento*porcentajeImpuesto
    return precioConDescuento+IVA


def total():
    precioTotal = float(input("Precio producto: "))
    descuento = float(input("Descuento: "))
    impuesto = float(input("iva: "))
    
    precioDescuento= calculaPrecio(precioTotal, descuento)
    precioConDescuentoConImpuesto= calculoImpuesto(precioDescuento, impuesto)
    
    print("Bienvenido su precio final fue: ", precioTotal)
    print("Bienvenido su precio inicial con descuento fue: " ,precioDescuento)
    print("Bienvenido su precio descuento con impuesto es: " ,precioConDescuentoConImpuesto)
    

#algoritmo
total()

