# Website Configuration #

### In this walkthrough we will: ###
1. Get and configure DNS
2. Get and configure apache2
3. Configure cgi
4. Get digital certificate

## Get and configure DNS ##

1.	On namecheap purchase your domain name
2.	Go to Domain list, then Advanced DNS
3.	Add new host record, type A record, and enter the EC2 Static IP Address

## Get and configure apache2 ##

1.	First use command “sudo apt update”
2.	Then use “sudo apt install apache2”
3.	Check if website is live in browser
4.	If not use “sudo systemctl start apache2”

## Configure cgi ##

1.	Use the command “sudo a2enmod cgi” to enable cgi module
2.	In etc/apache2/mods-available/mime.conf uncomment AddHandler cgi-script .cgi so it looks like this 
3.	Then in etc/apache2/apache2.conf scroll down to Directory /var/www/> and add ExecCGI to the end of the line below so it looks like this 
4.	In var/www/html make a new directory called cgi-bin and put your cgi files there
5.	Then in etc/apache2/conf-available/serve-cgi-bin.conf change the bottom to look like this 
6.	Then use command “systemctl restart apache2”

## Get digital certificate ##

1.	Go to certbot.eff.org
2.	Select Apache and Linux (snap) like in the image below 
3.	Follow the instructions to get the domain on https

## Summary ##
