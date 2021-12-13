from flask import Flask, jsonify, request

# Função para detectar vogais na mensagem do cliente
def isVowel(letter):
    return letter.lower() in 'aeiou'

# Função que faz com que a mensagem do cliente seja retornada na linguagem do P
def flangCompiler(msg):
    convertedMessage = ""

    for letterPos in range(len(msg)):
        if isVowel(msg[letterPos]):
            convertedMessage = convertedMessage + msg[letterPos] + f"f{msg[letterPos]}"
        else:
            convertedMessage = convertedMessage + msg[letterPos]

    return convertedMessage

app = Flask(__name__)

@app.route('/f', methods=['POST'])
def convert():
    req_data = request.get_json()

    convertedWord = flangCompiler(req_data['word'])

    return jsonify({
        'word': convertedWord
    })