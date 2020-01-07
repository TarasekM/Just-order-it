# Just-api for Just-order-it

## Running

### For bash env

``` bash
export FLASK_APP="/Users/artemii/Desktop/Just-order-it/src/just-api/just_api:create_app('development')"
export FLASK_ENV=development
export DEV_MONGO_URI="mongodb://localhost:27017/mydb"
export FLASK_RUN_PORT=9000
python -m flask run
```

### For Powershell (windows 10 default)

``` powershell
$env:FLASK_APP="C:\Users\rezkt\PycharmProjects\Just-order-it\src\just-api\just_api:create_app('development')"
$env:FLASK_ENV="development"
$env:DEV_MONGO_URI="mongodb://localhost:27017/mydb"
$env:FLASK_RUN_PORT=9000
python -m flask run
```
