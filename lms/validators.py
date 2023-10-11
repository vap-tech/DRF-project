import re
from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url_field = dict(value).get(self.field)
        url_pattern = r'https?://\S+|www\.\S+'
        youtube_pattern = r'(?:https?://)?(?:www\.)?youtube\.com'
        all_url = re.findall(url_pattern, url_field)
        for url in all_url:
            if not bool(re.match(youtube_pattern, url)):
                raise ValidationError(f'Можно добавлять только ссылки на youtube, но не {url}')
