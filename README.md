# Challenge Django Consultant

## Teste Técnico para Consultor Django DigitalSys
As instruções do teste estão presentes em https://github.com/DigitalsysTecnologia/challenge-django-consultant

### Instalação
Instale o [docker](https://docs.docker.com/engine/install/)
 e [docker-compose](https://docs.docker.com/compose/install/linux/).


Crie os arquivos de ambiente `.env` e `db.env` na pasta [back_api](back_api/)
usando como exemplo [dotenv.example](back_api/dotenv.example)
e [dbdotenv.example](back_api/dbdotenv.example).

Crie o arquivo de ambiente `.env.local` na pasta [front_app/loan](front_app/loan/)
usando como exemplo [dotenvlocal.example](front_app/loan/dotenvlocal.example).
Use o seu ip local de rede ou um ip onde a api esteja acessível.

Execute:

```sudo docker compose up --build```

depois, para migrar e adicionar o usuário inicial execute:

`sudo docker compose exec back_api bash ./initdb.sh`

Isto irá criar um superusuário com nome "user1" e senha "nosecurepassword".

Acesse o painel admin em http://localhost:8080/admin/
e o cadastro de empréstimo em http://localhost:8081
