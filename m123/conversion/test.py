"""Unit test for the conversion module.

Usage: python3 m123/conversion/test.py"""

import conversion
import test_cases

print('### Test case: price_db_variant ###')
db = conversion.PriceDb()
for test_case in test_cases.price_db_variant_test_cases:
	print('Input: %s\tExpected: %s' % (test_case['title'], test_case['expected']))
	variant = db._convert_to_variant(test_case['title'], test_case['brand'],
        test_case['model'], test_case['year'], test_case['transmission'])
	assert variant == test_case['expected']

print('Test completed.')
