from rdw.rdw import Rdw

KENTEKEN = "50NNR6"

car = Rdw()

# Base car data
car_data = car.get_vehicle_data(KENTEKEN)

# Fuel data, includes electric cars
fuel_data = car.get_fuel_information(KENTEKEN)

print(fuel_data)

dimensions = {
    'make': car_data['merk'].lower(),
    'model': car_data['handelsbenaming'],
    'type': car_data['europese_voertuicategorie'],
    'vehicle_type': car_data['voertuigsoort'],
    'width': car_data['breedte'],
    'length': car_data['lengte'],
    'weight_empty': car_data['massa_ledig_voertuig'],
    'weight_on_road': car_data['massa_rijklaar'],
    'new_price': car_data['catalogusprijs'],
    'build_year': car_data['datum_eerste_toelating']
}

if car_data['voertuigsoort'] == 'Motorfiets':
    pass
    # Road tax is 11 per month
    # Fuel data needs to come from somewhere else

# TODO Get spritmonitor data
# url https://www.spritmonitor.de/en/overview/48-Suzuki/915-DL_650_V-Strom.html?sort=3&powerunit=2
# Spritmonitor API https://api.spritmonitor.de/doc
# Spritmonitor stores data as l/100km
# Fuelly https://www.fuelly.com/motorcycle/suzuki/dl650_v-strom

# TODO map names from RDW -> Spritmonitor -> Fuelly -> AutoScout?

# info on types
# https://github.com/hongaar/motorrijtuigenbelasting/blob/main/packages/rdw/src/index.ts

# All suzuki types from Fuelly
# https://www.fuelly.com/motorcycle/suzuki

print(dimensions)
