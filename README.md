# SubnetCalculator
A Python subnet calculator class using built-in ipaddress module

## Availlable Methods:

## Usage:

Retrive informations about a given CIDR IP address

``` python

from libraries.ipCalculator import subnetCalculator
if __name__ == '__main__':
    IpPrefix = input('Enter IP address in IP/Mask Form : ')
    netInfo = subnetCalculator(IpPrefix)
    netInfo.toString()
    
```

## Output

```python

Enter IP address in IP/Mask Form : 192.168.0.0/16
Host Address :  192.168.0.0
Network Address :  192.168.0.0
Subnet Mask :  255.255.0.0
Mask :  /16
CIDR Notation :  192.168.0.0/16
Broadcast Address :  192.168.255.255
Wildcard Mask :  0.0.255.255
First IP :  192.168.0.1
Last IP :  192.168.255.254
Range :  192.168.0.1-192.168.255.254
Hosts Count :  65534

```
