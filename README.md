# CodeZen
> Platform to help educators organize their materials
> 
> No live demo yet. <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Project Status](#project-status)
* [Docker Command References](#docker-commands)
<!-- * [License](#license) -->

## General Information
<image src="https://ziadoua.github.io/m3-Markdown-Badges/badges/Flask/flask1.svg" alt="Flask badge" />
<image src="https://ziadoua.github.io/m3-Markdown-Badges/badges/Bootstrap/bootstrap1.svg" alt="Bootstrap badge" />
<!-- What problem does it (intend to) solve?-->
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Important
-  When trying to host your own project use Python Anywhere or Aptible
-  When using a virtual environment make sure to activate and deactive your environment, creating one helps avoid conflicts with the global interpreter/environment

## Technologies Used
- ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
- ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
- ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
- ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)

## Features
List of features here:
- Users can navigate through mulitple web pages
- Users can sign up ( In-Progress)
- Users can create an account ( In-Progress)

## Installation
See the appropriate guide for your environment and operating system.
- Flask or older Flask version
- Other frameworks that are not Flask, Bootstrap or a templating engine that is different from Jinja
>
  a. Flask Installation
>
  Add Flask to your global or virutal enivorment:
  For macOS:
  `pip3 install flask`
  For Windows:
  `pip install flask`
- Make sure that Flask is the current version
- If using the virtual enivorment make sure to navigate to your folder that you create your env folder and activated your env
- You can activate your enivorment by typing `source\bin\activate\` and for Windows `.\env\Scripts\activate`
>
  b. Boostrap Installation
>
  Add the link provided by Boostrap in your header located in your HTML file (this could also be your base file).
  >
  `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">`
  >
  - Make sure to use version 5 as this is the latest version
>
  c. Jinja/HTML/CSS Installation
>
  - There is no installation needed for Jinja, HTML, CSS.
>
  HTML and CSS is built into VSCode, while Jinja is Flask's official templating engine.

## Usage
How does one go about using it?

`User navigates onto the home page and can click any buttons or use the navigation links in the header(top of the page) or footer(bottom of the page).`
>
`User can also view the website on mulitple devices such as desktop or mobile.`

## Project Status
Project is: _in progress_ 

## Docker Commands
1. Build the Image
`docker build -t flask-image .`
2. Run the Container
`docker run -p 5001:5000 --rm --name flask-container flask-image`
3. Access via Browser
`http://localhost:5001`
