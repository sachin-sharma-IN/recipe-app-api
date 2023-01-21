# recipe-app-api
Recipe API Project.


### Issues/Fix:
- To install psycopg2 from requirements.txt in local macos, we need to run
 ```shell
  pip install -r requirements.txt --global-option=build_ext --global-option="-I/usr/local/opt/openssl/include" --global-option="-L/usr/local/opt/openssl/lib"
  ```
link: https://stackoverflow.com/a/43309554