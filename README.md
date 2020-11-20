# creating http endpoint server to connect OCi API GW to Oracle Autonomous Database
## Create an "always free" virtual machine in OCI
We'll create an "always free" VM with Oracle Linux 7.x installed in it.
1. login to the OCI Console. In the Home page, under quick actions, click create Vm Instance
<br>![quick actions](https://github.com/ravi041282/oci-apigw-atp/blob/main/screenshots/quickactions.jpg)
2. In the Create Compute instance page, enter a name for the VM
<br>![create compute instance](https://github.com/ravi041282/oci-apigw-atp/blob/main/screenshots/createcompute.jpg)
3. Click 'Show Shape, Network and Storage Options' and then make sure that you pick the 'Always Free' shape
<br>![always free shape](https://github.com/ravi041282/oci-apigw-atp/blob/main/screenshots/alwaysfree.jpg)
4. we'll need an ssh keypair to login to the instance once it is provisioned. Generate an ssh keypair using [ssh-keygen](https://www.ssh.com/ssh/keygen/) on Linux or Macbook. Use Puttygen to generate the keypair if you are on WIndows
5. After the keypair is generated, save both private and public keys to a directory.
6. Open the public key with a text editor and copy the text. Back in the OCI Console, paste the copied text in to the box that says **Add SSH key**. Alternatively, you can select **choose SSH key file** and upload the public key file, by browsing to the directory where keys are saved.
<br>![Add ssh key](https://github.com/ravi041282/oci-apigw-atp/blob/main/screenshots/sshkey.jpg)
7. Click create. It will take a couple of minutes for the instance to get provisioned.
8. Copy the public-ip address of the instance. 
<br>![provisioned instance]https://github.com/ravi041282/oci-apigw-atp/blob/main/screenshots/runninginstance.jpg)
connect to the instance to verify you can login successfully
   * Connect from a Linux/Mac Machine using the default cli tool like terminal using ssh command.
   <br>`ssh -i /path/to/private/key/file opc@public-ip`
   * Connect from Windows using a tool like putty.

## Configure the VM for http endpoint
1. make sure the virtual machine has latest python version installed using the command:
<br>`python3 version`
1. install flask using pip:
<br> `sudo pip3 install flask`
1. clone this git repo using the command:
<br>`git clone https://github.com/ravi041282/oci-apigw-atp.git`
1. `cd` to the directory `oci-apigw-atp`
1. create a python venv by running the command:
<br> `python3 -m venv venv`
1. Navigate to the directory `./venv/bin/` and run: <br>`sh activate`
1. Navigate back to `oci-apigw-atp`. you should notice two files named `app.py` & `atpconnect.sh`
   1. `app.py` - has to code to publish various routes and one of them routes us to the atp connect script
   1. `atpconnect.sh` - the pythin script has a route to this script and this script connects to ATP to retrieve user details.
1. For now, we will leave the scripts as-is & test the flask connection.
1. Make sure you are in the directory `oci-apigw-atp` and run: <br>`flask run`

## Configure OCI Security list to allow traffic on port 5000
1. Flask applications run by default on port 5000. we'll need to open this port on the security list(firewall)
1. Back in the OCI Console navigate to Hamburger Menu > Networking > Virtual Cloud Networks
<br>![hamburger menu](https://github.com/ravi041282/oci-apigw-atp/blob/main/screenshots/hamburger.jpg)
1. click on the VCN you have created and in the VCN page, click on Security Lists link under Resources
<br>![security lists](https://github.com/ravi041282/oci-apigw-atp/blob/main/screenshots/securitylists.jpg)
1. Click on the security list wihich starts with name **Default Security List**
1. Under Ingress Rules, click Add Ingress Rules button.
1. In the Add Ingress rules Window, enter `0.0.0.0/0` in the SOURCE CIDR box and enter `5000` in the DESTINATION PORT RANGE box and click Add Ingress Rules button to the bottom left.
<br>![add ingress](https://github.com/ravi041282/oci-apigw-atp/blob/main/screenshots/addingress.jpg)
1. open a new browser window and navigate to [http://public-ip.of.the.vm:5000](http://)
<br>![server works!](https://github.com/ravi041282/oci-apigw-atp/blob/main/screenshots/serverworks.jpg)

We have successfully configured the http endpoint.








