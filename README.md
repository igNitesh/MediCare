# MediCare - Your Health is Our Priority

MediCare is a website that provides users with information about hospitals, doctors, and medicines. The website is designed to help people find the nearest hospital with emergency services and search for doctors by location and specialization. It also allows users to search for information about medicines.

## Problem statement

During emergency situations, finding the nearest hospital with the required emergency services can be a daunting task. Similarly, finding a doctor with the required specialization and location can be time-consuming. Additionally, getting information about medicines can be difficult, especially for people who are not familiar with medical terms. The MediCare website aims to solve these problems by providing users with relevant information in one place.

## User Interface

![Home](https://imgur.com/GVh0Q5k.png)

## Table of Contents

- [Introduction](#introduction)
- [Technology Used](#technology-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Contact](#contact)

## Technology Used

MediCare is built using the following technologies:

- HTML, CSS, JavaScript, Bootstrap for the frontend
- Django, Python, SQLite for the backend
- Selenium and Request for scraping medicine information and storing in the database

## Features

The MediCare website offers the following features:

1. Services section: Users can search for hospitals and their emergency services, such as Ambulance, Ventilator, Oxygen Cylinder, and Beds. They can use the filter option to find the nearest hospital and get information about their real-time services availability.

![Services](https://imgur.com/Ju5Ng4l.png)

2. Doctor section: Users can search for doctors based on their city and specialization.

![Docters](https://imgur.com/R0mZE9i.png)

3. Search bar: Users can search for any medicine's information through the search bar with their name and get information about its manufacturer, composition, uses, side effects, how to use, safety advice, substitute, and other relevant details.

![Medicine](https://imgur.com/aisFVaZ.png)

4. Hospital user type: Hospitals can log in to the website to update or add emergency services and doctors.
5. Administrator user type: Administrators can log in to the website to manage hospitals, doctors, and users.

## Installation

To run the MediCare website on your local machine, follow these steps:

1. Clone the repository from GitHub using the command `git clone <repository URL>`.
2. Install Python and Django on your system.
3. Install the required packages using the command `pip install -r requirements.txt`.
4. Run the Django server using the command `python manage.py runserver`.
5. Open your web browser and navigate to `http://localhost:8000/`.

## Usage

To use the MediCare website, follow these steps:

1. On the home page, select the desired section (Services, Doctors, or Search Bar).
2. In the Services section, use the filter options to search for hospitals by location.
3. In the Doctors section, use the filter options to search for doctors by location and specialization.
4. Use the search bar to search for information about medicines.
5. If you are a hospital, log in to the website by navigating to `http://localhost:8000/admin/` to update or add emergency services and doctors.
6. If you are an administrator, log in to the website by navigating to `http://localhost:8000/admin/` to manage hospitals, doctors, and users.

## Contributing

We welcome contributions to the MediCare website. To contribute, follow these steps:

1. Fork the repository on GitHub.
2. Make your changes in a new branch.
3. Create a pull request with a description of your changes.
4. Wait for the pull request to be reviewed and merged.

## Credits

The MediCare website was developed by [Nitesh Rauniyar](https://github.com/igNitesh), [Kishlay Jeet](https://github.com/kishlayjeet). We would like to thank [Kishlay Jeet](#) for their contributions to the project.

## License

The MediCare website is licensed under the MIT license.

## Contact

If you have any questions or feedback about the MediCare website, please contact us at niteshrauniyar0@gmail.com or contact.kishlayjeet@gmail.com. We would love to hear from you!
