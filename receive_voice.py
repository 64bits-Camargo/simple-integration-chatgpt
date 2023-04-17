from interfaces import ReceiveInterface
from logger import logger
from settings import settings
import speech_recognition


class ReceiveVoice(ReceiveInterface):
    
    def __init__(self) -> None:
        self.initialized = False
        self.adjust_enviroment_noise = settings.ADJUST_FOR_AMBIENT_NOISE
        
    def init_mic(self) -> None:
        try:            
            self.mic = speech_recognition.Microphone()
            self.recognizer = speech_recognition.Recognizer()
            self.initialized = True
            logger.info('initialized mic... start!')
        except Exception as err:
            logger.error('initialized mic... failed!')
            raise Exception("Error initiation mic: {}".format(err.message))
            
    def to_listen(self) -> None:
        self.transcription = ''
        with self.mic as voice:
            if self.adjust_enviroment_noise:
                self.recognizer.adjust_for_ambient_noise(voice)
                self.adjust_enviroment_noise = False

            logger.info('listen...')
            audio = self.recognizer.listen(voice)

            logger.info('send to recognizer...')
            self.transcription = self.source_transcription(audio)

    def source_transcription(self, audio) -> str:
        if settings.SELECT_STT == 'google':
            transcription = self.google_transcription(audio)
        logger.info('transcription: {}'.format(transcription))
        return transcription

    def google_transcription(self, audio) -> str:
        transcription = self.recognizer.recognize_google(
            audio_data=audio, 
            language=settings.LANGUAGE_SPEAK
        )     
        return transcription

    def output_text(self) -> str:
        logger.info('output_text: {}'.format(self.transcription))
        return self.transcription


if __name__ == '__main__':
    receive_voice = ReceiveVoice()
    receive_voice.init_mic()
    receive_voice.to_listen()
    receive_voice.output_text()