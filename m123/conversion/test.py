"""Unit test for the conversion module.

Usage: python3 m123/conversion/test.py"""

import conversion
import test_cases

db = conversion.PriceDb()
for test_case in test_cases.price_db_variant_test_cases:
    db.add(test_case['price'], test_case['title'], test_case['brand'],
        test_case['model'], test_case['year'], test_case['transmission'])

db.export()
