import hashlib
import random
import requests
from pathlib import Path


this_dir = Path(__file__).absolute().parents[0].parents[0]
#print(this_dir)
apiURL = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
defaultAccount = {'id':'20151113000005349', 'key':'osubCEzlGjzvw8qdQc41'}

def getID_and_Key():
    try:
        id_key = open("%s/id&key.ini" % this_dir).read().split('\n')
        appID = id_key[0].split(':')[1]
        secretKey = id_key[1].split(':')[1]
    except:
        # 感谢CSDN博主LCYong_提供的appid和秘钥，原网址：https://blog.csdn.net/lcyong_/article/details/79068636
        appID = defaultAccount['id']
        secretKey = defaultAccount['key']
        open("%s/id&key.ini" % this_dir,'w').write('appID:%s\nkey:%s' % (appID, secretKey))
    # print(appID, secretKey)
    return appID, secretKey


def baiduAPI_translate(query_str, to_lang):
    appID, secretKey = getID_and_Key()
    trytime = 20
    while trytime:
        salt = str(random.randint(32768, 65536))
        pre_sign = appID + query_str + salt + secretKey
        sign = hashlib.md5(pre_sign.encode()).hexdigest()
        params = {
            'q': query_str,
            'from': 'auto',
            'to': to_lang,
            'appid': appID,
            'salt':salt,
            'sign': sign
        }
        try:
            response = requests.get(apiURL, params=params)
            result_dict = response.json()
            if 'trans_result' in result_dict:
                return result_dict
            else:
                print('Some errors occured:\n', result_dict)
                trytime -= 1
        except Exception as e:
            print('Some errors occured: ', e)
            trytime -= 1


def baidu_translate(query_str, dst_lang=''):

    if dst_lang:
        result_dict = baiduAPI_translate(query_str, dst_lang)
    else:
        result_dict = baiduAPI_translate(query_str, 'zh')
        if result_dict['from'] == 'zh':
            result_dict = baiduAPI_translate(query_str, 'en')
    # dst = result_dict['trans_result'][0]['dst']
    # print('{}: {} -> {}: {}'.format(result_dict['from'], query_str, result_dict['to'], dst))
    return result_dict


if __name__ == '__main__':
    baidu_translate('This is English.')
    baidu_translate('这是中文')
    baidu_translate('翻译成法语', 'fra')
