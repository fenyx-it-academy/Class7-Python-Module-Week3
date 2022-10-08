
def clean_result(dct):
    """clean up a result obj 
    return: dict - cleaned up version of the res obj.
    """

    new_dct = {
        "currency_of_choice": dct['base_code'],
        "date": dct['time_last_update_utc'],
        "conversion_rates": {
            "USD" : dct['conversion_rates']['USD'],
            "EUR" : dct['conversion_rates']['EUR'],
            "GBP" : dct['conversion_rates']['GBP'],
        }
    }

    return new_dct
