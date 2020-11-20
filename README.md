# creating http endpoint server to connect OCi API GW to Oracle Autonomous Database
## Create an "always free" virtual machine in OCI
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

