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
	'listv1/faucetlist': ['listFaucets', 'fetchRotator',
						  'list_faucets', 'fetch_rotator']
}

def callAPI(api_key, method, **kwargs):
	data = dict(
		api_key=api_key,
	)

	for key in api_parameters:
		if kwargs[key]:
			data[key] = kwargs[key]

	res = requests.post(base_url + method, data=data)
	res = res.json()

	return res

class API:
	def __init__(self, api_key):
		self.api_key = api_key

	def __getattr__(self, attr):
		for key, value in methods:
			if attr in value:
				attr = key

		return (lambda **kwargs: callAPI(self.api_key, attr, **kwargs))
