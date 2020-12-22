from requests import Session
from requests.auth import HTTPBasicAuth

from .exceptions import ApiError


class AppFollowAPI:
    API_URL = 'https://api.appfollow.io'

    def __init__(self, secret, session=None):
        self.secret = secret
        self.session = Session() if session is None else session

    def _api_call(self, path, params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        response = self.session.get(
            self.API_URL + path, params=params, auth=HTTPBasicAuth(self.secret, '')
        )

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
        return self._api_call(path='/apps', params={})

    def collection_apps(self, collection_id):
        return self._api_call(path='/apps/app', params={'apps_id': collection_id})

    def reviews(self, ext_id, **optionals):
        return self._api_call(path='/reviews', params={'ext_id': ext_id, **optionals})

    def reviews_summary(self, ext_id, **optionals):
        return self._api_call(
            path='/reviews/summary', params={'ext_id': ext_id, **optionals}
        )

    def review_reply(self, ext_id, review_id, answer_text, **optionals):
        return self._api_call(
            path='/reply',
            params={
                'ext_id': ext_id,
                'review_id': review_id,
                'answer_text': answer_text,
                **optionals,
            },
        )

    def review_update_tags(self, ext_id, review_id, tags: list, **optionals):
        return self._api_call(
            path='/tags/update',
            params={
                'ext_id': ext_id,
                'review_id': review_id,
                'tags': self.list_to_csv(tags),
                **optionals,
            },
        )

    def review_update_bug_trackers(self, ext_id, review_id, tags: list, **optionals):
        return self._api_call(
            path='/bt_tags/update',
            params={
                'ext_id': ext_id,
                'review_id': review_id,
                'tags': self.list_to_csv(tags),
                **optionals,
            },
        )

    def review_update_notes(self, ext_id, review_id, content):
        return self._api_call(
            path='/notes/update',
            params={'ext_id': ext_id, 'review_id': review_id, 'content': content},
        )

    def ratings(self, ext_id, **optionals):
        return self._api_call(path='/ratings', params={'ext_id': ext_id, **optionals})

    def versions(self, ext_id, **optionals):
        return self._api_call(path='/versions', params={'ext_id': ext_id, **optionals})

    def whats_new(self, ext_id, **optionals):
        return self._api_call(path='/whatsnew', params={'ext_id': ext_id, **optionals})

    def rankings(self, ext_id, **optionals):
        return self._api_call(path='/rankings', params={'ext_id': ext_id, **optionals})

    def keywords(self, ext_id, **optionals):
        return self._api_call(path='/keywords', params={'ext_id': ext_id, **optionals})

    def keywords_edit(self, country, device, keywords: list, **optionals):
        return self._api_call(
            path='/keywords/edit',
            params={
                'country': country,
                'device': device,
                'keywords': self.list_to_csv(keywords),
                **optionals,
            },
        )

    def aso_suggest(self, term, **optionals):
        return self._api_call(path='/aso/suggest', params={'term': term, **optionals})

    def aso_search(self, term, **optionals):
        return self._api_call(path='/aso/search', params={'term': term, **optionals})

    def aso_search_ads(self, app, country, **optionals):
        return self._api_call(
            path='/aso/search_ads', params={'app': app, 'country': country, **optionals}
        )

    def aso_trending(self, keyword, **optionals):
        return self._api_call(
            path='/aso/trending', params={'keyword': keyword, **optionals}
        )

    def app_analytics(self, ext_id, **optionals):
        return self._api_call(
            path='/app_analytics', params={'ext_id': ext_id, **optionals}
        )

    def aso_report(self, ext_id, channel, **optionals):
        return self._api_call(
            path='/reports/aso_report',
            params={'ext_id': ext_id, 'channel': channel, **optionals},
        )

    def reviews_stats(self, ext_id, **optionals):
        return self._api_call(
            path='/stat/reviews', params={'ext_id': ext_id, **optionals}
        )

    def reviews_stats_by_rating(self, ext_id, **optionals):
        return self._api_call(
            path='/stat/reviews/rating', params={'ext_id': ext_id, **optionals}
        )

    def reviews_stats_by_version(self, ext_id, **optionals):
        return self._api_call(
            path='/stat/reviews/version', params={'ext_id': ext_id, **optionals}
        )

    def reviews_stats_replies(self, ext_id, **optionals):
        return self._api_call(
            path='/stat/replies', params={'ext_id': ext_id, **optionals}
        )

    def reviews_stats_replies_speed(self, ext_id, **optionals):
        return self._api_call(
            path='/stat/replies/time', params={'ext_id': ext_id, **optionals}
        )

    def collection_reviews(self, collection_name, **optionals):
        return self._api_call(path=f'/{collection_name}/reviews', params=optionals)

    def reviews_custom_status(self, ext_id, review_id, custom_status):
        return self._api_call(
            path='/reviews/custom_status',
            params={
                'ext_id': ext_id,
                'review_id': review_id,
                'custom_status': custom_status,
            },
        )

    def ratings_export(self, collection_name, ext_id, **optionals):
        return self._api_call(
            path=f'/{collection_name}/ratings_export',
            params={'ext_id': ext_id, **optionals},
        )

    def reviews_featured(self, ext_id, **optionals):
        return self._api_call(
            path='/reviews/featured', params={'ext_id': ext_id, **optionals}
        )

    def reviews_reply_statistics(self, ext_id, **optionals):
        return self._api_call(
            path='/reviews/answer_count', params={'ext_id': ext_id, **optionals}
        )

    def countries(self):
        return self._api_call(path='/countries', params={})

    def aso_report_countries(self, ext_id):
        return self._api_call(
            path='/reports/aso_report/countries', params={'ext_id': ext_id}
        )

    def featured(self, ext_id, **optionals):
        return self._api_call(path='/feature', params={'ext_id': ext_id, **optionals})

    def top_charts(self, genre, device, country, date):
        return self._api_call(
            path='/rankings/topcharts',
            params={
                'genre': genre,
                'device': device,
                'country': country,
                'date': date,
            },
        )

    def report_a_concern(self, store, ext_id, concern_type, concern_explanation):
        return self._api_call(
            path='/reviews/concern',
            params={
                'store': store,
                'ext_id': ext_id,
                'concern_type': concern_type,
                'concern_explanation': concern_explanation,
            },
        )

    def downloads_revenue(self, ext_id, **optionals):
        return self._api_call(
            path='/downloads_revenue', params={'ext_id': ext_id, **optionals}
        )

    def add_collection(self, title, countries, **optional):
        return self._api_call(
            path='/apps/add',
            params={
                'title': title,
                'countries': self.list_to_csv(countries),
                **optional,
            },
        )

    def remove_collection(self, apps_id):
        return self._api_call(path='/apps/remove', params={'apps_id': apps_id})

    def add_app(self, apps_id, store, ext_id, locale, **optionals):
        return self._api_call(
            path='/app/add',
            params={
                'apps_id': apps_id,
                'store': store,
                'ext_id': ext_id,
                'locale': locale,
                **optionals,
            },
        )

    def remove_app(self, apps_id, store, ext_id, **optionals):
        return self._api_call(
            path='/app/delete',
            params={'apps_id': apps_id, 'store': store, 'ext_id': ext_id, **optionals},
        )

    def add_user(self, name, role, email, **optionals):
        return self._api_call(
            path='/users/add',
            params={'name': name, 'role': role, 'email': email, **optionals},
        )

    def remove_user(self, user_id):
        return self._api_call(path='/users/remove', params={'id': user_id})

    def update_user(self, user_id, name, role, email, **optionals):
        return self._api_call(
            path='/users/update',
            params={
                'id': user_id,
                'name': name,
                'role': role,
                'email': email,
                **optionals,
            },
        )

    @staticmethod
    def list_to_csv(arr):
        return ','.join(arr)
