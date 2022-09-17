<center> <h1>0x0A. Configuration management</h1> </center>
<span> DevOps
SysAdmin
Scripting
CI/CD
</span>


General
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file at the root of the folder of the project is mandatory
Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
Your Puppet manifests must run without error
Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
Your Puppet manifests files must end with the extension .pp
 
<h6>Install puppet </h6>
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet


---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |

| 0: Create a file | 0-create_a_file.pp | Using Puppet, create a file in /tmp|
| 1: Install a package| 1-install_a_package.pp | Using Puppet, install flask from pip3|
| 2: Execute a command | 2-execute_a_command.pp | Using Puppet, create a manifest that kills a process named killmenow |
