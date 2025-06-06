# Server Creation #

### In this walkthrough we will: ###
1. Launch ec2 instance
2. Get static ipv4 address
3. Set up ssh to server

## Launch EC2 Instance ##

1.	In EC2 find instances and click “Launch instances”
2.	Select Ubuntu 24.04 LTS for the operating system
3.	Instance type is t2.micro
4.	Create new key pair
5.	Create security group, click “edit” and add a rule, select http for the type
6.	Then create another rule in the same security group but this time select https for the type
7.	Add a 20GiB SSD
8.	Check that the instance is in the free tier it should look like this, then click “Launch instance”

## Get static ipv4 address ##

1.	Go to EC2 dashboard
2.	From there navigate to Elastic Ips
3.	Select your newly created instance
4.	Then click Allocate Elastic IP address
5.	Click Allocate

## Set up ssh to server ##

I find that creating a .bat file that automatically logs in to my ec2 instance is very convenient and can save time.

1.	Enable OpenSSH in the windows features settings if OpenSSH is not already installed
2.	In a new text file write “ssh -i ‘file_name_of_your_key_pair’ ‘username@ec2_instance_ip_address’”
3.	Save as a .bat file ideally in the same folder as your key pair
4.	Setting Key Pair Permissions
  a.	Go to the key pair file -> properties -> security -> advanced
  b.	Click disable inheritance and then convert inherited permissions to explicit permissions on this object
  c.	At the second line of the window change owner to your account
  d.	Finally, remove all permission entries except for the ones for your account
  e.	Apply changes and then click ok
5.	This file can now be run and will automatically open terminal and log into your ec2 instance
