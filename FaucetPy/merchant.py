import requests
merchant_url = 'https://faucetpay.io/merchant/'

class Merchant:
	def __init__(self, merchant_username):
		"""
		Create a class for Merchant (Beta) API endpoint access
		https://faucetpay.io/merchant
		"""
		self.merchant_username = merchant_username

	def get_payment(self, token):
		"""
		A function to get payment detail from token with these details:
		 - transaction_id
		 - merchant_username
		 - amount1
		 - currency1
		 - amount2
		 - currency2
		 - custom
		"""
		res = requests.post(f"{merchant_url}get-payment/{token}")
		res = res.json()

		return res
