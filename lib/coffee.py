#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self._size = None
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        allowed = ("Small", "Medium", "Large")
        if value not in allowed:
            print("size must be Small, Medium, or Large")
            return
        self._size = value

    def tip(self):
        # note: using U+2019 apostrophe to match tests
        print("This coffee is great, here’s a tip!")
        try:
            self.price = self.price + 1
        except Exception:
            # if price isn't numeric, ignore
            pass