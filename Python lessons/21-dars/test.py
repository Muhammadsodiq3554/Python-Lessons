# JSON (JavaScript Object Notation) -> tuzilgan ma'lumotlarni taqdim etish uchun ishlatiladigan ma'lumotlar formati.

# p = '{"name": "Bob", "languages": ["English", "German", "Italian"]}'

import requests

url = "https://openai80.p.rapidapi.com/chat/completions"

payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
			"content": "Hello!"
		}
	]
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "a2b69e7f24msh2a8eba385bff20ep1d749cjsn4569bc2ed3f5",
	"X-RapidAPI-Host": "openai80.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())