# ob_samal_ploshad = 1000
# ob_mikro_ploshad = 500
# ob_orbita_ploshad = 2000
#
# ob_samal_freez_ploshad = 700
# ob_mikro_freez_ploshad = 400
# ob_orbita_ploshad = 300
#
# ob_samal_free_space =

class OvosheBaza:
    def __init__(self, overall_space: int, freeze_space, prorab_name, prorab_phone, occupied_overall_space, occupied_freeze_space):
        self.PRIORITY = 'freezer'
        self.overall_space = overall_space
        self.freeze_space = freeze_space
        self.non_freeze_space = overall_space - freeze_space
        self.prorab_info = {'prorab_name': prorab_name, 'prorab_phone': prorab_phone}
        self.occupied_overall_space = occupied_overall_space
        self.occupied_freeze_space = occupied_freeze_space
        self.occupied_non_freeze_space = occupied_overall_space - occupied_freeze_space

    def get_overall_available_space(self):
        remaining_overall_space = self.overall_space - self.occupied_overall_space
        return remaining_overall_space

    def get_freeze_available_space(self):
        return self.freeze_space - self.occupied_freeze_space

    def get_non_freeze_available_space(self):
        return self.non_freeze_space - self.occupied_non_freeze_space

    def add_protuct_to_sklad(self, amount_of_product, product_type):
        # if product_type == any:
        #     if amount_of_product <= self.get_overall_available_space():
        #
        if product_type == 'freeze':
            if amount_of_product <= self.get_freeze_available_space():
                self.occupied_freeze_space = self.occupied_freeze_space + amount_of_product
            else:
                raise ValueError('Not enough space! Try different sklad!')
        elif product_type == 'non_freeze':
            if amount_of_product <= self.get_non_freeze_available_space():
                self.occupied_non_freeze_space = self.occupied_non_freeze_space + amount_of_product
            else:
                raise ValueError('Not enough space! Try different sklad!')

    def transfer_products_from_different_sklad(self, drugoi_sklad, amount_of_product, product_type):
        if product_type == 'freeze':
            if amount_of_product <= self.get_freeze_available_space():
                if amount_of_product >= drugoi_sklad.get_freeze_available_space():
                    self.occupied_freeze_space = self.occupied_freeze_space + amount_of_product
                    drugoi_sklad.occupied_freeze_space = drugoi_sklad.occupied_freeze_space - amount_of_product
                else:
                    raise ValueError('Not enough space! Try take from different sklad!')
            else:
                raise ValueError('Not enough space! Try different sklad!')
        elif product_type == 'non_freeze':
            if amount_of_product <= self.get_non_freeze_available_space():
                if amount_of_product >= drugoi_sklad.get_non_freeze_available_space():
                    self.occupied_non_freeze_space = self.occupied_non_freeze_space + amount_of_product
                    drugoi_sklad.occupied_non_freeze_space = drugoi_sklad.occupied_non_freeze_space - amount_of_product
                else:
                    raise ValueError('Not enough space! Try take from different sklad!')
            else:
                raise ValueError('Not enough space! Try different sklad!')





samal = OvosheBaza(overall_space=1000, freeze_space=700, prorab_name='Vitaliy', prorab_phone='7771112233',
                   occupied_overall_space=600, occupied_freeze_space=400)
mikro = OvosheBaza(overall_space=500, freeze_space=400, prorab_name='Sasha', prorab_phone='7071112255',
                   occupied_overall_space=300, occupied_freeze_space=300)
orbita = OvosheBaza(overall_space=2000, freeze_space=300, prorab_name='Ergali', prorab_phone='7011112299',
                    occupied_overall_space=1000, occupied_freeze_space=0)

[samal, mikro, orbita]

a = 3
some_text = 'aaahahaahah'

print('ok')
