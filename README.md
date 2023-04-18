# simple-integration-chatgpt

#### Settings .env
OPENAI_KEY=""               
SELECT_STT="google"    
ADJUST_FOR_AMBIENT_NOISE=true<br>
LANGUAGE_SPEAK='pt-BR'<br>
CHATGPT_SPEAK=true<br>
INPUT_TEXT=false<br>
ASSISTANT_NAME='Jarvis'


#### Implementation 
```python
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
```
