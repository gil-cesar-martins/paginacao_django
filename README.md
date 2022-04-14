# paginacao_django
Como dividir os registros de uma tabela em páginas

### Deploy local 
Instale as seguinte bibliotecas com o comando pip:

`pip install django==4.0.2 django-bootstrap-v5 django-adminlte3`

Instale as dependências no **requirements.txt**:
 
`pip freeze > requirements.txt`

No terminal de seu ambiente de desenvolvimento, crie o projeto com: 

`django-admin startproject <nome_do_seu_projeto .`

Crie o diretório da aplicação com:
`django-admin startapp core`
 
Qualquer alteração nos **models** deve ser concluída com o comando:
 
`python manage.py makemigrations`
 
E depois migrar os **models** para o banco de dados:
 
`python manage.py migrate`
 
Crie um superusuário para o gerenciamento do banco de dados:
 
`python manage.py createsuperuser`
 
Execute sua aplicação:
 
`python manage.py runserver`
 
Para acessar vá no seu navegador e  digite [http://localhost:8000](http://localhost:8000)
