# FaucetPy
FaucetPay + Python = FaucetPy

# Installation
`pip3 install FaucetPy`

# Usage
```python
>>> from FaucetPy import Api
>>> myApi = Api("5f5f8031xxxxxxxxxxxxxxd6668b2249692ade5e")
>>> myApi.get_balance()
{'status': 200, 'message': 'OK', 'currency': 'BTC', 'balance': '0', 'balance_bitcoin': '0.00000000'}
>>> myApi.listFaucets()
{'status': 404, 'message': 'Invalid API method accessed.'}
>>> myApi.payouts()
{'status': 200, 'message': 'OK', 'rewards': []}
>>> myApi.my_payouts()
{'status': 200, 'message': 'OK', 'rewards': []}
```

# Endpoints and Its Aliases
`balance`: `checkBalance`, `myBalance`, `balance`, `getBalance`,
`check_balance`, `my_balance`, `get_balance`<br/>
`currencies`: `supportedCurrencies`, `currencies`, `availableCurrencies`,
`supported_currencies`, `available_currencies`<br/>
`checkaddress`: `checkAddress`, `checkaddress`, `isaddressexist`
`check_address`, `is_address_exist`<br/>
`send`: `send`, `sendTo`, `transfer`, `makeTx`,
`send_to`, `make_tx`, `sendto`, `maketx`<br/>
`payouts`: `payouts`, `myPayouts`, `my_payouts` <br/>
`faucetlist`: `listFaucets`, `fetchRotator`,
`list_faucets`, `fetch_rotator
