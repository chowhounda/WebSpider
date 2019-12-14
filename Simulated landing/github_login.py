import requests
from lxml import etree


class GithubLogin(object):
    def __init__(self):
        self.headers = {
            'Host': 'github.com',
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def get_token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//*[@id="login"]/form/input[2]/@value')[0]
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            # self.dynamics(response.text)
            pass

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    # def dynamics(self, html):
    #     selector = etree.HTML(html)
    #     dynamics = selector.xpath('//*[contains(@class, "news")]//*[contains(@class, "alert")]')
    #     for item in dynamics:
    #        dynamic = ' '.join(item.xpath('.//*[@class="title"]//text()')).strip()
    #        print(dynamic)

    def profile(self, text):
        print(text)


if __name__ == '__main__':
    login = GithubLogin()
    login.login(email='chowhoundw@sina.com', password='')
