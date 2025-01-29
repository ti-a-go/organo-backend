# Set up frontend

This project is intended to be the backend for the Organo frontend app.

After set up this project with the help of the instructions on this repository you are ready to run the [frontend application](https://github.com/ti-a-go/organo-frontend).

# Start Docker services (`organo_db` & `organo_api`)

The [docker-compose.yaml file](./docker-compose.yaml) is ready to start two services:
- `organo_db`: a Postgres database
- `organo_api`: a FastAPI application

To start those services run in your terminal:

```sh
docker compose up -d
```

You should see the output:

```sh
[+] Running 3/3
 ✔ Network organo-backend_default  Created                                              0.1s 
 ✔ Container organo_db             Started                                              0.2s 
 ✔ Container organo_api            Started                                              0.4s 
```


# Run migrations

With the Docker services (`organo_db` & `organo_api`) up and running, it's time to run the migrations that will create the `teams` and `employees` tables in the database.

To run the migrations enter this command in your terminal:

```bash
docker exec -it organo_api alembic upgrade head
```

The output should be something as the following:

```sh
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 179181158b31, create teams, employees tables
```

To double check the migration success, you can open an interative terminal inside the database container with the command:

```sh
docker exec -it organo_db bash
```

After that, log into the Postgres command line (`psql`):

```sh
psql -U dev -d organo
```

And you should see something as follow:

```sh
psql (17.0 (Debian 17.0-1.pgdg120+1))
Type "help" for help.

organo=#
```

List the tables with:

```sh
organo=# \dt
```

And the output:

```sh
List of relations
 Schema |      Name       | Type  | Owner 
--------+-----------------+-------+-------
 public | alembic_version | table | dev
 public | employees       | table | dev
 public | teams           | table | dev
(3 rows)
```

Congrats!
Migrations run successfully.


# Seed

Now it's time to seed the database with the following data:

```json
[
    {
        "name": "Front-End",
        "primary_color": "#82CFFA",
        "secondary_color": "#E8F8FF"
    },
    {
        "name": "Data Science",
        "primary_color": "#A6D157",
        "secondary_color": "#F0F8E2"
    },
    {
        "name": "Devops",
        "primary_color": "#E06B69",
        "secondary_color": "#FDE7E8"
    },
    {
        "name": "UX e Design",
        "primary_color": "#D86EBF",
        "secondary_color": "#FAE5F5"
    },
    {
        "name": "Mobile",
        "primary_color": "#FEBA05",
        "secondary_color": "#FFF5D9"
    },
    {
        "name": "Inovação e Gestão",
        "primary_color": "#FF8A29",
        "secondary_color": "#FFEEDF"
    }
]
```

To run the seed will use the POST /teams endpoint of the FastAPI application running in the `organo_api` Docker service.

Will run the python script [./seed/run.py](./seed/run.py) that is just a main function calling the api using the [`requests`](https://pypi.org/project/requests/) library.

The command to seed the database is:

```sh
docker exec -it organo_api python seed/run.py
```

And the outpu:

```sh
Front-End: 201 - Created
Data Science: 201 - Created
Devops: 201 - Created
UX e Design: 201 - Created
Mobile: 201 - Created
Inovação e Gestão: 201 - Created
```

And now we are done!

Our Organo backend is ready to receive the frontend requests.
