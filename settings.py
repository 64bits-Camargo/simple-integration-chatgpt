from pydantic import BaseSettings


class Settings(BaseSettings):
    OPENAI_KEY: str
    SELECT_STT: str
    CHATGPT_SPEAK: bool
    ADJUST_FOR_AMBIENT_NOISE: bool
    LANGUAGE_SPEAK: str
    ASSISTANT_NAME: str = 'ChatGPT' 
    INPUT_TEXT: bool


settings = Settings(
    _env_file='.env', 
    _env_file_encoding='utf-8'
)


if __name__ == '__main__':
    import ipdb ; ipdb.set_trace()