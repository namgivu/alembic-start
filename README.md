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
  alembic revision -m 'Add a column'
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
  
  alembic downgrade base #back to the beginning
  alembic upgrade   head #up to the latest
  
  alembic revision -m 'migration name' #create new revision
  
  alembic current #view current revision
  alembic history           #view history
  alembic history --verbose #view history
  alembic history -r-3:     #view last 3 revision to current; more range syntax ref. http://alembic.zzzcomputing.com/en/latest/tutorial.html#viewing-history-ranges
  ```

  ##running plain/raw sql in migration up-down
  ref. https://www.johbo.com/2016/data-migrations-with-alembic-plain-sql.html
  sample code
  ```
  def upgrade():
    sql_up = '''
        YOUR SELECT QUERY
    '''
    c=op.get_bind(); c.execute(sql_up)
  ```
  comment
  > Quite often a good old plain SQL statement seems to be good enough to get the job done
  > Drawback: 
    Limited to support multiple database systems due to different sql dialects are used --> cannot write a single plain sql for that. 
    It is then better to use a higher abstraction level

  ##merge revisions when merging git branches
  ```
  alembic heads #list all heads
  alembic merge -m 'message for this merage' r01 r02 ... #listing the revision to merge as r01 r02; values taken from `alembic heads` command
  ```

  ##use variable to define value
  var02=%(var01)s/some-string

  ##multiple script locations
  ref. http://alembic.zzzcomputing.com/en/latest/branches.html#setting-up-multiple-version-directories
  defined by the entry/variable **version_locations** in `alembic.ini`
  eg.
  ```
  #eg01
  version_locations = %(here)s/bar %(here)s/bat %(here)s/alembic/versions
  
  #eg02
  rh = %(here)s/%(script_location)s/versions
  version_locations = %(rh)s %(rh)s/1803
  ```
  
  NOTE: 
  - creating new revision by `alembic revision -m 'some message'` will reuse folder of previous revision
    to choose new folder, use **--version-path** 
    ie. `alembic revision -m 'some message' --version-path 'folder path listed in version_locations'` 
  - to **move current revision files** to a folder `YYmm`, 
    do moving them normally and add the new folder to `version_locations` in alembic.ini
  
  NOTE: When using **version_locations**, value defined by **script_location** will be ignored ref. https://bitbucket.org/zzzeek/alembic/issues/124#comment-44658866


