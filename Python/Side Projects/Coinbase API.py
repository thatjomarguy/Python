import requests
from coinbase.wallet.client import Client

# def feesRequest():
#     bankFee = float(price.amount)*.0149
#     cardFee = float(price.amount)*.0399
#     coinbaseFee = float(price.amount)*.0149

#     print('\nFees')
#     print('U.S. Bank Fee: ' + str(bankFee))
#     print('Credit/Debit Fee: ' + str(cardFee))
#     print('Coinbase USD Wallet Fee: ' + str(coinbaseFee))

def main():

    apiKey = "PX2fmy32cWHRZs4c"
    apiSecret = "NC3rc0lo2QShxy1puOUVx8UvR6oos8fh"

    client = Client(apiKey, apiSecret)
    time = client.get_time()
    currency_code = 'USD'

    price = client.get_spot_price(currency=currency_code)
    print('Current: ' + price.amount)
    buyPrice = client.get_buy_price(currency=currency_code)
    print('Buy: ' + buyPrice.amount)
    sellPrice = client.get_sell_price(currency=currency_code)
    print('Sell: ' + sellPrice.amount)

    print('\nTime: ' + str(time['iso']))

if __name__ == "__main__":
    main()
