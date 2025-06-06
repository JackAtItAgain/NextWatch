# Website Configuration #

In this walkthrough we will:
1.  Get and Configure DNS
2.  Get and Configure Apache2
3.  Configure CGI
4.  Get Digital Certificate

## Get and Configure DNS ##

1.	After purchasing your domain name from [namecheap.com](https://www.namecheap.com/)
2.	Navigate to Domain List
3.  Select Manage for your domain name
4.	Then Advanced DNS
5.	Under the heading HOST RECORDS, add new record
6.	Select A record as the Type
7.	Enter your EC2 Static IP Address in Value
8.	Click the tick to confirm

## Get and Configure Apache2 ##

1.	After Logging into EC2 Server, use the command:

    ```
      sudo apt update
2.	Followed by:

    ```
      sudo apt install apache2
3.	Then check if website is live in browser by visiting your IP or DNS (keep in mind that DNS can take a while before updating)
4.	If website does not load the default Apache2 webpage use:

    ```
      sudo systemctl start apache2
## Configure CGI ##

1.	Use the command to enable cgi module:

    ```
      sudo a2enmod cgi
2.	In the file "etc/apache2/mods-available/mime.conf" uncomment the line "AddHandler cgi-script .cgi" so it looks like this<br /><br /><img src="https://github.com/JackAtItAgain/NextWatch/blob/main/Documentation/VisualAids/AddHandler.png?raw=true" width="400">
3.	Then in the file "etc/apache2/apache2.conf" scroll down to the line <Directory /var/www/> and add "ExecCGI" to the end of the line beneath so it looks like this<br /><br /><img src="https://github.com/JackAtItAgain/NextWatch/blob/main/Documentation/VisualAids/ExecCGI.png?raw=true" width="400">
4.	Now navigate to "var/www" and make a new directory called cgi-bin
5.	Then in the file "etc/apache2/conf-available/serve-cgi-bin.conf" edit the "IfDefine ENABLE_USR_LIB_CGI_BIN" tag to look like this<br /><br /><img src="https://github.com/JackAtItAgain/NextWatch/blob/main/Documentation/VisualAids/CgiBinDirectory.png?raw=true" width="400">
6.	Then use command:

    ```
      systemctl restart apache2
## Get Digital Certificate ##

1.	Go to [certbot.eff.org](https://certbot.eff.org/)
2.	Select Apache and Linux (snap) like in the image below<br /><br /><img src="https://github.com/JackAtItAgain/NextWatch/blob/main/Documentation/VisualAids/Certbot.png?raw=true" width="400">
3.	Follow the instructions that appear to get the domain on https

## Summary ##

The website should now be live on https with Apache2 configured to execute CGI files located in var/www/cgi-bin/.

Next Walkthrough is [Scripting](Scripting.md)
