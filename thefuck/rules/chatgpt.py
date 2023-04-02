import os
from thefuck.shells import shell
import requests
import json
from thefuck.conf import settings

def match(command):
    return True


def get_new_command(command):
    return shell.and_('hi hi')

def get_output(command):
    # Replace with your own API key
    api_key = settings.get("openai_key")

    # Define the API endpoint
    url = "https://api.openai.com/v1/chat/completions"

    # Set the headers for the API call
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Define the API request payload
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content":"""I am using command line and have typed the following command:
""" + command.script + """

After that I have received the following output:
""" + command.output + """
Can you explain what happened? What did the command do and what does the output mean? If the result is undesirable, which command would produce a desirable result?"""}],
        "max_tokens": 512,
        "n": 1,
        "stop": None,
        "temperature": 0.7
    }

    # Make the API call
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Parse the response
    response_data = json.loads(response.text)

    # Get the generated code
    # generated_code = response_data["choices"][0]["text"]

    # # Print the generated code
    # print(generated_code)
    return response_data["choices"][0]["message"]["content"]