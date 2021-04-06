from ipaddress import NetmaskValueError, AddressValueError
import  ipaddress

class subnetCalculator(object):
    def __init__(self, cidrAddress: str=None):
        cidrAddress = cidrAddress if cidrAddress is not None else input('Enter IP address in IP/Mask Form : ')
        try:
            self.__objAddress = ipaddress.ip_interface(cidrAddress)
        except (AddressValueError, NetmaskValueError):
            raise ValueError('%r does not appear to be an IPv4 or IPv6 Nework address' % cidrAddress)

    def Broadcast(self):
        return self.__objAddress.network.broadcast_address

    def Cidr(self):
        return str(self.__objAddress.network)

    def FirstAddress(self):
        NetAddr = self.__objAddress.network
        return list(NetAddr.hosts())[0]

    def Hosts(self):
        NetAddr = self.__objAddress.network
        return list(NetAddr.hosts())

    def HostAddress(self):
        return self.__objAddress.ip
        
    def LastAddress(self):
        NetAddr = self.__objAddress.network
        return list(NetAddr.hosts())[-1]

    def Mask(self):
        return '/' + str((self.__objAddress.with_prefixlen).split('/')[1])

    def Netmask(self):
        return (self.__objAddress.with_netmask).split('/')[1]

    def NetworkAddress(self):
        return str(self.__objAddress.network).split('/')[0]

    def Range(self):
        return '{}-{}'.format(self.FirstAddress(), self.LastAddress())

    def Size(self):
        return len(self.Hosts())

    def subNetworks(self, newPrefix: int = 0, subnetMask: str=None):
        ipn = ipaddress.ip_network(str(self.__objAddress.network))
        try:
            if isinstance(newPrefix, int) and newPrefix > 0 :
                minPrefix = (int((self.Mask()).strip('/')) + 1)
                if minPrefix > 31 or newPrefix not in range(minPrefix, 32, 1) :
                    raise ValueError('Invalid Subnet prefix given: %r' % newPrefix)
                return list(ipn.subnets(new_prefix=newPrefix))
            if subnetMask is not None :
                if not(ipaddress.IPv4Address(subnetMask)):
                    raise ValueError('Invalid Subnet netmask given: %r' % subnetMask)
                subnetMaskBits = bin(int(ipaddress.IPv4Address(subnetMask))).count('1')
                netmaskBits = bin(int(ipaddress.IPv4Address(self.Netmask()))).count('1')
                return list(ipn.subnets(prefixlen_diff=(subnetMaskBits-netmaskBits)))
        except ValueError as e:
            raise
        return list(ipn.subnets())

    def parentNetwork(self, newPrefix: int = 0, prefixlenDiff: int = 0):
        ipn = ipaddress.ip_network(str(self.__objAddress.network))
        try:
            maxValue = (int((self.Mask()).strip('/')) - 1) 
            if isinstance(newPrefix, int) and newPrefix > 0 :
                if maxValue < 1 or newPrefix not in range(1, maxValue, 1) :
                    raise ValueError('Invalid Subnet prefix given: %r' % newPrefix)
                return str(ipn.supernet(new_prefix=newPrefix))
            if isinstance(prefixlenDiff, int) and prefixlenDiff > 0 :
                if maxValue < 1 or prefixlenDiff not in range(1, maxValue, 1) :
                    raise ValueError('Invalid network prefixlen_diff given: %r' % prefixlenDiff)
                return str(ipn.supernet(prefixlen_diff=prefixlenDiff))
        except ValueError as e:
            raise
        return str(ipn.supernet())

    def toString(self):
        print('Host Address : ', self.HostAddress())
        print('Network Address : ', self.NetworkAddress())
        print('Subnet Mask : ', self.Netmask())
        print('Mask : ', self.Mask())
        print('CIDR Notation : ', self.Cidr())
        print('Broadcast Address : ' , self.Broadcast())
        print('Wildcard Mask : ' , self.Wildcard())
        print('First IP : ' , self.FirstAddress())
        print('Last IP : ' , self.LastAddress())
        print('Range : ' , self.Range())
        print('Hosts Count : ' , self.Size())

    def Wildcard(self):
        return self.__objAddress.hostmask


if __name__ == '__main__':
    exit('Direct access denied !')
