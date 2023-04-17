# para instalar todos os modulos
import openai
import speech_recognition as sr
import whisper
import pyttsx3
import os

from settings import settings

openai.api_key = settings.OPENAI_KEY

def generate_answer(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  ##
        # model="gpt-3.5-turbo-0301", ## ateh 1 junho 2023
        messages=messages,
        max_tokens=1000,
        temperature=0.5
    )
    return [response.choices[0].message.content, response.usage]


def talk(texto):
    # falando
    engine.say(texto)
    engine.runAndWait()
    engine.stop()


def save_file(dados):
    with open(path + filename, "wb") as f:
        f.write(dados)
        f.flush()


# reconhecer
r = sr.Recognizer()
mic = sr.Microphone()

model = whisper.load_model("base")

# falar
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)  # velocidade 120 = lento
for indice, vozes in enumerate(voices):  # listar vozes
    print(indice, vozes.name)
voz = 2# "IVONA_2_Ricardo_OEM"
engine.setProperty('voice', voices[voz].id)

mensagens = [{"role": "system", "content": "Você é um assistente gente boa. E meu nome é Bob!"}]

path = os.getcwd()
filename = "audio.wav"

print("Speak to Text", settings.SELECT_STT)

settings.ADJUST_ENVIROMENT_NOISE = True

while True:
    text = ""
    question = ""

    if settings.INPUT_TEXT:
        question = input("Perguntar pro ChatGPT (\"sair\"): ")
    else:
        # Ask a question
        with mic as fonte:
            if settings.ADJUST_ENVIROMENT_NOISE:
                r.adjust_for_ambient_noise(fonte)
                settings.ADJUST_ENVIROMENT_NOISE = False
            print("Fale alguma coisa")
            audio = r.listen(fonte)
            print("Enviando para reconhecimento")

            if settings.SELECT_STT == "google":
                question = r.recognize_google(audio, language="pt-BR")
            elif settings.SELECT_STT == "whisper":
                save_file(audio.get_wav_data())

        if settings.SELECT_STT == "whisper":
            text = model.transcribe(path + filename, language='pt', fp16=False)
            question = text["text"]

    if ("esligar" in question and "assistente" in question) or question.startswith("sair"):
        print(question, "Saindo.")
        if settings.SPEAK:
            talk("Desligando")
        break
    elif question == "":
        print("No sound")
        continue
    elif question.startswith("Assistente") or question.startswith("assistente") or question.startswith(
            "chat GPT") or settings.NO_ACTIVATING_WORD:
        print("Me:", question)
        mensagens.append({"role": "user", "content": str(question)})

        answer = generate_answer(mensagens)

        print("ChatGPT:", answer[0])

        if settings.DEBUG_COST:
            print("Cost:\n", answer[1])

        mensagens.append({"role": "assistant", "content": answer[0]})

        if settings.SPEAK:
            talk(answer[0])
    else:
        print("No message")
        continue

    if settings.DEBUG:
        print("Mensages", mensagens, type(mensagens))
print("See ya!")
