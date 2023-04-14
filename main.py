from utils.initialization import initialize

gpt, voice_recogniser = initialize()

while True:
    print("You: ")
    user_input = voice_recogniser.voice_capture()
    if user_input.said:
        text_input = user_input.text

        print(user_input.text)
        gpt_response = gpt.generate_response(text_input)

        if not gpt_response.error:
            voice_recogniser.say_text(gpt_response.response)
            print("GPT: {}", gpt_response.response)

        else:
            print("No connection with bot")

    else:
        print("Nothing was said")

    if 'koniec rozmowy' in text_input:
        break
