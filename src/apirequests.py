from openai import OpenAI
import functions
import os


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  
)


def send_prompt(messages, model="gpt-3.5-turbo"):
    """
    Communicates with the ChatGPT API and returns either a message or a function call based on the response.

    Parameters:
        - messages (list): List of message objects to send to the model.
        - model (str): The model to use, e.g., "gpt-4".

    Returns:
        - str: The response, either a message or a function call result.
    """
    try:
        # Send the messages to the API
        response = client.chat.completions.create(
            messages=messages,
            model=model
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f"An error occurred: {str(e)}"
