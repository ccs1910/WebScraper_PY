price_db_variant_test_cases = [
    {
        # Case with duplicate consecutive words.
        'price': 295000000, 'title': 'CR-V 2.4 2.4 Prestige SUV',
        'brand': 'Honda', 'model': 'CR-V', 'year': '2013',
        'transmission': 'Automatic', 'expected': '2.4 Prestige A/T'
    },
    {
        # Case with duplicate separated words.
        'price': 300000000, 'title': 'C350 3.5 V6 3.5 Automatic Sedan',
        'brand': 'Mercedes-Benz', 'model': 'C350', 'year': '2009',
        'transmission': 'Automatic', 'expected': '3.5 V6 A/T'
    },
    {
        # Case with duplicate engine displacement.
        'price': 95000000, 'title': 'March 1.2 1.2L Hatchback',
        'brand': 'Nissan', 'model': 'March', 'year': '2011',
        'transmission': 'Automatic', 'expected': '1.2 A/T'
    },
    {
        # Case with duplicate engine displacement.
        'price': 239000000, 'title': 'Civic 2.0 2 Sedan',
        'brand': 'Honda', 'model': 'Civic', 'year': '2014',
        'transmission': 'Automatic', 'expected': '2.0 A/T'
    },
    {
        # Case with two single ignorable keywords.
        'price': 1025000000, 'title': 'Vellfire 2.5 G Limited Van Wagon',
        'brand': 'Toyota', 'model': 'Vellfire', 'year': '2016',
        'transmission': 'Automatic', 'expected': '2.5 G Limited A/T'
    },
    {
        # Case with two double ignorable keywords.
        'price': 145000000, 'title': 'Yaris 1.5 Compact Car City Car',
        'brand': 'Toyota', 'model': 'Yaris', 'year': '2012',
        'transmission': 'Manual', 'expected': '1.5 M/T'
    },
    {
        # Case with two-word brand name.
        'price': 425000000, 'title': 'Range Rover 4.4 Vogue SUV',
        'brand': 'Land Rover', 'model': 'Range Rover', 'year': '2004',
        'transmission': 'Automatic', 'expected': '4.4 Vogue A/T'
    },
    {
        # Case with two-word model name.
        'price': 255000000, 'title': 'Pajero Sport 2.5 Exceed SUV',
        'brand': 'Mitsubishi', 'model': 'Pajero Sport', 'year': '2010',
        'transmission': 'Automatic', 'expected': '2.5 Exceed A/T'
    },
    {
        # Case with brand name typo.
        'price': 114000000, 'title': 'Picanto 1.2 SE 2 Hatchback',
        'brand': 'KIA', 'model': 'Picanto', 'year': '2014',
        'transmission': 'Automatic', 'expected': '1.2 SE 2 A/T'
    },
    {
        # Case with model name typo.
        'price': 99000000, 'title': 'X-trail 2.0 SUV Offroad 4WD',
        'brand': 'Nissan', 'model': 'X-trail', 'year': '2007',
        'transmission': 'Manual', 'expected': '2.0 M/T'
    },
    {
        # Case with variant name typo.
        'price': 95000000, 'title': 'Xenia 1.0 Li FAMILY MPV',
        'brand': 'Daihatsu', 'model': 'Xenia', 'year': '2011',
        'transmission': 'Manual', 'expected': '1.0 Li Family M/T'
    },
    {
        # Case with Mazda numerical model.
        'price': 198000000, 'title': '2 1.5 R Hatchback',
        'brand': 'Mazda', 'model': '2', 'year': '2015',
        'transmission': 'Automatic', 'expected': '1.5 R A/T'
    }
]
