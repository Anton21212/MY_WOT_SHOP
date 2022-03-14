from decimal import Decimal

from django.conf import settings

from shop.models import Fuel, Tanks

CATEGORY_MAPPING = {
    "Fuel": Fuel,
    "Tanks": Tanks
}


class Cart:
    """
    Инициализируем корзину
    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {
                "products": []
            }
        self.cart = cart

    def save(self):
        "Обновление сессии cart"
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product, quantity=1):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        category_name = str(product._meta.object_name)
        product_price = str(product.price)
        product_title = str(product.title)
        image = product.img.url

        product_dict = {
            "id": product_id,
            "category": category_name,
            "price": product_price,
            "quantity": quantity,
            "title": product_title,
            "image": product.img.url,

        }
        products = self.cart.get("products")
        generator = [i for i in products if i.get("id") == product_id and i.get("category") == category_name]

        if generator:
            available_product_dict_1 = generator[0]
            available_product_dict = dict(available_product_dict_1)
            available_product_dict["quantity"] = quantity
            self.cart["products"].remove(available_product_dict_1)
            self.cart["products"].append(available_product_dict)

        else:
            self.cart["products"].append(product_dict)

        self.save()

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        category_name = str(product._meta.object_name)

        products = self.cart.get("products")

        generator = [i for i in products if i.get("id") == product_id and i.get("category") == category_name]
        if generator:
            available_product_dict_1 = generator[0]
            self.cart["products"].remove(available_product_dict_1)

        self.save()



    def __iter__(self):
        """
         Перебор элемента в корзине и получение продуктов из базы данных.
        """
        self.cart["total_price"] = 0
        products = self.cart.get("products")

        for product in products:

            self.cart["total_price"] += Decimal(product.get("price"))
            yield product


    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.get("products", []))

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.get("products", []))

    def clear(self):
        " удаление корзины из сессии"
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

