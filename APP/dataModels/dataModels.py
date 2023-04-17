from pydantic import BaseModel
import speech_recognition


class SpeakerText(BaseModel):
    said: bool
    audio: type(speech_recognition.AudioData)
    text: str


class GptResponse(BaseModel):
    error: bool
    errorName: str
    response: str
    tokens: int
