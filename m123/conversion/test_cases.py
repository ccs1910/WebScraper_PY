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
        # Case with duplicate and misformat engine displacements (1 of 2).
        'title': '2011 Nissan March 1.2 1.2L Hatchback',
        'brand': 'Nissan', 'model': 'March', 'year': '2011',
        'transmission': 'Automatic', 'expected': '1.2 A/T'
    },
    {
        # Case with duplicate and misformat engine displacements (2 of 2).
        'title': '2014 Honda Civic 2.0 2 Sedan',
        'brand': 'Honda', 'model': 'Civic', 'year': '2014',
        'transmission': 'Automatic', 'expected': '2.0 A/T'
    },
    {
        # Case with duplicate model names (1 of 3).
        'title': '2012 Peugeot 107 1.0 107 Hatchback',
        'brand': 'Peugeot', 'model': '107', 'year': '2012',
        'transmission': 'Automatic', 'expected': '1.0 A/T'
    },
    {
        # Case with duplicate model names (2 of 3).
        'title': '2014 Subaru WRX STi 2.5 WRX STi Sedan',
        'brand': 'Subaru', 'model': 'WRX STi', 'year': '2014',
        'transmission': 'Manual', 'expected': '2.5 M/T'
    },
    {
        # Case with duplicate model names (3 of 3).
        'title': '2014 Porsche Panamera 3.0 Panamera S Fastback',
        'brand': 'Porsche', 'model': 'Panamera', 'year': '2014',
        'transmission': 'Automatic', 'expected': '3.0 S Fastback A/T'
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
        # Case with an edition-related variant (1 of 3).
        'title': '2015 Honda Jazz 1.5 RS Black Top Limited Edition Hatchback',
        'brand': 'Honda', 'model': 'Jazz', 'year': '2015',
        'transmission': 'Automatic', 'expected': '1.5 RS A/T'
    },
    {
        # Case with an edition-related variant (2 of 3).
        'title': '2011 MINI Cooper 1.6 S Red Hot Package Hatchback',
        'brand': 'MINI', 'model': 'Cooper', 'year': '2011',
        'transmission': 'Automatic', 'expected': '1.6 S A/T'
    },
    {
        # Case with an edition-related variant (3 of 3).
        'title': '2016 Toyota Alphard 2.5 G S C Package Van Wagon',
        'brand': 'Toyota', 'model': 'Alphard', 'year': '2016',
        'transmission': 'Automatic', 'expected': '2.5 G A/T'
    },
    {
        # Case with a color-related variant (1 of 3).
        'title': '2011 Chevrolet Captiva 2.0 Pearl White SUV',
        'brand': 'Chevrolet', 'model': 'Captiva', 'year': '2011',
        'transmission': 'Automatic', 'expected': '2.0 Diesel A/T'
    },
    {
        # Case with a color-related variant (2 of 3).
        'title': '2010 Daihatsu Luxio 1.5 X White Premier MPV',
        'brand': 'Daihatsu', 'model': 'Luxio', 'year': '2010',
        'transmission': 'Manual', 'expected': '1.5 X M/T'
    },
    {
        # Case with an edition-related variant (3 of 3).
        'title': '2015 Nissan Juke 1.5 RX Red Interior Revolt SUV',
        'brand': 'Nissan', 'model': 'Juke', 'year': '2015',
        'transmission': 'Automatic', 'expected': '1.5 RX Revolt A/T'
    },
    {
        # Case with a BMW minor variant.
        'title': '2010 BMW 320i 2.0 Business Edition Sedan',
        'brand': 'BMW', 'model': '320i', 'year': '2010',
        'transmission': 'Automatic', 'expected': '2.0 A/T'
    },
    {
        # Case with Mercedes-Benz minor variant.
        'title': '2014 Mercedes-Benz CLA200 1.6 Urban Coupe',
        'brand': 'Mercedes-Benz', 'model': 'CLA200', 'year': '2014',
        'transmission': 'Automatic', 'expected': '1.6 Coupe A/T'
    },
    {
        # Case where the brand name is a substring of the model name.
        'title': '2013 MINI MINI Cooper S 1.6 Sedan',
        'brand': 'MINI', 'model': 'MINI Cooper S', 'year': '2013',
        'transmission': 'Manual', 'expected': '1.6 M/T'
    },
    {
        # Case where the model name is a substring of the variant name.
        'title': '2015 MINI Cooper 2.0 John Cooper Works Hatchback',
        'brand': 'MINI', 'model': 'Cooper', 'year': '2015',
        'transmission': 'Automatic', 'expected': '2.0 John Cooper Works A/T'
    },
    {
        # Case where the year is a substring of the model name.
        'title': '2000 Mazda E2000 2.0 Ltd Van',
        'brand': 'Mazda', 'model': 'E2000', 'year': '2000',
        'transmission': 'Manual', 'expected': '2.0 Ltd M/T'
    },
    {
        # Case with Karimun Wagon R.
        'title': '2014 Suzuki Karimun Wagon R 1.0 DILAGO Wagon R Hatchback',
        'brand': 'Suzuki', 'model': 'Karimun Wagon R', 'year': '2014',
        'transmission': 'Manual', 'expected': '1.0 Dilago M/T'
    },
    {
        # Case with Mazda numerical model.
        'title': '2015 Mazda 2 1.5 R Hatchback',
        'brand': 'Mazda', 'model': '2', 'year': '2015',
        'transmission': 'Automatic', 'expected': '1.5 R A/T'
    }
]
