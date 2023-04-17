from interfaces import ReceiveInterface
from logger import logger


class ReceiveText(ReceiveInterface):
    
    def __init__(self) -> None:
        self.text = ''
        
    def input_text(self, description: str = '') -> None:
        self.text = input(description)
        
    def output_text(self):
        logger.info('output_text: {}'.format(self.text))
        return self.text


if __name__ == '__main__':
    receive_text = ReceiveText()
    receive_text.input_text("Qual é seu nome? ")
    receive_text.output_text()