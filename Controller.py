""" 
Main interface of OVPL with the external world.
Controller interfaces with LabPoolManager and VMPoolManager.

"""

import logging

import LabManager
import VMPoolManager

OVPL_LOGGER = logging.getLogger('ovpl')
LOG_FILENAME = '/root/ovpl/log/ovpl.log'       # make log name a setting
LOG_FD = open(LOG_FILENAME, 'a')

class Controller:
    def __init__(self):
        pass

    def test_lab(self, lab_id, lab_src_url, version=None):
        print "Controller.test_lab()"
        try:
            lab_spec = LabManager.get_lab_reqs(lab_id, lab_src_url, version)
            vmpoolmgr = VMPoolManager.VMPoolManager()
            (ip, port) = vmpoolmgr.create_vm(lab_spec)
            #(ip, port) = ("10.4.14.22", "8089")
            vmmgrurl = "http://" + ip
            
            print 'created vm ', ip, port
            print "vm manager url is :", vmmgrurl
            print "vm mgr port is :", port
            print "lab src url is: ", lab_src_url
            if LabManager.test_lab(vmmgrurl, port, lab_src_url, version):
                return ip
            else:
                return "Test failed"
        except Exception, e:
            # This should return an error json when Controller is a web service
            print e
        

if __name__ == '__main__':
    c = Controller()
    #c.test_lab("asdf", "asdf")
    #print c.test_lab("ovpl01", "https://github.com/nrchandan/vlab-computer-programming")
    print c.test_lab("ovpl01", "https://github.com/avinassh/cse09")