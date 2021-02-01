import requests

base_url = "https://faucetpay.io/api/v1/"
api_parameters = [
	'api_key',
	'currency',
	'address',
	'amount',
	'to',
	'referral',
	'ip_address',
	'count'
]
methods = {
	'balance': ['checkBalance', 'myBalance', 'balance', 'getBalance',
				'check_balance', 'my_balance', 'get_balance'],
	'currencies': ['supportedCurrencies', 'currencies', 'availableCurrencies',
					'supported_currencies', 'available_currencies'],
	'checkaddress': ['checkAddress', 'checkaddress', 'isaddressexist'
					 'check_address', 'is_address_exist'],
	'send': ['send', 'sendTo', 'transfer', 'makeTx',
			 'send_to', 'make_tx', 'sendto', 'maketx'],
	'payouts': ['payouts', 'myPayouts', 'my_payouts'],
	'faucetlist': ['listFaucets', 'fetchRotator',
				   'list_faucets', 'fetch_rotator']
}

def callAPI(api_key, method, **kwargs):
	"""
	A function to dynamically make a POST request to FaucetPay with no try-catch
	blocks, supports any parameters as a Keyword Arguments.
	"""
	data = dict(
		api_key=api_key,
	)

	for key in api_parameters:
		if key in kwargs:
			data[key] = kwargs[key]

	res = requests.post(base_url + method, data=data)
	res = res.json()

	return res

class Api:
	def __init__(self, api_key):
		"""
		Creates an Api class for FaucetPay regular API access with api_key as
		an initial required argument
		"""
		self.api_key = api_key

	def __getattr__(self, attr):
		"""
		Dynamically returns a function for user to call. If you want to access
		specific endpoint with some parameters, please consider doing this:
		>>> # Example
		>>> myAPI.check_address(address="TestBTCAddress")
		{ ... JSON Response ... }
		>>> myAPI.check_address(address="TestDOGEAddress", currency="DOGE")
		{ ... JSON Response For DOGE ... }

		You do not need to provide api_key anymore since you already done that
		at class initialization.
		"""
		for key in methods:
			if attr in methods[key]:
				attr = key

		return (lambda **kwargs: callAPI(self.api_key, attr, **kwargs))
