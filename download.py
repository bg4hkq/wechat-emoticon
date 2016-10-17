import json
import requests


f=open('emoticons.json','r')

jcontent = f.read()

jv = json.loads(jcontent)



for i in jv:
    r = requests.get(i['url'])
    with open("pics/" + i['md5']+'.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()
