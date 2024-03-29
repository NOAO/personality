"""\
FITS header calculation functions (hdrfunc).

Each function is passed a dictionary containing only the fields it
needs (per the @inkws decorator). It then RETURNS a dictionary of
field name/values to be updated.  

NB: The program that calls these functions must do some extra
bookkeeping to scrape the input keywords from multiple HDUs and to
update the values into the first HDU that contains the keyword (or
HDU-0 if no HDU contains it)

All functions have the same signature.

"""

# Grouped by OUTPUT Keyword

import logging
from pers.hdr_decorators import inkws, outkws


#########################
### DTSERNO
###

@inkws(['DETSERNO'])
@outkws(['DTSERNO'])
def DETSERNOtoDTSERNO(orig, **kwargs):
    """Intended for soar-spartan FITS files. Allow DETSERNO to be missing."""
    return {'DTSERNO': orig['DETSERNO'].strip()}

#########################
### DATE-OBS
###

@inkws(['UTSHUT'])
@outkws(['DATE-OBS'])
def fixTriplespec(orig, **kwargs):
    """Fix triplespec DATE-OBS using UTSHUT (Universal Time SHUTter)"""
    new = {'DATE-OBS': orig['UTSHUT'],
           #'INSTRUME': orig['INSTRUM'],
    }
    logging.debug('fixTriplespec: fields DATE-OBS ({})'
                  #', INSTRUME ({})'
                  #.format(new['DATE-OBS'], new['INSTRUME']))
                  .format(new['DATE-OBS']))
    return  new


@inkws(['DATE-OBS', 'TIME-OBS'])
@outkws(['DATE-OBS'])
def addTimeToDATEOBS(orig, **kwargs):
    """Use TIME-OBS for time portion of DATEOBS."""
    if ('T' in orig['DATE-OBS']): 
        return {'DATE-OBS': orig['DATE-OBS']}
    else:
        return {'DATE-OBS': orig['DATE-OBS'] + 'T' + orig['TIME-OBS']}


@inkws(['DATE-OBS'])
@outkws(['DATE-OBS'])
def addTToDATEOBS(orig, **kwargs):
    import datetime as dt
    if ('T' in orig['DATE-OBS']):
        return {'DATE-OBS': orig['DATE-OBS']}
    else:
        return {'DATE-OBS':dt.datetime.strptime(orig['DATE-OBS'], '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%dT%H:%M:%S.%f')}


@inkws(['DATE-OBS', 'DATE'])
@outkws(['ODATEOBS', 'DATE-OBS'])
def DATEOBSfromDATE(orig, **kwargs):
    """hdr function: DATEOBSfromDATE"""
    if 'ODATEOBS' in orig:
        logging.info('Overwriting existing ODATEOBS!')
    return {'ODATEOBS': orig['DATE-OBS'],            # save original
            'DATE-OBS': orig['DATE']+'.0' }


#########################
### DTCALDAT
###

@inkws(['DATE-OBS'])
@outkws(['DTCALDAT'])
def DTCALDATfromDATEOBStus(orig, **kwargs):
    """hdr function: DTCALDATfromDATEOBStus"""
    from dateutil import tz
    import datetime as dt

    local_zone = tz.gettz('America/Phoenix')
    utc = dt.datetime.strptime(orig['DATE-OBS'], '%Y-%m-%dT%H:%M:%S.%f')
    utc = utc.replace(tzinfo=tz.tzutc()) # set UTC zone
    localdt = utc.astimezone(local_zone)
    if localdt.time().hour > 9:
        caldate = localdt.date()
    else:
        caldate = localdt.date() - dt.timedelta(days=1)
    #!logging.debug('localdt={}, DATE-OBS={}, caldate={}'
    #!              .format(localdt, orig['DATE-OBS'], caldate))
    new = {'DTCALDAT': caldate.isoformat()}
    return new


@inkws(['DATE-OBS'])
@outkws(['DTCALDAT'])
def DTCALDATfromDATEOBSchile(orig, **kwargs):
    """hdr function: DTCALDATfromDATEOBSchile"""
    from dateutil import tz
    import datetime as dt

    local_zone = tz.gettz('Chile/Continental')
    utc = dt.datetime.strptime(orig['DATE-OBS'], '%Y-%m-%dT%H:%M:%S.%f')
    utc = utc.replace(tzinfo=tz.tzutc()) # set UTC zone
    localdt = utc.astimezone(local_zone)
    if localdt.time().hour > 12:
        caldate = localdt.date()
    else:
        caldate = localdt.date() - dt.timedelta(days=1)
    logging.debug('localdt={}, DATE-OBS={}, caldate={}'
                  .format(localdt, orig['DATE-OBS'], caldate))
    new = {'DTCALDAT': caldate.isoformat()}
    return new


#########################
### DTPROPID
###

@inkws(['PROPID'])
@outkws(['DTPROPID'])
def PROPIDplusCentury(orig, **kwargs):
    """Add missing century"""
    return {'DTPROPID': '20' + orig.get('PROPID','NA').strip('"') }

@inkws(['PROPID'])
@outkws(['DTPROPID'])
def PROPIDtoDT(orig, **kwargs):
    """Copy PROPID to DTPROPIOD"""
    if 'DTPROPID' in orig:
        return {'DTPROPID': orig.get('DTPROPID') }
    else:
        if 'PROPID' in orig:
            return {'DTPROPID': orig.get('PROPID') }
        else:
            return {}

#########################
### DTINSTR
###

@inkws(['INSTRUME'])
@outkws(['DTINSTRU'])
def INSTRUMEtoDT(orig, **kwargs):
    """hdr function: INSTRUMEtoDT"""
    if 'DTINSTRU' in orig:
        return {'DTINSTRU': orig['DTINSTRU'] }
    else:
        return {'DTINSTRU': orig['INSTRUME'] }

#########################
### PROPOSAL
###

@inkws(['PROPOSAL'])
@outkws(['PROPID'])
def PROPOSALtoPROPID(orig, **kwargs):
    """Copy PROPOSAL to PROPID"""
    if 'PROPID' in orig:
        return {'PROPID': orig.get('PROPID') }
    else:
        if 'PROPOSAL' in orig:
            return {'PROPID': orig.get('PROPOSAL') }
        else:
            return {}

#########################
### OBSTYPE
###

@inkws(['IMAGETYP'])
@outkws(['OBSTYPE'])
def IMAGTYPEtoOBSTYPE(orig, **kwargs):
    """hdr function: IMAGTYPEtoOBSTYPE"""
    return {'OBSTYPE': orig['IMAGETYP']  }

@inkws(['OBSTYP'])
@outkws(['OBSTYPE'])
def OBSTYPtoOBSTYPE(orig, **kwargs):
    """hdr function: OBSTYPtoOBSTYPE"""
    return {'OBSTYPE': orig['OBSTYP']  }

#########################
### OBSID
###

@inkws(['DATE-OBS'])
@outkws(['OBSID'])
def bokOBSID(orig, **kwargs):
    """hdr function: bokOBSID"""
    return {'OBSID': 'bok23m.'+orig['DATE-OBS'] }

#########################
### RA, DEC
###
@inkws(['RASTRNG','DECSTRNG'])
@outkws(['RA','DEC'])
def radecstr(orig, **kwargs):
    """hdr function: radecstr"""
    return {'RA': orig['RASTRNG'],'DEC': orig['DECSTRNG'] }

