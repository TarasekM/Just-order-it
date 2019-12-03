class Item(object):
    def __init__(self, name=None, price=None, tags=None, ingredients=None):
        self.name = name
        self.price = price
        self.tags = tags
        self.ingredients = ingredients

    def get_dict(self):
        item = dict()
        item['Name'] = self.name
        item['Price'] = self.price
        item['Tags'] = self.tags
        item['Ingredients'] = self.ingredients
        return item

    def __repr__(self):
        return self.get_dict()
