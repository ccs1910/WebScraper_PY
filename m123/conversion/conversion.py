"""Usage: python3 m123/conversion/conversion.py"""

import re
import statistics



class PriceDb():

    """Data structure for categorizing price and computing statistics.

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
            'Pick-up', 'Sedan', 'SUV', 'Trucks', 'Wagon',
            # Fuel types, because they will be added later into the variant
            # when necessary. By ignoring then here, we prevent duplicate fuel
            # type to appear in the resulting variant.
            'Bensin', 'Diesel', 'Petrol',
            # Possibly two words
            'Car', 'Van', '4WD', 'Offroad',
            # Specific technology
            'i-VTEC',
            # Miscellaneous
            'NA', 'Na'
        ]

        self._multi_fuel_models = {
            # Source: Wikipedia.
            'Captiva': {
                '2.0': 'Diesel', '2.2': 'Diesel',
                '2.4': 'Bensin', '3.0': 'Bensin', '3.2': 'Bensin'
            },
            # Source: https://en.wikipedia.org/wiki/Hyundai_Starex
            'H-1': { '2.4': 'Bensin', '2.5': 'Diesel' },
            'Santa Fe': { '2.2': 'Diesel', '2.4': 'Bensin' },
            # Only 2.7 Bensin, 2.4 Diesel (newer variants), and 2.5 Diesel
            # (older variants) are released in Indonesia (source: Wikipedia).
            'Fortuner': {
                '2.7': 'Bensin', '4.0': 'Bensin',
                '2.4': 'Diesel', '2.5': 'Diesel', '2.8': 'Diesel', '3.0': 'Diesel'
            },
            # Only 2.0 Bensin, 2.4 Diesel (newer variants), and 2.5 Diesel
            # (older variants) are released in Indonesia (source: Wikipedia).
            'Innova': {
                '2.0': 'Bensin', '2.7': 'Bensin',
                '2.4': 'Diesel', '2.5': 'Diesel', '2.8': 'Diesel'
            },
            # Below is a typo of the above but must be redundantly included.
            'Kijang Innova': {
                '2.0': 'Bensin', '2.7': 'Bensin',
                '2.4': 'Diesel', '2.5': 'Diesel', '2.8': 'Diesel'
            },
            # Below we only include one fuel type because it has significantly
            # low population.
            'Pajero': { '3.0': 'Bensin' },
            'Pajero Sport': { '3.0': 'Bensin' },
            'Spin': { '1.3': 'Diesel' }
        }

        self._known_brand_typos = { 'KIA': 'Kia', 'MINI': 'Mini' }
        self._known_model_typos = {
            'I-10': 'i10', 'I-20': 'i20',               # Hyundai
            'Ranger Rover': 'Range Rover',              # Land Rover
            'Lexus NX Series': 'NX Series',             # Lexus
            'MINI Cooper S': 'Cooper',                  # Mini
            'Colt T120 SS': 'Colt T120ss',              # Mitsubishi
            'Colt T120SS': 'Colt T120ss',               # Mitsubishi
            'Terano': 'Terrano', 'X-trail': 'X-Trail',  # Nissan
            'Gen 2': 'Gen-2',                           # Proton
            'Side Kick': 'Sidekick',                    # Suzuki
            'Kijang Innova': 'Innova'                   # Toyota
        }
        # TODO. Some models still need manual improvement, e.g., Brio Satya,
        # Camry Hybrid, Sirion D, and Gran Max (Blind Van, Box, MPV, Pick Up).
        self._known_variant_typos = {
            # Daihatsu Gran Max
            'BOX': 'Box',
            # Daihatsu Xenia
            'ATTIVO': 'Attivo', 'DELUXE': 'Deluxe',
            'FAMILY': 'Family', 'SPORTY': 'Sporty', 'PLUS': 'Plus',
            # Daihatsu Terios
            'ADVENTURE': 'Adventure', 'ELEGANT': 'Elegant', 'EXTRA': 'Extra',
            # Datsun Go
            'A-OPTION': 'A-Option', 'T-ACTIVE': 'T-Active',
            'T-OPTION': 'T-Option', 'T-STYLE': 'T-Style',
            # Isuzu Panther
            'GRAND': 'Grand', 'SMART': 'Smart', 'TOURING': 'Touring',
            # Isuzu Pick Up
            '3 WAY': '3 Way',
            # Mini Countryman
            'JCW': 'John Cooper Works',
            # Mitsubishi Mirage
            'EXCEED': 'Exceed',
            # TODO. Some BMW model names are also repeated in variant names.
            # Suzuki Karimun Wagon R
            'DILAGO': 'Dilago',
            'Wagon R ': '',  # Because the model name already contains Wagon R.
            # Typos below are introduced because of limited sample quantity.
            # By removing these phrases, we merge a small variant with its
            # more generic variant. The spare space at the end is necessary.
            'Pearl White ': '',                 # Chevrolet Captiva
            'White Premier ': '',               # Daihatsu Luxio
            'Black Top Limited Edition ': '',   # Honda Jazz
            'Red Hot Package ': '',             # Mini Cooper
            'S C Package ': '',                 # Toyota Alphard
            # Nissan Juke (this one shall be temporary, because there are
            # significant price differences between these variants)
            'Black Interior ': '', 'Red Interior ': '', 'Red Edition ': ''
        }

        # These are the phrases in variant names that may be eliminated. By
        # doing so, we merge several specific but similarly priced variants
        # into one variant which has better sample quantity.
        self._minor_variants = {
            'BMW': [
                'Business', 'Comfort', 'Edition', 'Luxury',
                'Modern', 'Sport', 'Touring', 'Urban'
            ],
            'Mercedes-Benz': [ 'Classic', 'Exclusive', 'Sport', 'Urban' ]
        }



    def add(self, price, title, brand, model, year, transmission):
        variant = self._convert_to_variant(title, brand, model, year,
            transmission)

        if variant is not None:
            # Fix known typos.
            for (typo, correction) in self._known_brand_typos.items():
                brand = brand.replace(typo, correction)
            for (typo, correction) in self._known_model_typos.items():
                model = model.replace(typo, correction)

            # In some Mazda models, we add Mazda in front of the model name.
            # e.g., Mazda 2, Mazda 3, Mazda 5, Mazda 6, Mazda 8.
            if brand == 'Mazda' and len(model) == 1:
                model = 'Mazda ' + model

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

    def _convert_to_variant(self, title, brand, model, year, transmission):
        variant = title

        # Remove any year, brand, and model name from the variant.
        # The extra whitespace is to ensure only whole words are replaced.
        variant = variant.replace(year + ' ', '', 1)
        variant = variant.replace(brand + ' ', '', 1)
        variant = variant.replace(model + ' ', '', 1)
        # Remove any double spaces from the variant.
        variant = variant.replace('  ', ' ')
        # Remove known keywords from the back of the variant.
        variant = self._remove_keywords(variant)
        # Remove duplicate words
        variant = self._remove_duplicate_words(variant)

        # Don't add the entry if the variant becomes empty.
        if len(variant) == 0:
            return None

        # Selectively append "Diesel" or "Bensin" to indicate fuel type.
        if model in self._multi_fuel_models:
            for cc in self._multi_fuel_models[model]:
                if cc in variant:
                    fuel_type = self._multi_fuel_models[model][cc]
                    variant = variant + ' ' + fuel_type

        # Append "M/T" or "A/T" to indicate transmission.
        if transmission == 'Automatic':
            variant = variant + ' A/T'
        elif transmission == 'Manual':
            variant = variant + ' M/T'
        # else:
            # TODO. Raise error.

        # Fix known typos.
        for (typo, correction) in self._known_variant_typos.items():
            variant = variant.replace(typo, correction)

        # Merge minor variants.
        if brand in self._minor_variants:
            for phrase in self._minor_variants[brand]:
                variant = variant.replace(phrase + ' ', '')

        # TODO. Engine displacement should be consistently before/after variant.

        return variant

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
                and variant_words[-1] in [ 'Blind', 'High' ]):
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



    def export(self):
        brands = self._db.keys()
        for brand in brands:
            models = self._db[brand].keys()
            for model in models:
                years = self._db[brand][model].keys()
                for year in years:
                    variants = self._db[brand][model][year].keys()
                    for variant in variants:
                        self._export_single(brand, model, year, variant)

    def _export_single(self, brand, model, year, variant):
        assert brand in self._db
        assert model in self._db[brand]
        assert year in self._db[brand][model]
        assert variant in self._db[brand][model][year]
        assert len(self._db[brand][model][year][variant]) > 0
        stats = list(map(lambda x: x(self._db[brand][model][year][variant]),
            [ len, min, max, statistics.mean, statistics.median ]))
        print('%s,%s,%s,%s,%s,%s,%s,%s,%s'
            % (brand, model, year, variant,
                stats[0], stats[1], stats[2], stats[3], stats[4]))
