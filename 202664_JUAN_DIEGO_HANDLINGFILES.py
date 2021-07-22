products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return(products[code])

def get_property(code,property):
    return(products[code][property])

def main():
    ame_quant = 0
    bc_quant = 0
    cap_quant = 0
    dal_quant = 0
    esp_quant = 0
    fra_quant = 0
    total_price = 0
    while(True):
        user_input = input("Enter product code and quantity:")
        if user_input == "/":
            break
        else:
            product_code, quantity = user_input.split(",")
            if product_code == "americano":
                ame_quant += int(quantity)
            elif product_code == "brewedcoffee":
                bc_quant += int(quantity)
            elif product_code == "cappuccino":
                cap_quant += int(quantity)
            elif product_code == "dalgona":
                dal_quant += int(quantity)
            elif product_code == "espresso":
                esp_quant += int(quantity)
            elif product_code == "frappuccino":
                fra_quant += int(quantity)
            total_price += get_property(product_code,"price")*int(quantity)

    final_list = []

    if ame_quant != 0:
        final_list += [("americano",ame_quant)]
    if bc_quant != 0:
        final_list += [("brewedcoffee",bc_quant)]
    if cap_quant != 0:
        final_list += [("cappuccino",cap_quant)]
    if dal_quant != 0:
        final_list += [("dalgona",dal_quant)]
    if esp_quant != 0:
        final_list += [("espresso",esp_quant)]
    if fra_quant != 0:
        final_list += [("frappuccino",fra_quant)]

    with open('receipt.txt','w') as r:
        r.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
        ''')
    for order in final_list:
        code = order[0]
        name = get_property(order[0],"name")
        quantity = order[1]
        subtotal = get_property(order[0],"price") * quantity

        with open('receipt.txt',"a") as r:
            r.write(f'\n{code}\t\t{name}\t\t{quantity}\t\t\t\t{subtotal}')

    with open('receipt.txt','a+') as r:
        r.write(f'''
Total:\t\t\t\t\t\t\t\t\t\t{total_price}
==
        ''')
        r.seek(0)
        print(r.read())

main()
