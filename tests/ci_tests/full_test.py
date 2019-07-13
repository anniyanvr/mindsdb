from tests import basic_test


# Cycle through a few options:
for backend in ['ludwig','lightwood']:
    for use_gpu in [True,False]:
        basic_test(backend='ludwig',use_gpu=False,ignore_columns=[])

# Try ignoring some columns
basic_test(backend='lightwood',use_gpu=True,ignore_columns=['days_on_market','number_of_bathrooms'])
print('\n\n=============[Success]==============\nFinished running full test suite !\n=============[Success]==============\n\n')
