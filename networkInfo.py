from libraries.ipCalculator import subnetCalculator
if __name__ == '__main__':
    IpPrefix = input('Enter IP address in IP/Mask Form : ')
    net = subnetCalculator(IpPrefix)
    net.toString()
#   print('Hosts List : ' , net.Hosts())
#   print('Parent Network : ' , net.parentNetwork(prefixlenDiff=5))
#   print('Subnets Blocks : ' , net.subNetworks(newPrefix=21))
