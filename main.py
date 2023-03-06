import os
import openai

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define conversation parameters
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

# Start the conversation loop
while True:
    # Get user input
    user_input = input("You: ")

    # Generate AI response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=start_sequence + user_input + restart_sequence,
        temperature=0.9,
        max_tokens=3000,
        stop=["\n"]
    )

    # Print AI response
    ai_response = response.choices[0].text.strip()
    print("AI:", ai_response)
