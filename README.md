#get started

create venv3
```bash
sudo pip install virtualenv
virtualenv -p python3 venv3
```

install requirements
```bash
source ./venv3/bin/activate
pip install -r requirements.txt
```

#alembic tutorial 
ref. http://alembic.zzzcomputing.com/en/latest/tutorial.html

  ##init
  ```bash
  alembic init alembic
  ```

  alembic.ini
  - file_template = %%(rev)s_%%(slug)s
  > %%(rev)s  - revision id
    %%(slug)s - revision message
    %%(year)d, %%(month).2d, %%(day).2d, %%(hour).2d, %%(minute).2d, %%(second).2d - timestamp fields
  
  - script_location = alembic
  > the location of the Alembic environment

  - timezone = SGT
  - sqlalchemy.url = driver://user:pass@localhost/dbname

  ##create new migration
  ```bash
  alembic revision -m 'create account table'
  ```
