# Installation
1. Download the archive:  
wget:  
`wget --no-check-certificate --content-disposition https://github.com/AppFollow/appfollow-api-python/archive/master.zip`  
or curl:  
`curl -LJO https://github.com/AppFollow/appfollow-api-python/archive/master.zip`  
or git:  
`git clone https://github.com/AppFollow/appfollow-api-python`

2. Install:  
`sudo python setup.py install`

# Usage
To execute AppFollow APIs, you need your API secret and cleint ID.  
You can get them in [account settings](http://watch.appfollow.io/settings/general).  
For the details about the API, see [apiary](https://appfollow.docs.apiary.io/#).

```python
from appfollow_api import AppFollowAPI

cid = '966'
api_secret = 'AppFollow-966-2b3da05ee'

api = AppFollowAPI(cid, api_secret)
data = api.collections()
```

You can pass your `requests.session` objects into api:
```python
...
api = AppFollowAPI(cid, api_secret, session=session)
...
```
