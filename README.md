# SubnetCalculator
A Python subnet calculator class using built-in ipaddress module

## Availlable Methods:

- [x]  def Broadcast(self)
- [x]  def Cidr(self)
- [x]  def FirstAddress(self)
- [x]  def Hosts(self)
- [x]  def HostAddress(self)
- [x]  def LastAddress(self)
- [x]  def Mask(self)
- [x]  def Netmask(self)
- [x]  def NetworkAddress(self)
- [x]  def Range(self)
- [x]  def Size(self)
- [x]  def subNetworks(self, newPrefix: int = 0, subnetMask: str=None)
- [x]  def parentNetwork(self, newPrefix: int = 0, prefixlenDiff: int = 0)
- [x]  def toString(self)
- [x]  def Wildcard(self)

## Usage:

Retrieve informations about a given CIDR IP address

``` python

from libraries.tools import subnetCalculator
if __name__ == '__main__':
    prefix = input('Enter IP address in IP/Mask Form : ')
    net = subnetCalculator(prefix)
    net.toString()
#   print('Hosts List : ' , net.Hosts())
    print('Parent Network : ' , net.parentNetwork(prefixlenDiff=1))
    print('Subnets Blocks : ' , net.subNetworks(newPrefix=25))
    
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
