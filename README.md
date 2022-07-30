Para deploy no Heroku

Fazer login

## cria app
heroku create <nome do app>
## cria Banco
heroku addons:create heroku-postgresql:hobby-dev -app <nome do app>
## ve config no heroku
heroku --config -app <nome da app>