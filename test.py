# Python Library
from unittest import skip
import unittest
from collections import OrderedDict
from pprint import pformat
# External packages
import astropy.io.fits as pyfits
# Local Packages
from pers.Personality import Personality
import expected as exp

def hdudictlist(fitsfile):
    """Read HDU headers into list of python dicts.  
    EXCEPTIONS:
       If key duplicated in an HDU.
       If headers cannot be read
    """
    ignoreflds = {'SIMPLE','BITPIX','NAXIS', 'EXTEND',
                  'CHECKSUM', 'DATASUM',
                  'COMMENT','HISTORY',''}
    odictlist = list()
    with pyfits.open(fitsfile) as hdulist:
        for hidx, hdu in enumerate(hdulist):
            foundflds = set()
            items = list()
            for k,v in hdu.header.items():
                if k in ignoreflds:
                    continue
                if k in foundflds:
                    raise Exception(
                        'Duplicate key "{}" found in HDU {} of "{}"'
                        .format(k,hidx,fitsfile))
                items.append((k,v))
                foundflds.add(k)
            odictlist.append(OrderedDict(items))
    return odictlist




class TestApplyPersonalies(unittest.TestCase):
    @skip('input file not valid')
    def test_wiyn_whirc(self):
        fits_name = 'test-data/20110101/wiyn-whirc/obj_355.fits.fz'
        pers_name = 'wiyn-whirc'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        expected = []
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_kp4m_mosaic3(self):
        fits_name = 'test-data/20160314/kp4m-mosaic3/mos3.75870.fits.fz'
        pers_name = 'kp4m-mosaic3'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG: kp4m-mosaic3 hdl={}'.format(pformat(hdl)))
        expected = exp.kp4m_mosaic3
        self.assertEqual(hdl, expected,'Actual to Expected')

        

if __name__ == '__main__':
    unittest.main()
    
        
