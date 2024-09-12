#Desafio: “Meu assistente pessoal” - TDE 3.2

#Imports
import speech_recognition as sr
import wikipedia
from awscli.compat import raw_input
import logging
import pyttsx3

wikipedia.set_lang("pt")
logging.basicConfig(filename='assistentevirtual.log', level=logging.INFO)
engine = pyttsx3.init()

#Assistente virual
print("Seja bem-vindo(a) ao assistente virtual!")
print("(1) - interação por audio/voz\n"
      "(2) - interação por texto")
tipo_interacao = int(input("Digite a opção desejada: "))
if tipo_interacao != 1 and tipo_interacao != 2:
    print("Entre com uma opção válida")
    tipo_interacao = int(input("Digite a opção desejada: "))


#Interação por voz
while tipo_interacao == 1:
    reconhecimento = sr.Recognizer()  # reconher audio
    try:
        with sr.Microphone() as mic:  # habilita o microfone
            reconhecimento.adjust_for_ambient_noise(mic)  # reduz ruido
            print("No que posso te ajudar? ")
            engine.say("No que posso te ajudar?")
            engine.runAndWait()
            engine.stop()
            audio = reconhecimento.listen(mic)  # armazena informacao
            text = reconhecimento.recognize_google(audio, language="pt-BR")
            print("Você disse: {}".format(text))
            engine.say("Você disse: {}".format(text))
            engine.runAndWait()
            engine.stop()
            pesquisa = wikipedia.summary(text, sentences = 2)
            print(pesquisa)
            engine.say(pesquisa)
            engine.runAndWait()
            engine.stop()
            logging.info('Usuário: ' + text)
            logging.info('Assistente virtual: ' + pesquisa)
            print("Diga (sim) ou (não)")
            print("Gostaria de continuar?")
            engine.say("Gostaria de continuar?")
            engine.runAndWait()
            engine.stop()
            reconhecimento = sr.Recognizer()  # reconher audio
            reconhecimento.adjust_for_ambient_noise(mic)
            audio = reconhecimento.listen(mic)  # armazena informacao
            continuar = reconhecimento.recognize_google(audio, language="pt-BR")
            if continuar == "sim":
                print("Você disse: {}".format(continuar))
                engine.say("Você disse: {}".format(continuar))
                engine.runAndWait()
                engine.stop()
                continue
            elif continuar == "não":
                print("Você disse: {}".format(continuar))
                engine.say("Você disse: {}".format(continuar))
                engine.runAndWait()
                engine.stop()
                print("Obrigada por utilizar o assistente virtual")
                engine.say("Obrigada por utilizar o assistente virtual")
                engine.runAndWait()
                engine.stop()
                break
    except:
        print("Não consigui entender, tente novamente")
        engine.say("Não consiguir entender, tente novamente")
        engine.runAndWait()
        engine.stop()
        print("Obrigada por utilizar o assistente virtual")
        engine.say("Obrigada por utilizar o assistente virtual")
        engine.runAndWait()
        engine.stop()
        break

#Interação por texto
while tipo_interacao == 2:
    pergunta = raw_input('Digite sua busca (para finalizar digite "encerrar"): ')
    try:
        if pergunta == "encerrar":
            print("Muito obrigada por utilizar a Assistente virtual")
            break
        else:
            pesquisa = wikipedia.summary(pergunta, sentences = 2)
            print(pesquisa)
            logging.info('Usuário: ' + pergunta)
            logging.info('Assistente virtual: ' + pesquisa)
    except:
        print("Não foi possível encontrar uma resposta")
        print("Obrigada por utilizar o assistente virtual")
        break


# Fontes de pesquisa:
"""
(1) https://www.youtube.com/watch?v=fMyzSrDoT-E&t=12s
(2) https://letscode.com.br/blog/speech-recognition-com-python
(3) https://medium.com/@erikatiliorey/criando-um-chatbot-com-python-36f24b62df6c
(4) https://acervolima.com/modulo-wikipedia-em-python/
(5) https://www.youtube.com/watch?v=gbIjRm--JLs
(6) https://pt.stackoverflow.com/questions/313962/como-buscar-o-resumo-em-portugu%C3%AAs-pela-api-da-wikipedia
(7) https://www.delftstack.com/pt/howto/python/python-log-to-file/
(8) https://docs.python.org/pt-br/dev/howto/logging.html
(9) https://sites.google.com/view/pythoncomarduino/projeto-assistente-virtual/como-fazer-o-python-falar
(10)https://www.codingame.com/playgrounds/52723/programacao-python-parte-3---prof--marco-vaz/tratamento-de-excecao#:~:text=Em%20Python%2C%20assim%20como%20em,os%20comandos%20try%20e%20except.
(11)https://www.youtube.com/watch?v=fMyzSrDoT-E
(12)https://www.treinaweb.com.br/blog/criando-um-chatbot-com-python
(13)https://dev.to/wendrewdevelop/gerando-logs-com-python-25k4
(14)https://medium.com/data-hackers/nunca-mais-prints-digam-hello-ao-logging-em-python-49c87274aed1
(15)https://www.alura.com.br/artigos/a-diferenca-das-funcoes-input-e-raw-input-no-python
"""