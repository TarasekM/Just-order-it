class Order(object):
    def __init__(self, order_date=None, order_pickup_date=None,
                 items=None, total_price=None, table_number=None):
        self.order_date = order_date
        self.order_pickup_date = order_pickup_date
        self.items = items
        self.total_price = total_price
        self.table_number = table_number

    def get_dict(self):
        order = dict()
        order['Order_Date'] = self.order_date
        order['Order_Pickup_Date'] = self.order_pickup_date
        order['Items'] = self.items
        order['Total_Price'] = self.total_price
        order['Table_Number'] = self.table_number
        return order

    def __repr__(self):
        return self.get_dict()
