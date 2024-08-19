import sys
import antigravity

def check_date(date):
    if len(date) != 10:
        return False
    
    if date[4] != '-' or date[7] != '-':
        return False
    
    for char in date.replace('-', ''):
        if not char.isdigit():
            return False
        
    return True

def get_geohash(arg1, arg2, date, dow):
    try:
        lat = float(arg1)
        lon = float(arg2)
        dow_float = float(dow)
    except:
        print('Latitude, longitude, and Dow price need to be float')
        exit()

    if not check_date(date):
        print('Date need to be in YYYY-MM-DD format')
        exit()

    datedow = f'{date}-{dow}'
    datedow_buffer = datedow.encode('utf-8')
    antigravity.geohash(lat, lon, datedow_buffer)


if __name__ == '__main__':
    if len(sys.argv) == 5:
        get_geohash(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print('4 arguments expected:\nLatitude / Longitude / Date / Dow opening price')