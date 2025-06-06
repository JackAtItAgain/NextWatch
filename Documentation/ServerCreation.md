# Server Creation #

In this walkthrough we will:
1.  Launch EC2 Instance
2.  Get Static IPv4 Address
3.  Set up SSH to Server

## Launch EC2 Instance ##

1.  From EC2 Dashboard navigate to Instances
2.	Click “Launch instances”
3.	Select Ubuntu 24.04 LTS for the operating system
4.	Instance type is t2.micro
5.	Create new Key Pair
6.	Create Security Group, click “edit” and add a rule, select http for the type
7.	Then create another rule in the same security group but this time select https for the type
8.	Add a 20GiB SSD
9.	Check that the instance is in the free tier it should look like this
  <img src="https://github.com/JackAtItAgain/NextWatch/blob/main/Documentation/VisualAids/InstanceSummary.png" width="400">
10.	Then click “Launch instance”

## Get Static IPv4 Address ##

1.	From EC2 Dashboard navigate to Elastic IPs
3.	Select your newly created instance
4.	Then click Allocate Elastic IP Address
5.	Click Allocate

## Set up SSH to Server ##

Let's set up a .bat file that we can run to automatically log into your EC2 Instance.
I find this is convenient and has saved my time.

1.	To enable OpenSSH Client if not already installed on your desktop
    * In settings navigate to System -> Optional features
    * Search for OpenSSH Client in the Added features box
    *  If you OpenSSH Client appears continue on to step 3, otherwise click "View features"
    * Search for OpenSSH Client, select and click next
    * Follow process until finished
2.	In a new text file write

    ```
      “ssh -i ‘file_name_of_your_key_pair’ ‘username@ec2_instance_ip_address’”
3.	Save as a .bat file ideally in the same folder as your key pair
4.	Setting Key Pair Permissions
    * Go to the key pair file -> properties -> security -> advanced
    * Click disable inheritance and then convert inherited permissions to explicit permissions on this object
    * At the second line of the window change owner to your account
    * Finally, remove all permission entries except for the ones for your account
    * Apply changes and then click ok
5.	Should now be able to double click .bat file and it will open terminal and log into your ec2 instance for you

## Summary ##

Amazon EC2 Instance should now be live with an attached Static IPv4 Address and you should be able to ssh into the Server via .bat file.

Next Walkthrough is [Website Configuration](WebsiteConfiguration.md)
