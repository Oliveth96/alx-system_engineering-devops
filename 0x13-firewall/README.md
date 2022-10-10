<h1>0x13. Firewall</h1>



| TASKS | FILES | DESCRIPTION |
|-------|-------|-------------|
| 0. Block all incoming traffic | [0-block_all_incoming_traffic_but](https://github.com/Oliveth96/alx-system_engineering-devops/0x13-firewall/0-block_all_incoming_traffic_but)| Let’s install the ufw firewall and setup a few rules on web-01. Share the ufw commands that you used in your answer file. <ol>Requirements:</ol> <li>The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)</li><li>Configure ufw so that it blocks all incoming traffic, except the following TCP ports:</li><li>22 (SSH)</li><li>443 (HTTPS SSL)</li><li>80 (HTTP)</li> |
| 1. Port forwarding |[100-port_forwarding](https://github.com/Oliveth96/alx-system_engineering-devops/0x13-firewall/100-port_forwarding)| Firewalls can not only filter requests, they can also forward them. <ol>Requirements:</ol> <li>Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.</li><li>Your answer file should be a copy of the ufw configuration file that you modified to make this happen</li><li>My web server nginx is only listening on port 80</li><li>netstat shows that nothing is listening on 8080</li> |


AUTHOR
<hr>

[Oliveth Ndubuka](https://github.com/Oliveth96)