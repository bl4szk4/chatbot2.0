import yaml
import logging

logger = logging.getLogger(__name__)


class YamlData:

    def __init__(self, filename='config.yaml'):
        try:
            with open(filename) as f:
                self.data = yaml.load(f, Loader=yaml.FullLoader)
                f.close()
        except EnvironmentError:
            exit(1)

    def get_gpt_key(self):
        return self.data['gpt_params']['gpt_token']

    def get_temperature(self):
        return self.data['gpt_params']['temperature']

    def get_voice(self) -> str:
        return self.data['voice_params']['voice']

    def get_voice_rate(self) -> str:
        return self.data['voice_params']['rate']

    def get_gpt_max_tokens(self) -> int:
        return self.data['gpt_params']['max_tokens']

    def get_gpt_engine(self) -> str:
        return self.data['gpt_params']['engine']
