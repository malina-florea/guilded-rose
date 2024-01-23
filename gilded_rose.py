# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


BRIE = "Aged Brie"
PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.name != BRIE and item.name != PASS:
                if item.quality > 0:
                    if item.name != SULFURAS:
                        self.decrease_quality_by_1(item)
            else:
                if item.quality < 50:
                    self.increase_quality_by_1(item)
                    if item.name == PASS:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                self.increase_quality_by_1(item)
                        if item.sell_in < 6:
                            if item.quality < 50:
                                self.increase_quality_by_1(item)
            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != BRIE:
                    if item.name != PASS:
                        if item.quality > 0:
                            if item.name != SULFURAS:
                                self.decrease_quality_by_1(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        self.increase_quality_by_1(item)

    @staticmethod
    def decrease_quality_by_1(item):
        item.quality = item.quality - 1

    @staticmethod
    def increase_quality_by_1(item):
        item.quality = item.quality + 1
