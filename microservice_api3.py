from flask import Flask, jsonify, request

# Função para detectar vogais na mensagem do cliente
def isVowel(letter):
    return letter.lower() in 'aeiou'

# Função que faz com que a mensagem do cliente seja retornada na linguagem do P
def llangCompiler(msg):
    convertedMessage = ""

    for letterPos in range(len(msg)):
        if isVowel(msg[letterPos]):
            convertedMessage = convertedMessage + msg[letterPos] + f"l{msg[letterPos]}"
        else:
            convertedMessage = convertedMessage + msg[letterPos]

    return convertedMessage

app = Flask(__name__)

@app.route('/l', methods=['POST'])
def convert():
    req_data = request.get_json()

    convertedWord = llangCompiler(req_data['word'])

    return jsonify({
        'word': convertedWord
    })