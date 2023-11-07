# Web infrastructure design
 This project is aim to learn how to design a web infrastructure.

## Key Concepts
- Server

- Web server

- Application server

- Network basic

- Database

- Firewall

- Load balancer

- DNS & DNS record type

- HTTP & HTTPS

- Monitoring

- Single point of failure (SPOF)

# File description
Some files contains a link to the image hosted on Imgbox (an image hosting flatform),
while others contains a detailed explaination of each tool used on the web server infrastructure.

## [0-simple_web_stack](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack)
On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start your explanation by having a user wanting to access your website

###  Requirements
- 1 server

- 1 web server (Nginx)

- 1 application server

- 1 application files (your code base)

- 1 database (MySQL)

- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

## [1-distributed_web_infrastructure](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure)
On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com.

###  Requirements
You must add to - [0-simple_web_stack](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack)
- 2 servers

- 1 web server (Nginx)

- 1 application server

- 1 load-balancer (HAproxy)

- 1 set of application files (your code base)

- 1 database (MySQL)

## [2-secured_and_monitored_web_infrastructure](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure)

On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

###  Requirements

You must add to - [1-distributed_web_infrastructure](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure)

- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)

## [3-scale_up](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/3-scale_up)

## Requirements
You must add to - [2-secured_and_monitored_web_infrastructure](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure)

- 1 server
- 1 load-balancer (HAproxy) configured as cluster with the other one
- Split components (web server, application server, database) with their own server

## Files
| FILENAME  |DESCRIPTION    |
|-------|-------------|
|[0-simple_web_stack](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack)| Web Infrastructure Design with a LAMP stack. This contains: 1 server, 1 web server, 1 application server, 1 database and 1 domain name|
| [1-distributed_web_infrastructure](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure)| Web Infrastructure Design, based on 0-simple_web_stack that contains some additional components: 1 server, 1 web server, 1 application server, 1 load-balancer, 1 set of application files, 1 database| 
|[2-secured_and_monitored_web_infrastructure](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure) |Web Infrastructure Design, based on 1-distributed_web_infrastructure that contains some additional components: 3 firewalls, 1 SSL certificate, 3 monitoring clients|
|[3-scale_up](https://github.com/TechieGold/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/3-scale_up)| Web Infrastructure Design, based on 2-secured_and_monitored_web_infrastructure that contains some additional components: 1 server, 1 load-balancer|







