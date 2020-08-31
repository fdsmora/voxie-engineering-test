# Voxie - Engineer Test
## Fausto's implementation
### Notes
- This project was implemented with Python and Flask. It uses `sqlite` as DB (`MySQL` integration is WIP, see the `mysql` branch for current progress)
- Other technologies used are `HTML`, `JavaScript`, `CSS`, `jQuery`. I also made use of the template method and adapter design patterns. 
- Pending features:
  1. MySQL integration (WIP)
  2. Bundle into a Docker image for easier deployment and testing. (Currently it only runs with `make import-linux`)
### How to run
#### Requirements
. Python  3
. Flask v. 1.1.2  

### Steps 
1. (In case you don't have it) Install Flask:
`
pip install Flask
` 
2. `git clone https://github.com/fdsmora/voxie-engineering-test`
3. Start the app:
`
source voxie-engineering-test/run_this_app.sh
` 
4. In another terminal run:
`
make import-linux
`
5. Open a browser tab and go to http://localhost:8000. Go ahead and test the app. 
6. In case you also want to run the tests I wrote, make sure you have `pytest` installed. If not:
6.1. `pip install pytest coverage`
6.2. `cd voxie-engineering-test` and run `pytest`

## Original README
This project provides a starting point for the Voxie engineering test. This repository's goal is to standardize a
project space for applicants to complete a full-stack project as part of the interview process. We're looking for
projects in PHP, Python, or Go, but let us know if you'd like to make a case for another language or particular
framework.

<details>
  <summary><strong>Table of Contents</strong> (click to expand)</summary>

- [Prompt](#prompt)
- [Usage](#usage)
- [Database](#database)
- [Review](#review)

</details>

## Prompt

We need to process an incoming JSON request containing team, contact, and each contact's custom attribute data. These
requests will always contain a team name, but all other data is optional. Below is an example of a possible incoming
JSON request.
```jsonc
{
  "name": "Michigan kangaroos",
  "contacts": [
    {
      "name": "Mrs. Lewis Kuvalis",
      "phone": "+15551498011",
      "custom_attributes": [
        {
          "key": "7LPkDHh6",
          "value": "Wh1st3Bc"
        }
      ]
    },
    {
      "name": "Nova Bradtke",
      "phone": "+15559382668",
      "email": "constantin.pacocha@example.net"
    }
  ]
}
```
This is another valid request containing the minimal amount of data possible in a request.
```jsonc
{
  "name": "Nevada owls"
}
```

Using this information, build an application that processes these incoming requests at
[http://localhost:8000/import](http://localhost:8000/import) and displays the processed data in a simple way where a
user can view, update, and delete teams and contacts. Please also provide a page or form where a user can search for
contacts by phone number. Feel free to use any existing packages or libraries that you would use in your normal
development process.

## Usage

There is a Makefile provided for your convenience — just run `make [command]` to get started.
```
db                            Start local development mysql database on :3306
import-linux                  Send an import JSON request to :8000/import on a linux-platform
import                        Send an import JSON request to :8000/import
```

Feel free to place all of your project work into the `project` directory within this repository.

## Database

Once you start the local development database using `make db`, there will be an existing `contacts` database with three
tables: `teams`, `contacts` and `custom_attributes`. You can see the credentials in the `docker-compose.yml` file.
During this `db` container creation process, it will use the `dump.sql` file to create the expected tables and
structure. Feel free to inspect the database after running `make db` to further inspect those tables.

## Review

We've set this project up in a way that allows for a simple review process from start to finish.
1. Clone this repository to your local machine
2. Create a new private repository for yourself called `voxie-engineering-test`
3. Follow the instructions to push an existing repository to push this project to your new private repository
4. Add [@jlaswell](https://github.com/jlaswell) as a collaborator to your new private repository
