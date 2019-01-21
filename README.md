# AppFollow API
A Python 3.6 wrapper for the [AppFollow API](https://appfollow.docs.apiary.io/#).

# Installation
`pip install appfollow_api`

# Usage
To execute AppFollow APIs, you need your API secret and cleint ID. 
You can get them in [account settings](http://watch.appfollow.io/settings/general)  
For the details about the API, see [apiary](https://appfollow.docs.apiary.io/#).
```python
from appfollow_api import AppfollowApi

cid = '966'
api_secret = 'AppFollow-966-2b3da05ee'

api = AppfollowApi(cid, api_secret)
data = api.collections()
```