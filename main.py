import openai
import os



# Set your OpenAI API key
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

def generate_email(prompt):
    # Set the model name and other parameters
    model = 'gpt-3.5-turbo-instruct'  # You can choose a different model based on your needs
    # model = 'text-gpt-3.5-turbo'
    temperature = 0.7
    max_tokens = 500

    # Make the API request
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    # Extract and return the generated text
    generated_text = response['choices'][0]['text'].strip()
    return generated_text

