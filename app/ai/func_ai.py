from app import config
import requests

API_KEY=config.API
url_auth = config.URL

async def ask_ai(user_message):

    payload = {"scope": "GIGACHAT_API_PERS"}
    headers_auth = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": "31d5d3d0-0cff-489f-9366-10b94fd06209",
        "Authorization": f"Basic {API_KEY}",
    }

    auth_resp = requests.post(url_auth, headers=headers_auth, data=payload, verify=False)
    token = auth_resp.json().get("access_token")

    # 2. Запрос в нейронку
    url_chat = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    headers_chat = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    body = {
        "model": "GigaChat",
        "messages": [
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 512,
    }

    chat_resp = requests.post(url_chat, headers=headers_chat, json=body, verify=False)
    data = chat_resp.json()

    # 3. Достаём текст ответа
    try:
        text_answer = data["choices"][0]["message"]["content"]
    except Exception:
        text_answer = str(data)

    return text_answer


# создать здесь функцию запроса к нейронке и написать комманды в БД