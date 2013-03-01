from scrapy.item import Item, Field

class AmazumpItem(Item):
    order_id = Field()
    order_placed = Field()
    order_total = Field()
    shippings = Field()

    # item_id = Field()
    # item_name = Field()
    # item_price = Field()
    # item_quantity = Field()
    # item_condition = Field()
    # sales_tax = Field()
    # payment_method = Field()
    # purchase_date = Field()
    # ship_date = Field()
    # recipient = Field()
    # shipping_address = Field()
    # shipping_speed = Field()
    # sold_by = Field()


