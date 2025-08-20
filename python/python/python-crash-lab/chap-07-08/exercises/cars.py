def car_info(
        manufacturer, model, **extra_details):
    extra_details['manufacturer_name'] = manufacturer
    extra_details['model_name'] = model
    return extra_details

car_id = car_info('toyota', 'lexus rx 350 2017', colour='red', tow_package=True )
print(car_id)