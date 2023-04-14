from utils.yaml_manager import YamlData
from APP.chatbot.gptBot import GptBot
from APP.chatbot.voice_recognisor import VoiceRecogniser


def initialize():

    yaml_data = YamlData()

    gpt_model = GptBot(yaml_data.get_gpt_engine(),
                       yaml_data.get_gpt_max_tokens(),
                       yaml_data.get_temperature(),
                       yaml_data.get_gpt_key())

    voice = VoiceRecogniser(yaml_data.get_voice(),
                            yaml_data.get_voice_rate())

    return gpt_model, voice
