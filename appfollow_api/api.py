from hashlib import md5

from requests import Session

from .exceptions import ApiError


class AppFollowAPI:
    API_URL = 'https://api.appfollow.io'

    def __init__(self, cid, secret, session=Session()):
        self.cid = cid
        self.secret = secret
        self.session = session

    def _make_sign(self, path, params):
        sign = '{sorted_params}{path}{secret}'.format(
            sorted_params=''.join([f'{k}={params[k]}' for k in sorted(params.keys())]),
            path=path,
            secret=self.secret
        )
        return md5(sign.encode()).hexdigest()

    def _api_call(self, path, params):
        params['cid'] = self.cid
        if 'from_' in params:
            params['from'] = params.pop('from_')

        params['sign'] = self._make_sign(path, params)

        response = self.session.get(self.API_URL + path, params=params)

        if response.status_code == 502:
            raise ApiError('Bad Gateway', 502)
        elif response.status_code == 504:
            raise ApiError('Gateway Timeout', 504)
        else:
            response.raise_for_status()

        data = response.json()
        if isinstance(data, dict):
            err = data.get('error')
            if err:
                raise ApiError(**err)
        return data

    def collections(self):
        return self._api_call(
            path='/apps',
            params={}
        )

    def collection_apps(self, collection_id):
        return self._api_call(
            path='/apps/app',
            params={'apps_id': collection_id}
        )

    def reviews(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/reviews',
            params=optionals
        )

    def reviews_summary(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/reviews/summary',
            params=optionals
        )

    def review_reply(self, ext_id, review_id, answer_text, **optionals):
        optionals.update({
            'ext_id': ext_id,
            'review_id': review_id,
            'answer_text': answer_text,
        })
        return self._api_call(
            path='/reply',
            params=optionals
        )

    def review_update_tags(self, ext_id, review_id, tags: list, **optionals):
        optionals.update({
            'ext_id': ext_id,
            'review_id': review_id,
            'tags': self.list_to_csv(tags)
        })
        return self._api_call(
            path='/tags/update',
            params=optionals
        )

    def review_update_bug_trackers(self, ext_id, review_id, tags: list, **optionals):
        optionals.update({
            'ext_id': ext_id,
            'review_id': review_id,
            'tags': self.list_to_csv(tags)
        })
        return self._api_call(
            path='/bt_tags/update',
            params=optionals
        )

    def review_update_notes(self, ext_id, review_id, content):
        return self._api_call(
            path='/notes/update',
            params={
                'ext_id': ext_id,
                'review_id': review_id,
                'content': content
            }
        )

    def ratings(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/ratings',
            params=optionals
        )

    def versions(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/versions',
            params=optionals
        )

    def whats_new(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/whatsnew',
            params=optionals
        )

    def rankings(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/rankings',
            params=optionals
        )

    def keywords(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/keywords',
            params=optionals
        )

    def keywords_edit(self, country, device, keywords: list, **optionals):
        optionals.update({
            'country': country,
            'device': device,
            'keywords': self.list_to_csv(keywords)
        })
        return self._api_call(
            path='/keywords/edit',
            params=optionals
        )

    def aso_suggest(self, term, **optionals):
        optionals.update({'term': term})
        return self._api_call(
            path='/aso/suggest',
            params=optionals
        )

    def aso_search(self, term, **optionals):
        optionals.update({'term': term})
        return self._api_call(
            path='/aso/search',
            params=optionals
        )

    def aso_search_ads(self, app, country, **optionals):
        optionals.update({'app': app, 'country': country})
        return self._api_call(
            path='/aso/search_ads',
            params=optionals
        )

    def aso_trending(self, keyword, **optionals):
        optionals.update({'keyword': keyword})
        return self._api_call(
            path='/aso/trending',
            params=optionals
        )

    def app_analytics(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/app_analytics',
            params=optionals
        )

    def aso_report(self, ext_id, channel, **optionals):
        optionals.update({'ext_id': ext_id, 'channel': channel})
        return self._api_call(
            path='/reports/aso_report',
            params=optionals
        )

    def reviews_stats(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/stat/reviews',
            params=optionals
        )

    def reviews_stats_by_rating(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/stat/reviews/rating',
            params=optionals
        )

    def reviews_stats_by_version(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/stat/reviews/version',
            params=optionals
        )

    def reviews_stats_replies(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/stat/replies',
            params=optionals
        )

    def reviews_stats_replies_speed(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/stat/replies/time',
            params=optionals
        )

    def collection_reviews(self, collection_name, **optionals):
        return self._api_call(
            path=f'/{collection_name}/reviews',
            params=optionals
        )

    def reviews_custom_status(self, ext_id, review_id, custom_status):
        return self._api_call(
            path='/reviews/custom_status',
            params={
                'ext_id': ext_id,
                'review_id': review_id,
                'custom_status': custom_status
            }
        )

    def ratings_export(self, collection_name, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path=f'/{collection_name}/ratings_export',
            params=optionals
        )

    def reviews_featured(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/reviews/featured',
            params=optionals
        )

    def reviews_reply_statistics(self, ext_id, **optionals):
        optionals.update({'ext_id': ext_id})
        return self._api_call(
            path='/reviews/answer_count',
            params=optionals
        )

    def countries(self):
        return self._api_call(
            path='/countries',
            params={}
        )

    @staticmethod
    def list_to_csv(arr):
        return ','.join(arr)
