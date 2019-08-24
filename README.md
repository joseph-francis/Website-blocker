# Website Blocker
Python script that blocks certain websites during your working hours 

# What got me interested
Every website, every service has its own IP address. DNS (Domain Naming System) converts that to a readable name like www.facebook.com for example. 

The first time you type in a web address, your Mac pings a DNS server — typically one automatically configured for you by your Internet Service Provider — to find out the TCP/IP address of the server you're trying to connect to. Your Mac builds up a hidden cache file to remember those details later on when you visit the same site again.

The host file overrides the DNS information, which means you can have an IP address to reroute if you were to visit a website. In other words, you can block a website by writing a python script for it.
