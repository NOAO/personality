#! /usr/bin/env python
# Python Library
from unittest import skip
import unittest
from collections import OrderedDict
from pprint import pformat
import warnings
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

    @classmethod
    def setUpClass(cls):
        warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
        

    def test_bok23m_90prime(self):
        fits_name = 'test-data/bok23m-90prime/d7212.0062.fits.fz'
        pers_name = 'bok23m-90prime'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')


    def test_ct09m_ccd_imager(self):
        fits_name = 'test-data/ct09m-ccd_imager/FIX_20160818.09.136.fits.fz'
        pers_name = 'ct09m-ccd_imager'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')
        
    def test_ct13m_andicam(self):
        fits_name = 'test-data/ct13m-andicam/FIXED_ir141225.0179.fits.fz'
        pers_name = 'ct13m-andicam'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')
        
    #@skip('no sample file provided')
    def test_ct15m_chiron(self):
        fits_name = 'test-data/ct15m-chiron/FIX_chi170717.1304.fits.fz'
        pers_name = 'ct15m-chiron'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')
    
    @skip('No clean example available')
    # OBSID keyword in an "eschelle" instrument refers to a "chiron" instrument.
    def test_ct15m_echelle(self):
        fits_name = 'test-data/ct15m-echelle/FIXED_chi150724.1000.fits.fz'
        pers_name = 'ct15m-echelle'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_ct4m_arcoiris(self):
        fits_name = 'test-data/ct4m-arcoiris/SPEC_ARC1724.fits.fz'
        pers_name = 'ct4m-arcoiris'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_ct4m_cosmos(self):
        fits_name = 'test-data/ct4m-cosmos/n2.25522.fits.fz'
        pers_name = 'ct4m-cosmos'
        hdl = hdudictlist(fits_name)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_ct4m_decam(self):
        fits_name = 'test-data/ct4m-decam/DECam_00482540.fits.fz'
        pers_name = 'ct4m-decam'
        hdl = hdudictlist(fits_name)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')
        
    def test_kp09m_hdi(self):
        fits_name = 'test-data/kp09m-hdi/c7015t0267b00.fits.fz'
        pers_name = 'kp09m-hdi'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_kp4m_kosmos(self):
        fits_name = 'test-data/kp4m-kosmos/a.20152.fits.fz'
        pers_name = 'kp4m-kosmos'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    #@skip('no sample file provided')
    def test_kp4m_mosaic_1_1(self):
        fits_name = 'test-data/kp4m-mosaic_1_1/n1.65961.fits.fz'
        pers_name = 'kp4m-mosaic_1_1'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_kp4m_mosaic3(self):
        fits_name = 'test-data/kp4m-mosaic3/mos3.75870.fits.fz'
        pers_name = 'kp4m-mosaic3'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_kp4m_newfirm(self):
        fits_name = 'test-data/kp4m-newfirm/FIXED_nhs_2015_n04_319685.fits.fz'
        pers_name = 'kp4m-newfirm'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')


    def test_soar_goodman(self):
        fits_name = 'test-data/soar-goodman/0079.spec_flat.fits.fz'
        pers_name = 'soar-goodman'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')
        
    def test_soar_osiris(self):
        fits_name = 'test-data/soar-osiris/SO2014B-015_1215.0188.fits.fz'
        pers_name = 'soar-osiris'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_soar_sami(self):
        fits_name = 'test-data/soar-sami/FIXED_SO2016B-015.013.fits.fz'
        pers_name = 'soar-sami'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_soar_soi(self):
        fits_name = 'test-data/soar-soi/FIXED_test.027.fits.fz'
        pers_name = 'soar-soi'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_soar_spartan(self):
        fits_name = 'test-data/soar-spartan/S301D_K012-0484d0.fits.fz'
        pers_name = 'soar-spartan'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_wiyn_bench(self):
        fits_name = 'test-data/wiyn-bench/FIXED_24dec_2014.061.fits.fz'
        pers_name = 'wiyn-bench'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')

    def test_wiyn_whirc(self):
        fits_name = 'test-data/wiyn-whirc/FIXED_obj_355.fits.fz'
        pers_name = 'wiyn-whirc'
        hdl = hdudictlist(fits_name)
        pers = Personality(pers_name)
        pers.modify_hdudictlist(hdl)
        #print('DBG-pers: {} hdl={}'.format(pers_name, pformat(hdl)))
        expected = exp.he.get(pers_name,dict())
        self.assertEqual(hdl, expected,'Actual to Expected')
        

if __name__ == '__main__':
    unittest.main()
    
        
