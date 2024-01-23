# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("foo", 1, 10)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("foo", items[0].name)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(9, items[0].quality)

    def test_item_degrades_twice_as_fast_after_sell_date_passed(self):
        items = [Item("foo", 0, 10)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("foo", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(8, items[0].quality)

    def test_item_quality_does_not_go_negative(self):
        items = [Item("foo", 0, 0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("foo", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 1, 10)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(11, items[0].quality)

    # test this using "Aged Brie" since this increases in quality
    def test_item_quality_does_not_exceed_fifty(self):
        items = [Item("Aged Brie", 1, 50)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

    def test_sulfuras_does_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(80, items[0].quality)

    def test_backstage_passes_increase_by_1_in_quality_when_11_days_or_more(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(14, items[0].sell_in)
        self.assertEquals(21, items[0].quality)

    def test_backstage_passes_increase_by_2_in_quality_when_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(22, items[0].quality)

    def test_backstage_passes_increase_by_3_in_quality_when_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(23, items[0].quality)

    def test_backstage_passes_quality_drop_to_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
