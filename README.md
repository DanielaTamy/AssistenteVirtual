# 🤖 Projeto: Assistente Virtual Pessoal - TDE 3.2

**Abril/2023**  
**1º semestre - Ciência da Computação PUCPR**  
**Trabalho Discente Efetivo (TDE)**

Este projeto consiste em um **assistente virtual pessoal** que interage com o usuário por meio de comandos de voz ou texto. A aplicação utiliza bibliotecas como **speech_recognition**, **wikipedia** e **pyttsx3** para reconhecimento de fala, buscas na Wikipedia e síntese de voz. O assistente pode responder perguntas e realizar buscas rápidas, além de gerar logs das interações.

## 🛠️ Funcionalidades
- **Interação por Voz** 🎤: O assistente reconhece comandos de voz, faz buscas na Wikipedia e responde com áudio.
- **Interação por Texto** 💬: O usuário pode digitar perguntas e receber respostas baseadas em informações da Wikipedia.
- **Logs de Interação** 📝: O sistema armazena logs de todas as interações em um arquivo de log.

## 🚀 Tecnologias Utilizadas
- **Python** 🐍
- **speech_recognition**: Para reconhecimento de fala
- **pyttsx3**: Para síntese de voz
- **wikipedia**: Para realizar pesquisas na Wikipedia
- **logging**: Para criar logs de atividades do assistente

## ⚙️ Como Funciona
1. O assistente pergunta se o usuário deseja interagir via voz ou texto.
2. Se a opção de voz for escolhida:
   - O usuário fala o destino ou pergunta, e o assistente responde em áudio.
   - O sistema gera logs de todas as interações.
3. Se a opção de texto for escolhida:
   - O usuário pode digitar perguntas ou instruções.
   - As respostas são exibidas no console e também logadas.

## 📚 Fontes de Pesquisa
1. [Reconhecimento de Fala com Python](https://www.youtube.com/watch?v=fMyzSrDoT-E&t=12s)
2. [Speech Recognition com Python](https://letscode.com.br/blog/speech-recognition-com-python)
3. [Criando um ChatBot com Python](https://medium.com/@erikatiliorey/criando-um-chatbot-com-python-36f24b62df6c)
4. [Wikipedia em Python](https://acervolima.com/modulo-wikipedia-em-python/)
5. [Como Gerar Logs com Python](https://www.delftstack.com/pt/howto/python/python-log-to-file/)
6. [Guia de Logging no Python](https://docs.python.org/pt-br/dev/howto/logging.html)

## 📦 Requisitos
Para executar este projeto, você precisará das seguintes bibliotecas instaladas:
- `speech_recognition`
- `wikipedia`
- `pyttsx3`
- `logging`
  
Instale as dependências com o seguinte comando:

```bash
pip install speechrecognition wikipedia pyttsx3
