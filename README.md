# REFERRAL SERVICE API  
## Описание проекта  
Referral Service API позволяет:  
* регистрировать пользователя и аутентифицировать с помощью JWT;
* аутентифицированному пользователю создать и удалить свой реферальный код;
* получить реферальный код по email адресу реферра;
* регистрировать по реферальному коду в качестве реферала;
* получить информацию о рефералах по id реферера;  

Документация автоматически сгенерирована с помощью Swagger и ReDoc и доступна по следующим url:  
* http://127.0.0.1:8000/api/schema/swagger-ui/
* http://127.0.0.1:8000/api/schema/redoc/
## Установка и настройка проекта

1. Клонируйте репозиторий с проектом в вашу рабочую директорию:  
```commandline
$ git clone git@github.com:TarakanovAndrey/referral_service.git
```
2. Зайдите в директорию проекта и установить все зависимости командой:  
```commandline
$ make install
```
3. В директории проекта создатей файл .env и создайте следующие записи:  
SECRET_KEY=  
HUNTER_SECRET_KEY=

Секретный ключ (SECRET_KEY) можно сгенерировать в 
терминале Ubuntu командой  
```commandline
openssl rand -base64 32
```
Эта команда сгенерирует случайный секретный ключ длиной 32 символа и закодирует его в формате Base64. 
Вы можете изменить размер ключа, заменив 32 на любое другое значение.  

Для получени ключа HUNTER_SECRET_KEY зарегистрируйтесь на https://hunter.io/ и из дашборда скопируйте секретный ключ.
## Запуск проекта  
В директории проекта с помощью термина введите команды:  
```
$ make migrations
$ make migrate
$ make run
```
## Postman  
Для тестирования проекта можно использовать декстопную версию Postman.
При генерации токена во вкладке Headers необходимо добавить ключ "Authorization"
со значением "Bearer {ваш токен}".

## Регистрация пользователя  
Endpoint: http://127.0.0.1:8000/api/users/create/  
Body:
```commandline
{
    "email": "example@example.com",
    "password": "example_password"
}
```

## Получение access/refresh токенов

http://127.0.0.1:8000/api/token/
```commandline
{
    "email": "<Учетные данные уже зарегистрированного полльзователя>",
    "password": "<Учетные данные уже зарегистрированного полльзователя>"
}
```
В настройках время жизни access токена выставлено 30 минут (чтобы часто не обновлять при разработке). Дефолтный
показатель - 5 минут.


## Создание реферального кода  
Код генерируется автоматически.  
Endpoint: http://127.0.0.1:8000/api/codes/create/  
Method: POST  
Body: 
```commandline
{
    "valid_until": "2024-11-12",
    "is_active": "True",
    "owner_id": 2
}
```
В запросе передаются следующие данные:  
* "valid_until" - дата до которой код активен;  
* "is_active": - принимает True/False. Показывает активируется ли код при его создании. Если код актвируется сразу, 
то все остальные созданные данным пользователем коды деактивируются автоматически;
* "owner_id": - id создателя кода.  
## Обновление даты годности и статуса активности реферального кода  
Endpoint: http://127.0.0.1:8000/api/codes/update/<referral_code>/  
Method: PATCH   
Body:  
```commandline
{
    "is_active": "True",
    "valid_until": "2027-12-12"
}
```
У любого из созданных ранее реферальных кодов можно изменить статус активности. При изменение статуса на True
, у всех остальных кодов он меняется на False. Также можно изменить дату до которой код активен.
## Удаление реферального кода  
Endpoint: http://127.0.0.1:8000/api/codes/update/<referral_code>/  
Method: DELETE  
## Получения реферального кода по email адресу реферера  
Endpoint: "http://127.0.0.1:8000/api/codes/search/?email=<email_adress>"  
Method: GET  
## Регистрация по реферальному коду в качестве реферала  
Endpoint: http://127.0.0.1:8000/api/referrers/attach/  
Method: POST  
Body:  
```commandline
{
    "email": "example@example.com",
    "code_value": "example_code"
}
```
## Получение информации о рефералах по id реферера  
Endpoint: http://127.0.0.1:8000/api/referrers/search/?referrer_id=<referrer_id>  
Method: GET

## Задачи для реализации  
1. Доработать скрипт генерации кода, чтобы в начале кода были ключевые слова реферала. По типу "MYCODE1234123"
2. С помощью Selery/Reddis реализовать проверку срока годности кодов
3. Доработать статсусы у ответов, по которым клиент может ориентироваться о результатах ответа.
4. DRF странный в реализации асинхронщины. FastApi больше бы подошел
5. Обязательно тесты
6. Сбор дополнительных данных о клиенте
7. В рамках DRF оптимизировать асинх