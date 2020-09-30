def is_key_present(data_from_extruct, item):
    found = data_from_extruct.get(item)
    return False if found is None else True


data_from_extruct = {
    'start_time': 't-shirt',
    'end_time': 1235456311,
    'distance_fake': 10,
    'offer': None
}

try:
    price_from_extruct = data_from_extruct.get('offer', {}).get('amount')
except:
    print("offer is None")

offers_from_extruct = data_from_extruct.get('offer') or {}
price_from_extruct = offers_from_extruct.get('amount')

print(price_from_extruct)

# print(is_key_present(data_from_extruct, 'title'))
# print(is_key_present(data_from_extruct, 'hello'))


comparators = [is_key_present(data_from_extruct, 'start_time'),
               is_key_present(data_from_extruct, 'end_time_'),
               is_key_present(data_from_extruct, 'distance')]

print(comparators)
found_diffs = any([comp for comp in comparators])
print(found_diffs)
