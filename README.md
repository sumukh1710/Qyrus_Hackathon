<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="static/img/logo.png" alt="Logo" width="80" height="80">
  </a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<b>Project Description</b>

Qyrus device farm has grown from having just 10 devices to more than 100 devices in a year, from 1 location to 3 locations. 
A typical device farm is a hardware intensive operation, which involves procurement, setup and maintenance of hardware devices like Phones, Network equipment, USB Hubs, Cables, servers etc.
Qyrus has 2 offerings when it comes to device farm - Dedicated and Shared. 
Dedicated devices are allocated to a client and cannot be used by anyone else. This brings an added layer of management which is allocation and de-allocation of devices to a client.
Considering the above, there is a clear need for us to systemise the entire process of device farm and this requires us to have a centralised system using which the Device Farm and Infra squad can procure, setup and manage the device farm.
<br>
<b>Users</b>
Developer
Admin 
Client
<br>
<b>Roles</b>
Each location has a device farm (3 locations, 3 device farms)
Each device farm has hardware devices (Mobile phone,n/w equipement,USB cables , Servers) which are of type Shared and Dedicated
Infra Squad (Developer) has to perform operation such as  Procurement , setup , management of h/w devices with respect to device farm along with location of device farm as well as client .
Infra Squad (Developer) has to track the procurement request of client and assign devices based on device status : free/available, consumed, damaged.
Infra Squad (Developer) has to identify no, of devices which canbe connected to server.
Infra Squad (Admin) has to generate reports, maintain Audit logs and send notifications to developer.
Client can request for device , has to accept device and release device based on time period of the device mentioned. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* BACKEND : Python,Django Framework
* FRONTEND :HTML,CSS,AJAX,JQuery,Bootstrap
* DATABASE : MSQL

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

1.Install Python version 3.8 or Install Anaconda
2.Install MYSQL Workbench


### Installation
To install project locally on system follow the below steps.

Steps:

1.Download or Clone project using GitHub link.
2.Create local enviornment using venv or conda create --name command.
3.Install requirements.txt in the enviornment.
4.Run python manage.py makemmigrations command.
5.Run python manage.py migrate command.
6.Run python manage.py runserver localhost:8000

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1.There are 3 users involved in the application such as Client, Developer, Admin.
2.Login for all 3 users vary depending upon their user type.
3.Credentials for Developer and Admin are hard-coded for Developer and Admin due to time constarints,please refer credentials.txt.
4.Authentication is provided for Client login.

Please refer below url for getting started with web-application once the application is up and running on local system.

url :  http://localhost:8000/login

Navigate through below pages to understand the functionality:

1. Register : If new client visists,then he/she needs to register clicking on create an account link.
2. Login : If registration is done, then login using the credentials used in registeration.
3. Dashboard : If the login is of user type developer , then navigation will be done to dashboard where developer can perform operations like Add Mobile , Add Server, Edit Mobile, Edit Server, Procurement request.
4. Client_Dashboard : If login is of user type client , then navigation will be done to cient dashboard where client can perform Add request for Mobile and Server.
5. Admin : If you login as Admin then navigation will be done to Admin Page where charts and reports are shown with repect to mobile and server information and logs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


