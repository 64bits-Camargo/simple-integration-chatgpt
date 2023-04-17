from interfaces import DeliverInterface
from logger import logger
import pyttsx3

from receive_voice import ReceiveVoice


class DeliverVoice(DeliverInterface):
    
    def __init__(self) -> None:
        self.initialized = False
        self.engine = None
        
    def init_settings(self) -> None:
        try:            
            self.engine = pyttsx3.init()
            voices = self.engine.getProperty('voices')
            self.engine.setProperty('rate', 105)
            self.engine.setProperty('voice', voices[96].id)
            logger.info('initialized deliver voice... start!')
        except Exception as err:
            logger.error('initialized deliver voice... failed!')
            raise Exception(
                "Error initiation deliver voice: {}".format(err.message)
            )
            
    def output(self, text) -> None:
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()


if __name__ == '__main__':
    
    deliver_voice = DeliverVoice()
    deliver_voice.init_settings()
    deliver_voice.output(
    '''
        O que for teu desejo, assim será tua vontade.
        O que for tua vontade, assim serão teus atos.
        O que forem teus atos, assim será teu destino.!
    '''
    )
    
    