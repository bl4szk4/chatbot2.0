# chatbot2.0
That version of chatbot uses OpenAI to generate a response to user.
The transcryption of user's prompt is recorded wiht microphone and then sent through API to generate a response, which is then played to speakers.
In order to give the best response to user I want to implement the neutral network used in my previous project with chatterbot.

To use the OpenAI you have to fill the personal key in the config file.
All requirements ale in requirements.txt

TO DO:
- Implement a neutral network from previous project to recognize the emotion in voice.
- Use predicted emotions to generate the best answer.
- Adjust the emotions detection.
