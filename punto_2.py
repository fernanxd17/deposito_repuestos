#Programa que simula la compra de respuestos y aplica descuento segun el promedio de la compra
#By Fernando Romero

def askName():
    print("Bienvenid@!!!")
    print("Por favor digita tu nombre: ", end = "")
    name = input()
    print()
    return name

def showCat(name, catalogue):
    print("Hola {0}!!!".format(name))
    print("Estos son los respuestos que te ofrecemos, y sus respectivos precios:\n")
    tam = len(catalogue)
    for i in range(tam):
        print("{0}. {1}: ${2:,.2f}".format(i+1,catalogue[i][0], catalogue[i][1]))
        i+=1
    print()
            
def selectProduct():
    print("Por favor dijite el numero del producto y el total a comprar, en el siguiente formato: 'id_producto(espacio)total_ha_comprar'")
    list_item = list(map(int, input().split(' ')))  
    list_sale = list()
    list_sale.append(list_item)
    continuar = True
    while (continuar):
        print("Desea agregar otro producto (s/n): ", end="")
        answer = input()
        if(answer == 's'):
            print("\nPor favor dijite el numero del producto y el total a comprar, en el siguiente formato: 'id_producto(espacio)total_ha_comprar'")
            list_item = list(map(int, input().split(' ')))
            list_sale.append(list_item)
        else:
            continuar= False
    print()
    return list_sale

def validateDescount(list_sale):
    promedio, subTotal = calcularPromedioTotal(list_sale, catalogue)
    print("Promedio es de ${:,.2f}:".format(promedio))
    descuento = 0
    if(promedio > 150000):
        descuento = subTotal * 0.1
        print("Felicidades, Aplica descuento del 10%!!!")
    else: print("Lo sentimos, NO aplica descuento!")

    print("\nSub-Total: ${:,.2f}".format(subTotal))
    print("Descuento(10%): ${:,.2f}".format(descuento))
    print("Total: ${:,.2f}".format(subTotal - descuento))
    
def calcularPromedioTotal(list_sale, catalogue):
    subTotal = 0
    tam = len(list_sale)
    num_products = 0
    for i in range(tam):
        idProduct = list_sale[i][0] - 1
        precio    = catalogue[idProduct][1]
        cantidad  = list_sale[i][1]
        num_products+= cantidad
        subTotal +=  cantidad * precio 
    
    promedio = subTotal / num_products
    return promedio, subTotal

name = askName()
catalogue = [
                ['Pastillas Frenos', 151537], 
                ['Correa accesorios',53853], 
                ['Amortiguadores',   200000], 
                ['Discos frenos',    150000], 
                ['Embrague',         180000]
            ]

showCat(name, catalogue)
list_sale = selectProduct()
validateDescount(list_sale)