products = []


def infoAndInput(mes):
    print(mes)
    f = input()
    return f


class product:
    def __init__(self, name, bio, price, amount):
        self.name = name
        self.bio = bio
        self.price = price
        self.amount = int(amount)

    def toDictionary(self):
        return {
            'name': self.name,
            'bio': self.bio,
            'price': self.price,
            'amount': int(self.amount)
        }


print("welcome to foroshgah!!!!")
while (True):
    print("1 for seller 2 for customer")
    userType = int(input())

    if userType == 1:
        name = infoAndInput("name?")
        bio = infoAndInput("bio?")
        price = infoAndInput("price?")
        amount = infoAndInput("amount(tedad mahsool dar anbar)?")
        myProduct = product(name, bio, price, amount)
        products.append(myProduct.toDictionary())
        print("product was added")
    else:
        for i in range(len(products)):
            if (products[i]['amount'] == 0):
                products.pop(i)
        if(products==[]):
            print("no products")
            continue;
        for i in range(len(products)):
            print(
                f"{i+1}.name: {products[i]['name']}, bio: {products[i]['bio']}, price:{products[i]['price']}$,")

        n = infoAndInput("which you will buy?(type the product number)")
        products[int(n)-1]['amount'] -= 1
        print("thanks for buying!")
