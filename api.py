import requests

class Proxy6:
    def __init__(self, api_key=False):
        self.api_domain = 'https://proxy6.net/api/'
        self.api_key = api_key


    def getprice(self, count=1, period=1, version=False):
        #version == 6 (default by proxy6)
        tmp_url = self.api_domain + self.api_key + '/getprice?count=' + count + '&period=' + period
        if version:
            tmp_url = tmp_url + '&version=' + version
        r = requests.get(tmp_url)
        if r.status_code == 503:
            return 'Too many requests'
        tmp_response = r.json()
        if tmp_response['status'] == 'no':
            return tmp_response['error_id']
        return tmp_response


    def getcount(self, country='ru', version=False):
        # version == 6 (default by proxy6)
        tmp_url = self.api_domain + self.api_key + '/getcount?country=' + country
        if version:
            tmp_url = tmp_url + '&version=' + version
        r = requests.get(tmp_url)
        if r.status_code == 503:
            return 'Too many requests'
        tmp_response = r.json()
        if tmp_response['status'] == 'no':
            return tmp_response['error_id']
        return tmp_response


    def getcountry(self, version=False):
        tmp_url = self.api_domain + self.api_key + '/getcountry'
        if version:
            tmp_url = tmp_url + '&version=' + version
        r = requests.get(tmp_url)
        if r.status_code == 503:
            return 'Too many requests'
        tmp_response = r.json()
        if tmp_response['status'] == 'no':
            return tmp_response['error_id']
        return tmp_response['list']


    def getproxy(self, state='active', descr=False, nokey=True):
        tmp_url = self.api_domain + self.api_key + '/getproxy&state=' + state
        if descr:
            tmp_url = tmp_url + '&descr=' + descr
        if nokey:
            tmp_url = tmp_url + '&nokey'
        r = requests.get(tmp_url)
        if r.status_code == 503:
            return 'Too many requests'
        tmp_response = r.json()
        if tmp_response['status'] == 'no':
            return tmp_response['error_id']
        if not 'list' in tmp_response.keys():
            return "Proxy list is empty"
        return tmp_response['list']


    def settype(self, ids=False, type='http'):
        #ids ONLY list
        #type only "http" or "socks"
        if ids == False:
            return "Empty id's"
        tmp_ids = ','.join(ids)
        tmp_url = self.api_domain + self.api_key + '/settype&ids=' + tmp_ids + '&type=' + type
        r = requests.get(tmp_url)
        if r.status_code == 503:
            return 'Too many requests'
        tmp_response = r.json()
        if tmp_response['status'] == 'no':
            return tmp_response['error_id']
        return True


    def setdescr(self):
        #https://proxy6.net/developers
        #Метод "setdescr"
        #Не считаю нужным
        return False


    def buy(self, count=1, period=30, country='ru', version=4, type='http', nokey=True):
        tmp_url = self.api_domain + self.api_key + '/buy&count=' + count + '&period=' + period + '&country=' + country + '&version=' + version + '&type=' + type
        if nokey:
            tmp_url = tmp_url + '&nokey'
        r = requests.get(tmp_url)
        if r.status_code == 503:
            return 'Too many requests'
        tmp_response = r.json()
        if tmp_response['status'] == 'no':
            return tmp_response['error_id']
        return tmp_response['list']


    def prolong(self, period=1, ids=False, nokey=True):
        if ids == False:
            return "Empty id's"
        tmp_ids = ','.join(ids)
        tmp_url = self.api_domain + self.api_key + '/prolong&ids=' + tmp_ids + '&period=' + period
        if nokey:
            tmp_url = tmp_url + '&nokey'
        r = requests.get(tmp_url)
        if r.status_code == 503:
            return 'Too many requests'
        tmp_response = r.json()
        if tmp_response['status'] == 'no':
            return tmp_response['error_id']
        return tmp_response['list']


    def delete(self, ids):
        if ids == False:
            return "Empty id's"
        tmp_ids = ','.join(ids)
        tmp_url = self.api_domain + self.api_key + '/delete&ids=' + tmp_ids
        r = requests.get(tmp_url)
        if r.status_code == 503:
            return 'Too many requests'
        tmp_response = r.json()
        if tmp_response['status'] == 'no':
            return tmp_response['error_id']
        return tmp_response


    def check(self):
        #https://proxy6.net/developers
        #Метод "check"
        #Не считаю нужным
        return False


if __name__ == "__main__":
    from pprint import pprint
    test = Proxy6()
    pprint(test.getproxy(state='all'))