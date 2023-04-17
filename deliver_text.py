from interfaces import DeliverInterface
from logger import logger


class DeliverText(DeliverInterface):
    
    def output(self, text) -> None:
        logger.info('output_text execute')
        print(text)