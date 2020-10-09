import json


def convert():
    stocks = []

    with open('../RU.txt', 'r') as data:
        for line in data:
            line = line.strip()
            ldata = line.split('\t')
            temp_stock = {
                'geonameid': ldata[0],
                'name': ldata[1],
                'asciiname': ldata[2],
                'alternatenames': ldata[3],
                'latitude': ldata[4],
                'longtitude': ldata[5],
                'feature_class': ldata[6],
                'feature_code': ldata[7],
                'country_code': ldata[8],
                'cc2': ldata[9],
                'admin1_code': ldata[10],
                'admin2_code': ldata[11],
                'admin3_code': ldata[12],
                'admin4_code': ldata[13],
                'population': ldata[14],
                'elevation': ldata[15],
                'dem': ldata[16],
                'timezone': ldata[17],
                'modification_date': ldata[18]
            }
            stocks.append(temp_stock)
    with open('../static/geonames.json', 'w') as fp:
        json.dump(stocks, fp, indent=4)


if __name__ == '__main__':
    convert()
