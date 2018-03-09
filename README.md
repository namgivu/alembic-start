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
  #create new revision/migration file
  alembic revision -m 'create account table'
  
  : #edit the upgrade() and downgrade()
  
  #run it
  alembic upgrade head
  ```
  
  what-happened detail
  > Alembic first checked if table *alembic_version* exists, and if not, created it
    Search the current version in this table, if any, 
    and then calculates *revision-path* from this version to the version requested i.e  *head*  
    For each revision in the path, *call upgrade()* method is called
    
    Q:what is current version, how to know it, what indicate its value?
    A1:the single-cell table stores this value alembic_version
    A2:`alembic current`

  ##create 2nd migration
  ```bash
  alembic revision -m "Add a column"
  : #edit the upgrade() and downgrade()
  alembic upgrade head 
  ```
  
    
#misc

  ##all alembic op commands
  ref. http://alembic.zzzcomputing.com/en/latest/ops.html#ops
  
  ##dump postgres db
  ref. https://www.digitalocean.com/community/tutorials/how-to-backup-postgresql-databases-on-an-ubuntu-vps
  ```bash
  sudo su - postgres
  pg_dump alembic_start > /tmp/dump-db.sql
  exit
  cp /tmp/dump-db.sql "$CODE/db/dump-db.sql"
  ```
  
  ##switching between revision
  ```bash
  alembic upgrade   ae1
  alembic upgrade   +2
  alembic downgrade -1
  alembic upgrade   ae1+2
  
  alembic upgrade   head #up to latest
  alembic downgrade base #down to beginning
  ```
