from sanic import Sanic
from sanic.response import text
from sanic.log import logger

import requests

app = Sanic(__name__, load_env='APP_')

# TOKEN = os.getenv("TOKEN")
URL = f'https://api.telegram.org/bot{TOKEN}/'
kv = {"User-Agent": "Mozilla/5.0"}


@app.route("/")
async def Index(request):
    return text('Welcome to Telegram Bot WebHook!')


@app.route('/<api>', methods=["GET", "POST"])
async def message_handler(request, api):
    query = request.url.split('/')[-1]
    url = f'{URL}{query}'
    req = requests.post(url=url, headers=kv)
    if req.status_code == 200:
        logger.info("Great,it's succeed! URL: %s", request.url)
    else:
        logger.info("Sorry,it's failed! URL: %s", request.url)


@app.route('/getWebhookInfo')
async def webHookInfo(request):
    method = 'getWebhookInfo'
    req = requests.get(url=URL+method, headers=kv)
    req.raise_for_status()
    if req.status_code == 200:
        logger.info("Get Webhook Info succeed! Webhook: %s", req.url)
    else:
        logger.info("Get Webhook Info failed!")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
