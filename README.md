pgbackup
========

CLI for backing up remote PostgreSQL databases locally or through S3

## Usage

pass in a full databse URL, the storage driver, and destination.

S3 example with bucket name:
```
$ pgbackup prostgres://bob@example.com:5432/db_one --driver s3 backups
```
local example with local path:

```
$ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups
```

## installation from source

to install the package after you have cloned the repository, you will want to run the following command from within the project directory:

```
$ pip install --user -e .
```

## preparing for development

follow thse steps to start developing with this project

1. ensure `pip` and `pipenv` are installed
2. clone repository: `git clone git@github.com:example/pgbackup`
3. `cd` into repository
4. activate virtualenv: `pipenv shell`
5. install dependencies: `pipenv install`

