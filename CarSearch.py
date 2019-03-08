import requests

url = 'https://www.autotrader.com/rest/searchresults/base'

params = dict(
    zip=40291,
    makeCodeList='HONDA',
    modelCodeList='FIT',
    marketExtension='true',
    #maxMileage=75000,
    startYear=2011,
    endYear=2011,
    searchRadius=0,
    maxPrice=200000,
    sortBy='mileageASC',
    numRecords=100,
    firstRecord=0
)

headers = {
    'Cache-Control': 'no-cache',
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

resp = requests.get(url=url, params=params, headers=headers)

data = resp.json()

for listing in data['listings']:
    print(listing['specifications']['mileage']['value'].replace(',', ''), end='\t')
    print(listing['pricingDetail']['primary'], end='\t')

    if('vin' in listing):
        print(listing['vin'], end='\t')
    else:
        print('-----------------', end='\t')

    if 'features' in listing:
        for feature in listing['features']:
            if('nav' in feature.lower()):
                print('Has Nav', end='\t')

    if(listing['specifications']['mileage']['label'] != 'miles'):
        print("ERROR mileage not in miles")
    else:
        print()
