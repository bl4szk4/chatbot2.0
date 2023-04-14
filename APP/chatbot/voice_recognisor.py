import speech_recognition
import speech_recognition as sr
from APP.dataModels.dataModels import SpeakerText
import pyttsx3


class VoiceRecogniser:

    def __init__(self, voice, rate):
        # data for google recognizer - speech to text
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone(device_index=1)
        # data for speaking out text - text to voice
        self.engine = pyttsx3.init()
        self.voice = self.engine.setProperty('voice', str(voice))
        self.rate = self.engine.setProperty('rate', str(rate))

    def noise_adjustment(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=3)

    def voice_capture(self):
        try:
            with self.microphone as source:
                response = self.recognizer.listen(source, timeout=10, phrase_time_limit=5)

                try:
                    SpeakerText.text = self.recognizer.recognize_google(response, language='pl-PL')

                    SpeakerText.said = True
                    SpeakerText.audio = response

                except speech_recognition.UnknownValueError:
                    SpeakerText.said = False

        except speech_recognition.WaitTimeoutError:
            SpeakerText.said = False

        except speech_recognition.UnknownValueError:
            SpeakerText.said = False

        return SpeakerText

    def say_text(self, text_to_say:str):
        self.engine.say(text_to_say)
        self.engine.runAndWait()

