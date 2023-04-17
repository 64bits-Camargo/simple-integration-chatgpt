import openai

from deliver_text import DeliverText
from deliver_voice import DeliverVoice
from receive_text import ReceiveText
from receive_voice import ReceiveVoice
from settings import settings


openai.api_key = settings.OPENAI_KEY
def generate_answer(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        temperature=0.5
    )
    return [response.choices[0].message.content, response.usage]


class Commander:
    
    def __init__(self) -> None:
        self.commands = {}  

    def add_command(self, command: str, synonyms: list[str]):
        if command not in self.commands:
            self.commands[command] = synonyms
        else:
            self.commands[command].extend(synonyms)
    
    def start(self):
        while True:
            try:
                receive, deliver = self.start_components()
            except Exception as err:
                continue
            
            output_text = receive.output_text()
            
            if output_text.lower() in \
                [command.lower() for command in self.commands['sair']]:
                break
            
            mensagens = []
            mensagens.append({"role": "user", "content": str(output_text)})
            answer = generate_answer(mensagens)
            
            print(answer[0])
            
            deliver.output(
                text=answer[0]
            )

    def start_components(self, *args, **kwargs):
        if settings.INPUT_TEXT: 
            receive = ReceiveText()    
            receive.input_text('Pergunte: ')            
        else:
            receive = ReceiveVoice()    
            receive.init_mic()
            receive.to_listen()
            
        if settings.CHATGPT_SPEAK:
            deliver = DeliverVoice()
            deliver.init_settings()
        else:
            deliver = DeliverText()
        
        return receive, deliver

if __name__ == '__main__':
    commander = Commander()
    
    commander.add_command('sair', [
        f'sair {settings.ASSISTANT_NAME}', 
        f'tchau {settings.ASSISTANT_NAME}', 
        f'até mais {settings.ASSISTANT_NAME}', 
        f'até logo {settings.ASSISTANT_NAME}', 
        f'adeus {settings.ASSISTANT_NAME}',
        f'{settings.ASSISTANT_NAME} sair',
        f'{settings.ASSISTANT_NAME} tchau',
        f'{settings.ASSISTANT_NAME} até mais',
        f'{settings.ASSISTANT_NAME} até logo',
        f'{settings.ASSISTANT_NAME} adeus',
    ])
    
    commander.start()