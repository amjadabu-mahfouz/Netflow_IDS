from argparse import ArgumentParser
from IDS_main import IDS_core

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", default="Ethernet", 
                        help="specify the network INTERFACE to use. The default is Ethernet", metavar="INTERFACE")
    args = parser.parse_args()
    
    return args.interface

    

if __name__ == "__main__":
    interface = main()
    
    IDS_core(interface)     #use this call when running from the command line 
    #IDS_core('Wi-Fi')      #use this call instead when running from the python interpreter and pass the interface to listen at as a str  
