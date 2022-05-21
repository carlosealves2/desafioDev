# Desafio Fluxo de pedidos

projeto simples de fluxo de pedido

# inicialização

O projeto esta dockerizado, não sendo preciso nada além do docker e do docker compose instalado na maquina para poder rodar.

# como iniciar

Para inciar, execute o comando no terminal estando na pasta raiz do projeto:

	docker-compose up -d --build 

Este comando inicia o docker compose e gera o build do projeto.

# Acessando a aplicação
O sistema de rotas e arquivos estáticos esta sendo gerenciador pelo motor web NGINX, a aplicação principal pode ser acessada pela rota:

	http://localhost:5000/

## outros serviços

Além da aplicação principal o projeto conta com o serviço do PGADMIN4, um gerenciador de banco de dados PostgreSQL.
para acessá-lo abra seu navegador e acesse:

	http://localhost:5000/dbadmin



Arquivos estaticos podem ser acessados pela rota:

	http://localhost:5000/static


A aplicação principal usa o gunicorn como web server para WSGI.

# testes
Para executar os testes, é necessário acessar o container da aplicação utilizando o seguinte comando na raiz do projeto:

	docker-compose exec app bash

Apos acessar, navege até a pasta core utilizando o comando:

	cd core/

E em seguida use o proximo comando para executar os testes:

	./manage.py test

# Parando o serviço
Para parar o serviço incluindo todos os containeres basta fazer o seguin:

### 1ª certifique-se de estar na raiz do projeto

### 2ª execute:
	docker-compose down -v;

Assim ira parar os serviços e remover os volumes.

# Aviso
Atualmente sempre que o serviço for finalizado, na próxima vez que for iniciado os dados estarão perdidos. Para resolver isso acesso o arquivo entrypoint.sh na pasta "core" e comente a linha:

	# python manage.py flush --no-input
