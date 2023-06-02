# recipe-app-api
Recipe API Project.


### Issues/Fix:
- To install psycopg2 from requirements.txt in local macos, we need to run
 ```shell
  pip install -r requirements.txt --global-option=build_ext --global-option="-I/usr/local/opt/openssl/include" --global-option="-L/usr/local/opt/openssl/lib"
  ```
link: https://stackoverflow.com/a/43309554

#### User API
- Create a new app `User` in our code to store all code for our user api.
  ```docker
    docker-compose run --rm app sh -c "python manage.py startapp user<name-of-app>"
  ```
  - Add `user` app in `app/app/settings.py` to register and enable it in our project.
