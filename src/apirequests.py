import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

def send_message(user_input, model="gpt-3.5-turbo"):
    """
    Sends a message to the OpenAI API and appends the response to the conversation history.

    Args:
        user_input (str): The latest input from the user.
        model (str): The model to use (default: "gpt-3.5-turbo").

    Returns:
        str: The model's response.
    """
    # Add user input to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    try:
        # Send the conversation history to the model
        response = openai.ChatCompletion.create(
            model=model,
            messages=conversation_history,
            max_tokens=500,
            temperature=0.7
        )
        # Extract the assistant's response
        assistant_response = response['choices'][0]['message']['content']
        # Add the assistant's response to the conversation history
        conversation_history.append({"role": "assistant", "content": assistant_response})
        return assistant_response
    except Exception as e:
        return f"Error: {e}"
