"""\
This file is intended for modification by OPS.  It contains the
full Personality Library.

Each personality is a pair containing PersonalityName and Content.
The Content is key/value dictionary containing the three keys: 
calchdr, options, params.  
 calchdr :: list of hdrfuncs (each must be in personality.hdr_funcs)
 options :: key/value dictionary; keys are FITS keywords
 params  :: parameters to use when ingesting using the Personality

Some of the old params may have become obsolete in NATICA but the are
still retained in this library. (for historical reasons only)

"""

import pers.hdr_funcs as hf
#!import hdr_funcs as hf


# from: sandbox/tada-cli/personalities/*/*.yaml
# All DTTELESC, DTINSTRU should be lowercase

# [(persName, dict(calchdr=[hdrfunc,...], options=dict(), params=dict())), ...]
personalities = [
    ('legacysurvey',
     {'options': {'DTINSTRU': 'whirc',
                  'DTTELESC': 'wiyn',
                  'DTSITE': 'kp',
                  'PROCTYPE': 'raw',
                  'DTACQNAM': 'NONE',
                  'DATE-OBS': '1900-01-31',
                  'DTCALDAT': '1900-01-31',
                  },
      'params': {}}),
    ('bok23m-90prime',                                  # PersName, Test?=yes
     {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                  hf.addTimeToDATEOBS,
                  hf.DTCALDATfromDATEOBStus,
                  hf.bokOBSID],
      'options': {'DTPROPID': '2015A-0801',
                  'DTCOPYRI': 'University of Arizona',
                  'DTINSTRU': '90prime',
                  'DTOBSERV': 'University of Arizona '
                  'Observatories',
                  'DTPI': 'Xiaohui Fan,',
                  'DTPIAFFL': 'University  of Arizona',
                  'DTPROPID': '2015A-0801',
                  'DTSITE': 'kp',
                  'DTTELESC': 'bok23m',
                  'DTTITLE': 'Beijing-Arizona Sky Survey (BASS)',
                  'OBSERVAT': 'Steward',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'Image'},
      'params': {}}),
    ('ct09m-ccd_imager',                                # PersName, Test?=no
     {'calchdr': [hf.DTCALDATfromDATEOBSchile,
                                      hf.IMAGTYPEtoOBSTYPE],
                          'options': {'DTPROPID': 'smarts',
                                      'DTINSTRU': 'ccd_imager',
                                      'DTSITE': 'ct',
                                      'DTTELESC': 'ct09m',
                                      'PROCTYPE': 'raw',
                                      'PRODTYPE': 'image'},
                          'params': {'OPS_PREAPPLY_UPDATE': 'YES'}}),
    ('ct13m-andicam',                                   # PersName, Test?=yes
     {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                                 hf.addTimeToDATEOBS,
                                 hf.DTCALDATfromDATEOBSchile],
                     'options': {'DTPROPID': 'smarts',
                                 'DTINSTRU': 'andicam',
                                 'DTSITE': 'ct',
                                 'DTTELESC': 'ct13m',
                                 'PROCTYPE': 'raw',
                                 'PRODTYPE': 'image'},
                     'params': {}}),
    ('ct15m-chiron',                                    # PersName, Test?=no
     {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                  hf.DTCALDATfromDATEOBSchile],
      'options': {'DTPROPID': 'smarts',
                  'DTINSTRU': 'chiron',
                  'DTSITE': 'ct',
                  'DTTELESC': 'ct15m',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('ct15m-echelle',                                   # PersName, Test?=yes
     {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                  hf.DTCALDATfromDATEOBSchile],
      'options': {'DTPROPID': 'smarts',
                  'DTINSTRU': 'echelle',
                  'DTSITE': 'ct',
                  'DTTELESC': 'ct15m',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('ct4m-arcoiris',                                   # PersName, Test?=yes
     {'calchdr': [hf.DTCALDATfromDATEOBSchile],
      'options': {'DTINSTRU': 'arcoiris',
                  'DTSITE': 'ct',
                  'DTTELESC': 'ct4m',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {'OPS_PREAPPLY_UPDATE': 'yes',
                 'jobid_type': 'obsmicro'}}),

    ('ct4m-cosmos',                                     # PersName, Test?=yes
     {'calchdr': [hf.DTCALDATfromDATEOBSchile],
      'options': {'DTINSTRU': 'cosmos',
                  'DTSITE': 'ct',
                  'DTTELESC': 'ct4m',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),
    
    ('ct4m-decam',                                      # PersName, Test?=no
     {'calchdr': [hf.DTCALDATfromDATEOBSchile, hf.PROPIDtoDT],
      'options': {'DTINSTRU': 'decam',
                  'DTSITE': 'ct',
                  'DTTELESC': 'ct4m',
                  'PROCTYPE': 'raw'},
      'params': {}}),
    
#!    ('debug',                                           
#!     {'calchdr': [], 'options': {},
#!      'params': {'jobid_type': 'seconds', 'source': 'dome'}}),
#!
#!    ('dry-run',                                         
#!     {'calchdr': [],  'options': {},
#!      'params': {'dry_run': 'yes', 'test_resubmit': 1}}),

    ('kp09m-hdi',                                       # PersName, Test?=no
     {'calchdr': [hf.addTToDATEOBS, hf.DTCALDATfromDATEOBStus, hf.radecstr],
      'options': {'DTINSTRU': 'hdi',
                  'DTSITE': 'kp',
                  'DTTELESC': 'kp09m',
                  'OBSERVAT': 'KPNO',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {'jobid_type': 'obsmicro'}}),

    ('kp4m-kosmos',                                     # PersName, Test?=yes
     {'calchdr': [hf.DTCALDATfromDATEOBStus],
      'options': {'DTINSTRU': 'kosmos',
                  'DTSITE': 'kp',
                  'DTTELESC': 'kp4m',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('kp4m-mosaic3',                                    # PersName, Test?=yes
     {'calchdr': [hf.DTCALDATfromDATEOBStus],
      'options': {'DTINSTRU': 'mosaic3',
                  'DTSITE': 'kp',
                  'DTTELESC': 'kp4m',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('kp4m-mosaic_1_1',                                 # PersName, Test?=no
     {'calchdr': [hf.DTCALDATfromDATEOBStus],
      'options': {'DTPROPID': 'noao',
                  'DTINSTRU': 'mosaic',
                  'DTSITE': 'kp',
                  'DTTELESC': 'kp4m',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('kp4m-newfirm',                                    # PersName, Test?=yes
     {'calchdr': [hf.DTCALDATfromDATEOBStus],
      'options': {'DTINSTRU': 'newfirm',
                  'DTSITE': 'kp',
                  'DTTELESC': 'kp4m',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('ct4m-newfirm',                                    # PersName, Test?=no
     {'calchdr': [hf.addTimeToDATEOBS, 
                 hf.DTCALDATfromDATEOBSchile,
                 hf.PROPIDtoDT],
      'options': {'DTINSTRU': 'newfirm',
                  'DTSITE': 'ct',
                  'DTTELESC': 'ct4m',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

     ('soar-ghts_red',                                    # PersName, Test?=no
     {'calchdr': [hf.DTCALDATfromDATEOBSchile],
      'options': {'DTINSTRU': 'ghts_red',
                  'DTSITE': 'cp',
                  'DTTELESC': 'soar',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

     ('soar-ghts_red_imager',                             # PersName, Test?=no
     {'calchdr': [hf.DTCALDATfromDATEOBSchile],
      'options': {'DTINSTRU': 'ghts_red_imager',
                  'DTSITE': 'cp',
                  'DTTELESC': 'soar',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

     ('soar-ghts_blue',                                    # PersName, Test?=no
     {'calchdr': [hf.DTCALDATfromDATEOBSchile],
      'options': {'DTINSTRU': 'ghts_blue',
                  'DTSITE': 'cp',
                  'DTTELESC': 'soar',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),


#!    ('ops-fakearcoiris',                                
#!     {'calchdr': [hf.DTCALDATfromDATEOBSchile],
#!      'options': {'PROCTYPE': 'raw', 'PRODTYPE': 'image'},
#!      'params': {'OPS_PREAPPLY_UPDATE': 'yes',
#!                 'jobid_type': 'obsmicro'}}),
#!
#!    ('overwrite',                                       
#!     {'calchdr': [],
#!      'options': {},
#!      'params': {'test_resubmit': 1}}),
#!
#!    ('pipeline',                                        
#!     {'calchdr': [],
#!      'options': {'DTSUBMIT': 'Q20160126'},
#!      'params': {'source': 'pipeline'}}),

    ('pipeline-90prime',                                
     {'calchdr': [],
      'options': {},
      'params': {'source': 'pipeline'}}),

    ('pipeline-decam',                                    
     {'calchdr': [],
      'options': {},
      'params': {'source': 'pipeline'}}),

    ('pipeline-mosaic3',                                
     {'calchdr': [],
      'options': {},
      'params': {'source': 'pipeline'}}),

    ('pipeline-newfirm',
     {'calchdr': [],
      'options': {},
      'params': {'source': 'pipeline'}}),

#!    ('smoke',                                           
#!     {'calchdr': [], 'options': {},
#!      'params': {'job_tag': 'TADASMOKE', 'test_resubmit': 2}}),

# SOAR Goodman fills proposal info into PROPOSAL keyword instead of PROPID
    ('soar-goodman',                                    # PersName, Test?=yes
     {'calchdr': [hf.DTCALDATfromDATEOBSchile,
                  hf.PROPOSALtoPROPID,
                  hf.INSTRUMEtoDT],
      'options': {'DTINSTRU': 'goodman',
                  'DTSITE': 'cp',
                  'DTTELESC': 'soar',
                  'OBSERVAT': 'SOAR',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('soar-osiris',                                     # PersName, Test?=yes
     {'calchdr': [hf.addTimeToDATEOBS,
                  hf.IMAGTYPEtoOBSTYPE,
                  hf.DTCALDATfromDATEOBSchile,
                  hf.INSTRUMEtoDT],
      'options': {'DTINSTRU': 'osiris',
                  'DTSITE': 'cp',
                  'DTTELESC': 'soar',
                  'OBSERVAT': 'SOAR',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('soar-sami',                                       # PersName, Test?=yes
     {'calchdr': [hf.addTimeToDATEOBS,
                  hf.DTCALDATfromDATEOBSchile,
                  hf.INSTRUMEtoDT],
      'options': {'DTINSTRU': 'sami',
                  'DTSITE': 'cp',
                  'DTTELESC': 'soar',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('soar-soi',                                        # PersName, Test?=yes
     {'calchdr': [hf.addTimeToDATEOBS,
                  hf.DTCALDATfromDATEOBSchile,
                  hf.INSTRUMEtoDT],
      'options': {'DTINSTRU': 'soi',
                  'DTSITE': 'cp',
                  'DTTELESC': 'soar',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),
# SOAR Spartan doesn't seem to use PROPID so hardwire it
    ('soar-spartan',                                    # PersName, Test?=yes
     {'calchdr': [hf.DTCALDATfromDATEOBSchile,
                  hf.INSTRUMEtoDT,
                  hf.DETSERNOtoDTSERNO],
      'options': {'DTINSTRU': 'spartan',
                  'DTSITE': 'cp',
                  'DTTELESC': 'soar',
                  'DTPROPID': 'soar',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('soar-triplespec',                                   # PersName, Test?=yes
     {'calchdr': [hf.DTCALDATfromDATEOBSchile],
      'options': {'DTINSTRU': 'triplespec',
                  'DTSITE': 'cp',
                  'DTTELESC': 'soar',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {'OPS_PREAPPLY_UPDATE': 'yes',
                 'jobid_type': 'obsmicro'}}),


    ('wiyn-bench',                                      # PersName, Test?=yes
     {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                  hf.DTCALDATfromDATEOBStus],
      'options': {'DTINSTRU': 'bench',
                  'DTSITE': 'kp',
                  'DTTELESC': 'wiyn',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}}),

    ('wiyn-whirc',                                      # PersName, Test?=yes
     {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                  hf.DTCALDATfromDATEOBStus],
      'options': {'DTINSTRU': 'whirc',
                  'DTSITE': 'kp',
                  'DTTELESC': 'WIYN',
                  'PROCTYPE': 'raw',
                  'PRODTYPE': 'image'},
      'params': {}})
] # END personalities

