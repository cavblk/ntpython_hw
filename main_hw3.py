import csv
import hashlib
import os
import json

output_data_dir = 'output_data'


def generate_id(list):
    stri = list.__str__()
    # print("Stri="+stri)
    """
    Generate an id for an string/array
    :param list: list
    :return: digest of encoded stringed list 
    """
    hash_list = hashlib.md5(stri.encode()).hexdigest()
    # print(hash_list)
    return hash_list


def get_hdr_cars():
    with open('homework_example.csv', 'r') as in_file:
        rows = csv.reader(in_file, delimiter=',')
        # print(type(rows).__name__)
        # headers = ['Id'].append(rows[0])
        cars = [r for r in rows]
        headers = cars[0]
        cars.pop(0)  # remove header from cars list

        headers.insert(0, 'Id')  # Put an Id column at beginning of header

        # Strip headers of whitespaces
        # print(headers)
        headers = [x.strip() for x in headers]
        # print(headers)

        for car in cars:
            # print(car, type(car).__name__)
            id = generate_id(car)
            # print(f'id={id}, type={type(id)}')
            car.insert(0, id)  # insert id for each car at the beginning of car

        # print(cars)
        return headers, cars


def generate_car_dict(car):
    # print(f'Dict for car {car[0]}')
    car_dict = {k: v for k, v in zip(header, car)}
    # print(car_dict)
    return car_dict


def prepare_dir():
    access_rights = 0o755
    is_dir = os.path.isdir(output_data_dir)
    if is_dir:
        for file in os.listdir(output_data_dir):
            try:
                os.remove(output_data_dir + os.sep + file)
            except OSError as error:
                print("Deletion of the directory %s failed" % output_data_dir)
                print(error)
            else:
                print("Successfully deleted file %s of the directory %s" % (file, output_data_dir))

        try:
            os.rmdir(output_data_dir)
        except OSError as error:
            print("Deletion of the directory %s failed" % output_data_dir)
            print(error)
            is_dir = True
        else:
            print("Successfully deleted the directory %s" % output_data_dir)
            is_dir = False

    if not is_dir:
        try:
            os.mkdir(output_data_dir, access_rights)
        except OSError:
            print("Creation of the directory %s failed" % output_data_dir)
            is_dir = False
        else:
            print("Successfully created the directory %s" % output_data_dir)
            is_dir = True
    return is_dir


def slow_cars(car_dict_list):
    slow_cars_list = [k for k in car_dict_list if int(k.get('hp')) < 120]
    slow_cars_list_dict = dict(slow_cars=slow_cars_list)
    with open(os.path.join(output_data_dir, 'slow_cars.json'), 'w') as f:
        json.dump(slow_cars_list_dict, f, indent=4)


def fast_cars(car_dict_list):
    fast_cars_list = [k for k in car_dict_list if 120 <= int(k.get('hp')) < 180]
    fast_cars_list_dict = dict(fast_cars=fast_cars_list)
    with open(os.path.join(output_data_dir, 'fast_cars.json'), 'w') as f:
        json.dump(fast_cars_list_dict, f, indent=4)


def sport_cars(car_dict_list):
    sport_cars_list = [k for k in car_dict_list if int(k.get('hp')) >= 180]
    sport_cars_list_dict = dict(sport_cars=sport_cars_list)
    with open(os.path.join(output_data_dir, 'sport_cars.json'), 'w') as f:
        json.dump(sport_cars_list_dict, f, indent=4)


def cheap_cars(car_dict_list):
    cheap_cars_list = [k for k in car_dict_list if int(k.get('price')) < 1000]
    cheap_cars_list_dict = dict(cheap_cars=cheap_cars_list)
    with open(os.path.join(output_data_dir, 'cheap_cars.json'), 'w') as f:
        json.dump(cheap_cars_list_dict, f, indent=4)


def medium_cars(car_dict_list):
    medium_cars_list = [k for k in car_dict_list if 1000 <= int(k.get('price')) < 5000]
    medium_cars_list_dict = dict(medium_cars=medium_cars_list)
    with open(os.path.join(output_data_dir, 'medium_cars.json'), 'w') as f:
        json.dump(medium_cars_list_dict, f, indent=4)


def expensive_cars(car_dict_list):
    expensive_cars_list = [k for k in car_dict_list if int(k.get('price')) >= 5000]
    expensive_cars_list_dict = dict(expensive_cars=expensive_cars_list)
    with open(os.path.join(output_data_dir, 'expensive_cars.json'), 'w') as f:
        json.dump(expensive_cars_list_dict, f, indent=4)


def generate_brand_files(car_dict_list):
    brand_set = set([k.get('brand') for k in car_dict_list])
    print(brand_set)
    for brand in brand_set:
        brand_cars_list = [k for k in car_dict_list if k.get('brand') == brand]
        brand_cars_list_dict = {brand: brand_cars_list}
        with open(os.path.join(output_data_dir, brand) + '.json', 'w') as f:
            json.dump(brand_cars_list_dict, f, indent=4)


header, cars = get_hdr_cars()

my_car_dict_list = []

print('Outside')

for c in cars:
    # print(c)
    my_car_dict_list.append(generate_car_dict(c))
print('-----')
print(my_car_dict_list)

if prepare_dir():
    slow_cars(my_car_dict_list)
    fast_cars(my_car_dict_list)
    sport_cars(my_car_dict_list)
    cheap_cars(my_car_dict_list)
    medium_cars(my_car_dict_list)
    expensive_cars(my_car_dict_list)
    generate_brand_files(my_car_dict_list)
