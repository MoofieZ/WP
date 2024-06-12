import requests

def get_sensitive_data(key):
    sensitive_data = {
        'WORDPRESS_SITE': 'https://your-wordpress-site.com',  # Replace with your WordPress site URL
        'WORDPRESS_USER': 'your-username',  # Replace with your WordPress username
        'WORDPRESS_APP_PASSWORD': 'your-app-password',  # Replace with your WordPress application password
        'OPENAI_API_KEY': ''  # Replace with your OpenAI API key
    }
    return sensitive_data[key]

TITLE = 'Sample Blog Post via API'
CONTENT = '<p>This is a sample blog post created via the WordPress API.</p>'

def create_post(wordpress_site, username, password, title, content):
    url = f"{wordpress_site}/wp-json/wp/v2/posts"
    headers = {
        "Content-Type": "application/json",
    }
    auth = (username, password)
    body = {
        'title': title,
        'content': content,
        'status': 'publish',
        'categories': [1],  # Replace with appropriate category IDs
        'tags': [1, 2, 3]  # Replace with appropriate tag IDs
    }
    response = requests.post(url, json=body, headers=headers, auth=auth)
    if response.status_code == 201:
        print("Post created successfully:", response.json())
    else:
        print("Error:", response.status_code, response.text)

def openai(message):
    openai_api_key = get_sensitive_data('OPENAI_API_KEY')
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "temperature": 0.2,
        "max_tokens": 4095,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print("Error:", response.status_code, response.text)

def create():
    message = "Give me a joke"
    resp = openai(message)
    wordpress_site = get_sensitive_data('WORDPRESS_SITE')
    username = get_sensitive_data('WORDPRESS_USER')
    password = get_sensitive_data('WORDPRESS_APP_PASSWORD')
    for i in range(1, 6):
        create_post(wordpress_site, username, password, f"{TITLE} {i}", resp)

create()
