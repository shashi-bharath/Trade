import kiteconnect
import math

positions = [{'tradingsymbol': 'BANKNIFTY22JUL37000CE', 'exchange': 'NFO', 'instrument_token': 13928194, 'product': 'MIS', 'quantity': 25, 'overnight_quantity': 0, 'multiplier': 1, 'average_price': 112.65, 'close_price': 0, 'last_price': 120.00, 'value': 183.75, 'pnl': 183.75, 'm2m': 183.75, 'unrealised': 183.75, 'realised': 0, 'buy_quantity': 25, 'buy_price': 112.65, 'buy_value': 2816.25, 'buy_m2m': 2816.25, 'sell_quantity': 25, 'sell_price': 120, 'sell_value': 3000, 'sell_m2m': 3000, 'day_buy_quantity': 25, 'day_buy_price': 112.65, 'day_buy_value': 2816.25, 'day_sell_quantity': 25, 'day_sell_price': 120, 'day_sell_value': 3000}, {'tradingsymbol': 'INFY', 'exchange': 'NSE', 'instrument_token': 408065, 'product': 'MIS', 'quantity': 0, 'overnight_quantity': 0, 'multiplier': 1, 'average_price': 0, 'close_price': 0, 'last_price': 1503.5, 'value': -2.75, 'pnl': -2.75, 'm2m': -2.75, 'unrealised': -2.75, 'realised': 0, 'buy_quantity': 1, 'buy_price': 1508.3, 'buy_value': 1508.3, 'buy_m2m': 1508.3, 'sell_quantity': 1, 'sell_price': 1505.55, 'sell_value': 1505.55, 'sell_m2m': 1505.55, 'day_buy_quantity': 1, 'day_buy_price': 1508.3, 'day_buy_value': 1508.3, 'day_sell_quantity': 1, 'day_sell_price': 1505.55, 'day_sell_value': 1505.55}, {'tradingsymbol': 'TATAMOTORS', 'exchange': 'NSE', 'instrument_token': 884737, 'product': 'MIS', 'quantity': 0, 'overnight_quantity': 0, 'multiplier': 1, 'average_price': 0, 'close_price': 0, 'last_price': 449.3, 'value': 1.1999999999999886, 'pnl': 1.1999999999999886, 'm2m': 1.1999999999999886, 'unrealised': 1.1999999999999886, 'realised': 0, 'buy_quantity': 1, 'buy_price': 449.25, 'buy_value': 449.25, 'buy_m2m': 449.25, 'sell_quantity': 1, 'sell_price': 450.45, 'sell_value': 450.45, 'sell_m2m': 450.45, 'day_buy_quantity': 1, 'day_buy_price': 449.25, 'day_buy_value': 449.25, 'day_sell_quantity': 1, 'day_sell_price': 450.45, 'day_sell_value': 450.45}]
def get_request_key():
    api = "0gje3yks6vggm0w9"
    secret = "6tznb7ww9wkq2h9k9o595utjswzx2d5h"
    request_token="lsoA5xm8b7kShVdh6tMJ7nzTq6KncFv5"
    kite = kiteconnect.KiteConnect(api_key = api)
    url = kite.login_url()
    print(url)

    # data = kite.generate_session(request_token, api_secret=secret)
    # var1 = kite.set_access_token(data["access_token"])
    # bal = kite.margins()['equity']['net']
    # print("Balance:", bal)

    margin = 1000 * (5/100)
    #print(kite.orders())

    #positions = kite.positions()['net']

    #print(positions)
    # pnl_total = 0
    # for pos in positions:
    #     if pos['product'] == 'MIS':
    #         if pos['quantity'] < 1:
    #             print("Inside MIS")
    #             m2m_value = pos['m2m']
    #             profit = (int(pos['average_price']) - int(pos['last_price'])) * abs(pos['quantity'])
    #             pnl_total = pnl_total + profit
    #             #print("Profit for %s is %s" %(pos['tradingsymbol'], profit))
    #         elif pos['quantity'] >= 1:
    #             m2m_value = pos['m2m']
    #             profit = (pos['last_price'] - pos['average_price']) * pos['quantity']
    #             pnl_total = pnl_total + profit
    #             #print("Profit for %s is %s" %(pos['tradingsymbol'], profit))
    #     if pnl_total < -(margin):
    #         kite.
        

get_request_key()