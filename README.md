# chatbot2.0
That version of chatbot uses OpenAI to generate a response to user.
The transcryption of user's prompt is recorded wiht microphone and then sent through API to generate a response, which is then played to speakers.
In addition the program recognizes the emotion that is mostly present in speaker's voice via neutral network.
To give the best result emotions are being recognized while the whole conversation and then to get the strongest emotion the median of all predicions is calculated.

To use the OpenAI you have to fill the personal key in the config file.
All requirements ale in requirements.txt

TO DO:
- Use predicted emotions to generate the best answer.
- Adjust the emotions detection
