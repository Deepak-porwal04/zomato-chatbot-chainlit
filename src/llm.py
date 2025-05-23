import os
from openai import OpenAI
from src.prompt import system_instruction

client = OpenAI()

messages = [
    {"role":"system","content":system_instruction}
]

import requests

def ask_order(messages, model_name="gpt-4.1-nano", max_tokens=10000, temperature=0.7):
    url = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": os.getenv("EURI_AUTH_HEADER")
    }
    payload = {
        "messages": messages, # [
        #     {
        #         "role": "user",
        #         "content": prompt
        #     }
        # ],
        "model": model_name,
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post(url, headers=headers, json=payload, verify=False)
    print(f"here is the response: \n\n {response}")
    data = response.json()
    res = data['choices'][0]['message']['content']
    # print(data)
    return res

# def ask_order(messages, model="gpt-3.5-turbo", temperature = 0):

#     response = client.chat.completions.create(
#         model = model,
#         messages= messages,
#         temperature = temperature
#     )

    # return response.choices[0].message.content