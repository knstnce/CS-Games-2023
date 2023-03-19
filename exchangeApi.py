import requests

# https://www.exchangerate-api.com/
API_KEY = "2e1c41396f473115488c4907"
# taken from: https://www.exchangerate-api.com/docs/supported-currencies
SUPPORTED_CURRENCY_CODES = {"AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SOS", "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XCD", "XDR", "XOF", "XPF", "YER", "ZMW", "ZWL" }


#1
def get_currency_information(currency_code: str) -> dict:
    if not currency_code:
        raise Exception('Please pass in a valid currency_code (as lised: https://www.exchangerate-api.com/docs/supported-currencies')
    if currency_code not in SUPPORTED_CURRENCY_CODES:
        raise Exception(f'Currency code "{currency_code}" not supported, please try one of "{SUPPORTED_CURRENCY_CODES}"')

    return requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency_code}').json()

#2
def get_supported_currency_codes() -> set[str]:
    return SUPPORTED_CURRENCY_CODES

#3
def get_currency_conversions(currency_code: str) -> dict:
    currency_information = get_currency_information(currency_code)
    if 'conversion_rates' not in currency_information:
        raise Exception(f'The provided currency "{currency_code}" does not have conversion rates available at this time')
    return currency_information['conversion_rates']

def convert_currencies(*, from_currency_amount: float, from_currency_code: str, to_currency_code: str) -> float:
    from_currency_conversions = get_currency_conversions(from_currency_code)
    if to_currency_code not in from_currency_conversions:
        raise Exception(f'The provided currency "{from_currency_code}" cannot be converted to "{to_currency_code}"')
    return float(from_currency_conversions[to_currency_code]) * from_currency_amount