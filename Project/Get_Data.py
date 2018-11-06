import requests, json

initial_request = 'https://whattomine.com/coins.json?utf8=✓&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=0&adapt_q_570=0&adapt_q_580=0&adapt_q_vega56=0&adapt_q_vega64=0&adapt_q_750Ti=0&adapt_q_1050Ti=0&adapt_q_10606=0&adapt_q_1070=0&adapt_q_1070Ti=0&adapt_q_1080=0&adapt_q_1080Ti=8&adapt_1080Ti=true&adapt_q_2080=0&eth=true&factor%5Beth_hr%5D=396.0&factor%5Beth_p%5D=1520.0&zh=true&factor%5Bzh_hr%5D=504.0&factor%5Bzh_p%5D=1600.0&cns=true&factor%5Bcns_hr%5D=8000.0&factor%5Bcns_p%5D=1200.0&cnh=true&factor%5Bcnh_hr%5D=8000.0&factor%5Bcnh_p%5D=1200.0&cn7=true&factor%5Bcn7_hr%5D=6800.0&factor%5Bcn7_p%5D=1200.0&cn8=true&factor%5Bcn8_hr%5D=5760.0&factor%5Bcn8_p%5D=1200.0&lre=true&factor%5Blrev2_hr%5D=592000.0&factor%5Blrev2_p%5D=1520.0&ns=true&factor%5Bns_hr%5D=15200.0&factor%5Bns_p%5D=1520.0&tt10=true&factor%5Btt10_hr%5D=332.0&factor%5Btt10_p%5D=1600.0&x16r=true&factor%5Bx16r_hr%5D=192.0&factor%5Bx16r_p%5D=1520.0&l2z=true&factor%5Bl2z_hr%5D=45.6&factor%5Bl2z_p%5D=1520.0&phi2=true&factor%5Bphi2_hr%5D=71.2&factor%5Bphi2_p%5D=1600.0&xn=true&factor%5Bxn_hr%5D=55.2&factor%5Bxn_p%5D=1520.0&hx=true&factor%5Bhx_hr%5D=136.0&factor%5Bhx_p%5D=1600.0&phi=true&factor%5Bphi_hr%5D=324.0&factor%5Bphi_p%5D=1600.0&ppw=true&factor%5Bppw_hr%5D=156.0&factor%5Bppw_p%5D=1680.0&factor%5Bcost%5D=0.0&sort=Profitability7&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=cryptobridge&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate'

json_data = requests.get(initial_request)
dict_data = json.loads(json_data.text)

coin_list = []
for k in dict_data['coins']:
    coin_list.append(k)


'''
max_dict ={}
max_prof = 0
for k in dict_data['coins']:
    print(k, dict_data['coins'][k]['profitability'])
    if dict_data['coins'][k]['profitability'] > max_prof:
        max_prof = dict_data['coins'][k]['profitability']
        max_dict = {k: max_prof}
'''

