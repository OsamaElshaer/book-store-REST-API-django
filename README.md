# book-store-REST-API-django

This is a book-store REST API that provides the main functions you'd expect from a book-store like user managment, crud operations etc.

## Project Status

This project is been compeleted .

## About The Project

build by **Django** as backend framework cause Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel and SQLite as database.
**python** as a back end it's great choise cause it contains several distinct libraries in task automation, data analysis, and data visualization and webScraping .

<!-- GETTING STARTED -->

## Getting Started

These instructions will give you a copy of the project up and running on your local machine for development.

### Prerequisites

#### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`
`DEBUG`

### Installation

1. Clone the repo
    ```sh
     git clone https://github.com/OsamaElshaer/book-store-REST-API-django.git
    ```
2. vertual enviroment
    ```sh
     python -m venv env
     env\scripts\activate
    ```
3. install requirements
    ```sh
     pip install -r requirements.txt
    ```
4. migrate --> create user admin
    ```sh
     python manage.py migrate
     python manage.py createsuperuser
    ```
5. run server
    ```sh
     python manage.py sunserver
    ```

### API Docs

    http://127.0.0.1:8000

<!-- LICENSE -->

## License

Distributed under the MIT License.
