class Price(object):

    disc= 0.9
    qty=1

    def after_discount(self, price):
        return price * self.disc* self.qty 
