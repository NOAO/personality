# Python library
import logging
from collections import defaultdict
from pprint import pformat, pprint
# External packages
import astropy.io.fits as pyfits
# Local packages
#!from personality.personalities import personalities
#!import personality.hdr_decorators as hd
from pers.personalities import personalities
import pers.hdr_decorators as hd

def get_personality_names():
    return [persName for (persName,persDict) in personalities]

class NoPersonalityName(Exception):
    pass
    
#!def flat_hdudict(hdudict_list):
#!    """Combine key/value pairs from all HDUs into a single dict (returned).
#!    If key appears in multiple HDUs, first one wins."""
#!    hdudict = dict()
#!    for hdict in hdudict_list:
#!        for k,v in hdict.items():
#!            if k not in hdudict:
#!                hdudict[k] = v
#!    return hdudict

# InstVars: persdict, persName, update_dict, kwset
# Methods: name, options, params, param, functions,
#    make_update_dict, modify_hdudictlist, modify_fits
class Personality():
    
    def __init__(self, persName):
        # Raise exception if there is a duplicate Personality Name
        dupes = get_personality_names()
        for n in set(get_personality_names()):
            dupes.remove(n)
        if len(dupes) > 0:
            raise Exception('Duplicate personality name(s): {}'
                            .format(', '.join(dupes)))
        
        self.persdict = dict()    # like CONTENT of old Personality File
        self.persName = '<none>'  # like NAME    of old Personality File
        self.update_dict = dict() # k/v to update on HDU-0

        allpers = dict(personalities)
        if persName in allpers:
            self.persdict = allpers.get(persName)
            self.persName = persName
        else:
            pers_names = [pn for (pn,pd) in personalities]
            msg = ('Personality name ("{}") not found.  Available personalties'
                   ' are: {}.  '
                   ' To add more, see personality/personalities'
                   ).format(persName, ', '.join(pers_names))
            raise NoPersonalityName(msg)

        # KeyWords used by any hdrfuncs
        self.kwset = hd.all_in_keywords.union(hd.all_out_keywords)

    def name(self):
        return self.persName

    def options(self):
        return self.persdict['options'].items()

    def params(self):
        return self.persdict['params'].items()

    def param(self, name):
        if params not in self.persdict:
            return None
        return self.persdict.get('params').get(name)

    def functions(self):
        return self.persdict.get('calchdr',[])
    
    def make_update_dict(self, hdu_dict_list):
        """Apply personality to header.
        The personality does not specify which HDU keywords are to be found in.
        OUTPUT keywords are put in same HDU as first original was found in, 
        if any (overwriting old value), else new value put in HDU-0.
        INPUT keyword value comes from first HDU that has the keyword.

        RETURN: dict[hduidx][key] = value
           Gives keys and values for specific HDUs 
        """
        # Flatten all HDUs into single (hdu0dict)
        #!print('DBG: hdudict_list={}'.format(pformat(hdudict_list)))
        #!hdudict = flat_hdudict(hdu_dict_list)
        kwset = set()
        kwset.update(set([k for k,v in self.options()]),
                     hd.all_in_keywords,
                     hd.all_out_keywords)
        kwhdu = dict() # kwhdu[kw] = hduidx
        for hduidx,hdu_dict in enumerate(hdu_dict_list):
            for kw in kwset:
                if kw in hdu_dict:
                    kwhdu[kw] = hduidx
                    continue # Got first use of kw, next kw

        
        hduidxdict = defaultdict(dict) # dict[hduidx][key] = value
        # create initial hdu dict list subset from needed fields
        for k in kwset:
            idx = kwhdu.get(k,0)
            if k in hdu_dict_list[idx]:
                hduidxdict[idx][k] = hdu_dict_list[idx][k]

        # Apply personality "options" (direct field values)
        for k,v in self.options():
            # overwrite with explicit fields from personality
            hduidxdict[kwhdu.get(k,0)][k] = v
            
        flat  = dict() # flat[fitsKeyword] = val
        for k in kwset:
            if k in hduidxdict[kwhdu.get(k,0)]:
                flat[k] = hduidxdict[kwhdu.get(k,0)][k]

        # Apply hdr funcs
        #logging.debug('Flat= {}'.format(flat))
        for calcfunc in self.functions():
            newflat = calcfunc(flat)
            flat.update(newflat)
            logging.debug('Ran hdrfunc: {}=>{}'
                         .format(calcfunc.__name__, newflat))
            # Update
            for k,v in newflat.items():
                hduidxdict[kwhdu.get(k,0)][k] = v                
        self.update_dict = hduidxdict
        #logging.debug(f'update_dict={pformat(dict(self.update_dict))}')
        return self.update_dict

    def modify_hdudictlist(self, hdudictlist):
        """Modify hdudictlist IN-PLACE to reflect updates formed from 
        Personality"""
        if len(self.update_dict) == 0:
            self.make_update_dict(hdudictlist)

        for idx,hdudict in self.update_dict.items():
            if idx < len(hdudictlist):
                for k,v in self.update_dict[idx].items():
                    if k in hdudictlist[idx]:
                        hdudictlist[idx][k] = v
                    else:
                        hdudictlist[0][k] = v
                        
    def modify_fits(self, orig_fits_fname, new_fits_fname):
        logging.debug(f'modify_fits({orig_fits_fname},{new_fits_fname})')
        with pyfits.open(orig_fits_fname) as hdulist:
            #!hdulist[0].header.update(self.update_dict)
            for idx,hdudict in self.update_dict.items():
                if idx < len(hdulist):
                    for k,v in self.update_dict[idx].items():
                        if k in hdulist[idx].header:
                            hdulist[idx].header[k] = v
                        else:
                            hdulist[0].header[k] = v
            hdulist.writeto(new_fits_fname, output_verify='fix')
        return new_fits_fname
        
