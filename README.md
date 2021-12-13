# Reuso de Software - Arquitetura de Microsserviços - Conversor linguagens de P, F e L.

## Alunos:
### Edson Ivo - 428689
### Ribamar Filho - 472687

> Para rodar, é necessário ter um gerenciador de pacotes do Node instalado e então digitar no terminal: `npm i`

> O servidor então deve ser iniciado com `npm start`

> Para os arquivos python, é necessário ter o python instalado, juntamente ao Flask, que pode ser instalado com `pip install Flask`

> Para cada arquivo, é necessário abrir um terminal para o seu respectivo serviço, que podem ser executados com:

```
FLASK_APP=microservice_api1 flask run --port=3001
FLASK_APP=microservice_api2 flask run --port=3002
FLASK_APP=microservice_api3 flask run --port=3003
```

> As requisições devem ser feitas para a porta do servidor NodeJS (`http://localhost:3000`), contendo os campos type e word, com type contendo a letra que pode ser p, f ou l, e word a palavra que deve se converter. Os métodos devem ser POST.