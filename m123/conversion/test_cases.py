price_db_variant_test_cases = [
    {
        # Case with duplicate consecutive words.
        'title': '2013 Honda CR-V 2.4 2.4 Prestige SUV',
        'brand': 'Honda', 'model': 'CR-V', 'year': '2013',
        'transmission': 'Automatic', 'expected': '2.4 Prestige A/T'
    },
    {
        # Case with duplicate separated words.
        'title': '2009 Mercedes-Benz C350 3.5 V6 3.5 Automatic Sedan',
        'brand': 'Mercedes-Benz', 'model': 'C350', 'year': '2009',
        'transmission': 'Automatic', 'expected': '3.5 V6 A/T'
    },
    {
        # Case with duplicate and misformat engine displacement (1 of 2).
        'title': '2011 Nissan March 1.2 1.2L Hatchback',
        'brand': 'Nissan', 'model': 'March', 'year': '2011',
        'transmission': 'Automatic', 'expected': '1.2 A/T'
    },
    {
        # Case with duplicate and misformat engine displacement (2 of 2).
        'title': '2014 Honda Civic 2.0 2 Sedan',
        'brand': 'Honda', 'model': 'Civic', 'year': '2014',
        'transmission': 'Automatic', 'expected': '2.0 A/T'
    },
    {
        # Case with two single ignorable keywords.
        'title': '2016 Toyota Vellfire 2.5 G Limited Van Wagon',
        'brand': 'Toyota', 'model': 'Vellfire', 'year': '2016',
        'transmission': 'Automatic', 'expected': '2.5 G Limited A/T'
    },
    {
        # Case with two double ignorable keywords (1 of 2).
        'title': '2012 Toyota Yaris 1.5 Compact Car City Car',
        'brand': 'Toyota', 'model': 'Yaris', 'year': '2012',
        'transmission': 'Manual', 'expected': '1.5 M/T'
    },
    {
        # Case with two double ignorable keywords (2 of 2).
        'title': '2013 Suzuki APV 1.5 Blind Van High Van',
        'brand': 'Suzuki', 'model': 'APV', 'year': '2013',
        'transmission': 'Manual', 'expected': '1.5 M/T'
    },
    {
        # Case with a two-word brand name.
        'title': '2004 Land Rover Range Rover 4.4 Vogue SUV',
        'brand': 'Land Rover', 'model': 'Range Rover', 'year': '2004',
        'transmission': 'Automatic', 'expected': '4.4 Vogue A/T'
    },
    {
        # Case with a two-word model name.
        'title': '2014 Mitsubishi Pajero Sport 3.0 V6 SUV',
        'brand': 'Mitsubishi', 'model': 'Pajero Sport', 'year': '2014',
        'transmission': 'Automatic', 'expected': '3.0 V6 Bensin A/T'
    },
    {
        # Case with an ambiguous fuel type (1 of 2).
        'title': '2010 Hyundai H-1 2.5 XG MPV',
        'brand': 'Hyundai', 'model': 'H-1', 'year': '2010',
        'transmission': 'Automatic', 'expected': '2.5 XG Diesel A/T'
    },
    {
        # Case with an ambiguous fuel type (2 of 2).
        'title': '2016 Toyota Fortuner 2.7 SRZ SUV',
        'brand': 'Toyota', 'model': 'Fortuner', 'year': '2016',
        'transmission': 'Automatic', 'expected': '2.7 SRZ Bensin A/T'
    },
    {
        # Case with a minority fuel type.
        'title': '2013 Chevrolet Spin 1.5 LTZ SUV',
        'brand': 'Chevrolet', 'model': 'Spin', 'year': '2013',
        'transmission': 'Automatic', 'expected': '1.5 LTZ A/T'
    },
    {
        # Case with an ambiguous fuel type and a model name typo.
        'title': '2013 Toyota Kijang Innova 2.0 G Luxury MPV',
        'brand': 'Toyota', 'model': 'Kijang Innova', 'year': '2013',
        'transmission': 'Manual', 'expected': '2.0 G Luxury Bensin M/T'
    },
    {
        # Case with a brand name typo.
        'title': '2014 KIA Picanto 1.2 SE 2 Hatchback',
        'brand': 'KIA', 'model': 'Picanto', 'year': '2014',
        'transmission': 'Automatic', 'expected': '1.2 SE 2 A/T'
    },
    {
        # Case with a model name typo.
        'title': '2007 Nissan X-trail 2.0 SUV Offroad 4WD',
        'brand': 'Nissan', 'model': 'X-trail', 'year': '2007',
        'transmission': 'Manual', 'expected': '2.0 M/T'
    },
    {
        # Case with a variant name typo (1 of 2).
        'title': '2011 Daihatsu Xenia 1.0 Li FAMILY MPV',
        'brand': 'Daihatsu', 'model': 'Xenia', 'year': '2011',
        'transmission': 'Manual', 'expected': '1.0 Li Family M/T'
    },
    {
        # Case with a variant name typo (2 of 2).
        'title': '2016 Datsun GO+ 1.2 T-STYLE MPV',
        'brand': 'Datsun', 'model': 'GO+', 'year': '2016',
        'transmission': 'Manual', 'expected': '1.2 T-Style M/T'
    },
    {
        # Case with an edition-related typo (1 of 3).
        'title': '2015 Honda Jazz 1.5 RS Black Top Limited Edition Hatchback',
        'brand': 'Honda', 'model': 'Jazz', 'year': '2015',
        'transmission': 'Automatic', 'expected': '1.5 RS A/T'
    },
    {
        # Case with an edition-related typo (2 of 3).
        'title': '2011 MINI Cooper 1.6 S Red Hot Package Hatchback',
        'brand': 'MINI', 'model': 'Cooper', 'year': '2011',
        'transmission': 'Automatic', 'expected': '1.6 S A/T'
    },
    {
        # Case with an edition-related typo (3 of 3).
        'title': '2016 Toyota Alphard 2.5 G S C Package Van Wagon',
        'brand': 'Toyota', 'model': 'Alphard', 'year': '2016',
        'transmission': 'Automatic', 'expected': '2.5 G A/T'
    },
    {
        # Case with a color-related typo (1 of 3).
        'title': '2011 Chevrolet Captiva 2.0 Pearl White SUV',
        'brand': 'Chevrolet', 'model': 'Captiva', 'year': '2011',
        'transmission': 'Automatic', 'expected': '2.0 Diesel A/T'
    },
    {
        # Case with a color-related typo (2 of 3).
        'title': '2010 Daihatsu Luxio 1.5 X White Premier MPV',
        'brand': 'Daihatsu', 'model': 'Luxio', 'year': '2010',
        'transmission': 'Manual', 'expected': '1.5 X M/T'
    },
    {
        # Case with an edition-related typo (3 of 3).
        'title': '2015 Nissan Juke 1.5 RX Red Interior Revolt SUV',
        'brand': 'Nissan', 'model': 'Juke', 'year': '2015',
        'transmission': 'Automatic', 'expected': '1.5 RX Revolt A/T'
    },
    {
        # Case where brand name is a substring of model name.
        'title': '2013 MINI MINI Cooper S 1.6 Sedan',
        'brand': 'MINI', 'model': 'MINI Cooper S', 'year': '2013',
        'transmission': 'Manual', 'expected': '1.6 M/T'
    },
    {
        # Case with Mazda numerical model.
        'title': '2015 Mazda 2 1.5 R Hatchback',
        'brand': 'Mazda', 'model': '2', 'year': '2015',
        'transmission': 'Automatic', 'expected': '1.5 R A/T'
    }
]
