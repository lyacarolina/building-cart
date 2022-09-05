cart = []

 
id_user = input("Insira o id do usuário: ")
id_product  = input("Insira o id do produto: ")
price_product = float(input("Insira o preço do produto: "))
quantity_product = int(input("Insira a quantidade de produto: "))

item = [id_user, id_product, price_product, quantity_product]
cart = add_item_cart(item, cart)
print(cart)


def add_item_cart(item, cart):
    cart.append(item)
    return cart

def get_all_items_cart(item, cart):
    for item in cart:
        cart += item    
        return cart
 
def get_item_cart_by_id(id_product):
    kd_id = []
    for item in cart:
        if item[1] == id_product:
            return kd_id   
        else:
            print("Id não encontrado")
    

def remove_item_id(id_product):
    for item in cart:
        if item[1] == id_product:
            kd_id.remove()   
        else:
            print("Id não encontrado")