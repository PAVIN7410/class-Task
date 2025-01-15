# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.



class Store:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.items = {}

    def add_items(self, product, price):     #Добавим товар
        self.items[product] = price


    def delete_items(self, product):#                          #Удаляем товар
        if product in self.items:
            del self.items[product]


    def get_price_product(self, product):                      #Возвращает цену товара. Если товара нет, возвращает None
        return self.items.get(product)



    def get_new_price_items(self, product, price):        #Обновляет цену товара, если он есть в ассортименте
        if product in self.items:
            self.items[product] = price

            return price                                      # Возвращаем обновленную цену

        return None                                              # Возвращаем None, если товар не найден

    def info(selfself):
        print(f"name-{self.name},address-{self.address}")


       # Создание 3 Store и тест 1

store1 = Store("Магазин фруктов", "Улица Ленина, 10")
store2 = Store("Книжный магазин", "Проспект Мира, 5")
store3 = Store("Электроника", "Улица Победы, 15")

print(store1.name)
print(store1.address)

        #Добавление товаров
store1.add_items("бананы", 0.75)
print("Цена бананов:", store1.get_price_product("бананы"))
store1.add_items("яблоки", 0.5)
print("Цена яблок:", store1.get_price_product("яблоки"))

store2.add_items("книга о Python", 15.0)
store2.add_items("книга о Java", 20.0)

store3.add_items("ноутбук", 500.0)
store3.add_items("телевизор", 300.0)

        #Тест методов store1

print("Цена яблок:", store1.get_price_product("яблоки"))

new_price = store1.get_new_price_items("яблоки",0.6)

if new_price is not None:
    print("Обновленная цена яблок:", new_price  )
else:
    print("Товар не найден в ассортименте.")
print("Цена бананов:", store1.get_price_product("бананы"))
store1.delete_items("бананы")
print("Цена бананов после удаления:", store1.get_price_product("бананы"))
print("БАНАНИВ НЕМАЕ!!!")

print("Ура-а-а Бананы завели!")
store1.add_items("бананы", 0.85)
print("Цена бананов:", store1.get_price_product("бананы"))
