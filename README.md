# AutoTraderSearch
Simple python console app to search auto trader via api and print results

Searches AutoTrader.com via the api available at autotrader.com/rest/searchresults/base

You can change the search parameters by altering the params dict

It's currently configured to print the price and milage of all cars found. I was attempting to use this to create a depreciation curve correlating milage with price for vehicles of a set make, model, and year. Unfortunately the data is a bit more complicated than that. Also prints the VIN (so you can reference or verify information later) and whether "nav" is listed as a feature.

I'd like to do some more work documenting valid parameters and the structure of the returned information. Unfortunately I'm not sure when or if I'll get the time. If that's something you'd like to work on, feel free to submit a Pull Request!
