"""Usage: python3 m123/conversion/conversion.py"""

class PriceDb():

    """Data structure storing price.

    Use `insert` to add a new data point. Then use the compute functions to
    retrieve useful statistics of a particular category. You can also use
    `export` to print the whole content of the data structure as CSV."""

    def __init__(self):
        
        # The main data structure, which is a four-level nested dictionary of
        # car parameters (brand, model, year, and variant) and a list of price.
        # Sample structure:
        #
        #     self._db = {
        #         'brand': {
        #             'model': {
        #                 'year': {
        #                     'variant': [ 151000000, 152000000, 153000000 ]
        #                 }
        #             }
        #         }
        #     }
        #
        self._db = {}

        # These are a list of keywords which can be found in title but should
        # be ignored.
        self._ignorable_keywords = [
            # Transmission
            'Automatic', 'A/T', 'Manual', 'M/T',
            # Body types
            'Box', 'Hatchback', 'Jeep', 'Minibus', 'Minivans', 'MPV',
            'Pick-up', 'Sedan', 'SUV', 'Trucks', 'Wagon'
            # Possibly two words
            'Car', 'Van', '4WD', 'Offroad',
            # Specific technology
            'i-VTEC',
            # Miscellaneous
            'NA', 'Na'
        ]

        self._known_brand_typos = { 'KIA': 'Kia', 'MINI': 'Mini' }
        self._known_model_typos = {
            'I-10': 'i10', 'I-20': 'i20',               # Hyundai
            'Lexus NX Series': 'NX Series',             # Lexus
            'MINI Cooper S': 'Cooper',                  # Mini
            'Terano': 'Terrano', 'X-trail': 'X-Trail',  # Nissan
            'Gen 2': 'Gen-2',                           # Proton
            'Side Kick': 'Sidekick',                    # Suzuki
            'Kijang Innova': 'Innova'                   # Toyota
        }
        self._known_variant_typos = {
            # Daihatsu Xenia
            'ATTIVO': 'Attivo', 'DELUXE': 'Deluxe', 'DELUXE+': 'Deluxe+',
            'FAMILY': 'Family', 'SPORTY': 'Sporty',
            # Daihatsu Terios
            'ADVENTURE': 'Adventure', 'EXTRA': 'Extra'
        }



    def add(self, price, title, brand, model, year, transmission):
        variant = title
        # Remove any brand name, model name, and year from the variant.
        variant = variant.replace(brand, '')
        variant = variant.replace(model, '')
        variant = variant.replace(year, '')
        # Remove any double spaces from the variant.
        variant = variant.replace('  ', ' ')
        # Remove known keywords from the back of the variant.
        variant = self._remove_keywords(variant)
        # Remove duplicate words
        variant = self._remove_duplicate_words(variant)

        # Don't add the entry if the variant becomes empty.
        if len(variant) == 0:
            return

        # Add M/T or A/T to indicate transmission.
        if transmission == 'Automatic':
            variant = variant + ' A/T'
        elif transmission == 'Manual':
            variant = variant + ' M/T'
        # else:
            # TODO. Raise error.

        # In some Mazda models, we add Mazda in front of the model name.
        # e.g., Mazda 2, Mazda 3, Mazda 5, Mazda 6, Mazda 8.
        if brand == 'Mazda' and len(model) == 1:
            model = 'Mazda ' + model

        # Fix known typos.
        for (typo, correction) in self._known_brand_typos.items():
            brand = brand.replace(typo, correction)
        for (typo, correction) in self._known_model_typos.items():
            model = model.replace(typo, correction)
        for (typo, correction) in self._known_variant_typos.items():
            variant = variant.replace(typo, correction)

        # TODO. Engine displacement should be consistently before/after variant.

        # Insert a new entry to the data structure.
        if brand not in self._db:
            self._db[brand] = {}
        if model not in self._db[brand]:
            self._db[brand][model] = {}
        if year not in self._db[brand][model]:
            self._db[brand][model][year] = {}
        if variant not in self._db[brand][model][year]:
            self._db[brand][model][year][variant] = []
        self._db[brand][model][year][variant].append(price)



    def _remove_keywords(self, variant):
        variant_words = variant.split()

        # Repeat until the last word in the variant is not ignorable.
        last_word = variant_words[-1]
        while len(variant_words) > 0 and last_word in self._ignorable_keywords:
            variant_words.pop()
            if last_word == 'Car' and len(variant_words) > 1:
                # Remove an extra word. This will remove the likes of
                # 'Compact Car', 'City Car', 'Sports Car', and 'Super Car'.
                variant_words.pop()
            elif (last_word == 'Van' and len(variant_words) > 1
                and variant_words[-2] in [ 'Blind', 'High' ]):
                # This will remove the likes of 'Blind Van', and 'High Van'.
                variant_words.pop()

            if len(variant_words) > 0:
                last_word = variant_words[-1]

        # Reassemble the words again using space as separator.
        return ' '.join(variant_words)

    def _remove_duplicate_words(self, variant):
        variant_words = variant.split()
        # Iterate from the last word until the first word.
        for i in range(len(variant_words) - 1, -1, -1):
            if variant_words[i] in variant_words[0:i]:
                variant_words.pop(i)
            elif (len(variant_words[i]) == 1
                and variant_words[i].isdigit()
                and variant_words[i] + '.0' in variant_words[0:i]):
                # Remove if this word looks like '2' and '2.0' word exists.
                variant_words.pop(i)
            else:
                match = re.match('(\d\.\d)L', variant_words[i])
                if match and match.groups()[0] in variant_words[0:i]:
                    # Remove if this word looks like '1.2L' and '1.2' word exists.
                    variant_words.pop(i)

        # Reassemble the words again using space as separator.
        return ' '.join(variant_words)



    def compute_min(self, brand, model, year, variant):
        pass

    def compute_max(self, brand, model, year, variant):
        pass

    def compute_count(self, brand, model, year, variant):
        pass

    def compute_mean(self, brand, model, year, variant):
        pass

    def compute_median(self, brand, model, year, variant):
        pass

    def compute_modus(self, brand, model, year, variant):
        pass



    def export(self):
        brands = self._db.keys()
        for brand in brands:
            models = self._db[brand].keys()
            for model in models:
                years = self._db[brand][model].keys()
                for year in years:
                    variants = self._db[brand][model][year].keys()
                    for variant in variants:
                        print('%s - %s - %s - %s' % (brand, model, year, variant))



# =========
# Unit test
# =========

db = PriceDb()
test_cases = [
    {
        # Case with duplicate consecutive words.
        'price': 270000000, 'title': 'Civic 1.8 1.8 Sedan',
        'brand': 'Honda', 'model': 'Civic', 'year': '2013',
        'transmission': 'Automatic'
    },
    {
        # Case with duplicate separated words.
        'price': 300000000, 'title': 'C350 3.5 V6 3.5 Automatic Sedan',
        'brand': 'Mercedes-Benz', 'model': 'C350', 'year': '2009',
        'transmission': 'Automatic'
    },
    {
        # Case with two single ignorable keywords.
        'price': 1025000000, 'title': 'Vellfire 2.5 G Limited Van Wagon',
        'brand': 'Toyota', 'model': 'Vellfire', 'year': '2016',
        'transmission': 'Automatic'
    },
    {
        # Case with two double ignorable keywords.
        'price': 145000000, 'title': 'Yaris 1.5 Compact Car City Car',
        'brand': 'Toyota', 'model': 'Yaris', 'year': '2012',
        'transmission': 'Manual'
    },
    {
        # Case with two-word brand name.
        'price': 425000000, 'title': 'Rover Range Rover 4.4 Vogue SUV',
        'brand': 'Land Rover', 'model': 'Range Rover', 'year': '2004',
        'transmission': 'Automatic'
    },
    {
        # Case with two-word model name.
        'price': 255000000, 'title': 'Pajero Sport 2.5 Exceed SUV',
        'brand': 'Mitsubishi', 'model': 'Pajero Sport', 'year': '2010',
        'transmission': 'Automatic'
    },
    {
        # Case with brand name typo.
        'price': 114000000, 'title': 'Picanto 1.2 SE 2 Hatchback',
        'brand': 'KIA', 'model': 'Picanto', 'year': '2014',
        'transmission': 'Automatic'
    },
    {
        # Case with model name typo.
        'price': 99000000, 'title': 'X-trail 2.0 SUV Offroad 4WD',
        'brand': 'Nissan', 'model': 'X-trail', 'year': '2007',
        'transmission': 'Manual'
    },
    {
        # Case with variant name typo.
        'price': 95000000, 'title': 'Xenia 1.0 Li FAMILY MPV',
        'brand': 'Daihatsu', 'model': 'Xenia', 'year': '2011',
        'transmission': 'Manual'
    },
    {
        # Case with Mazda numerical model.
        'price': 198000000, 'title': '2 1.5 R Hatchback',
        'brand': 'Mazda', 'model': '2', 'year': '2015',
        'transmission': 'Automatic'
    }
]
for test_case in test_cases:
    db.add(test_case['price'], test_case['title'], test_case['brand'],
        test_case['model'], test_case['year'], test_case['transmission'])

db.export()
