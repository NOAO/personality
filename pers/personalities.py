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
    ('bok23m-90prime',
     {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                  hf.addTimeToDATEOBS,
                  hf.DTCALDATfromDATEOBStus,
                  hf.bokOBSID],
      'options': {'AAPROPID': '2015A-0801',
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
    ('ct09m-ccd_imager', {'calchdr': [hf.DTCALDATfromDATEOBSchile,
                                      hf.IMAGTYPEtoOBSTYPE],
                          'options': {'AAPROPID': 'smarts',
                                      'DTINSTRU': 'ccd_imager',
                                      'DTSITE': 'ct',
                                      'DTTELESC': 'ct09m',
                                      'PROCTYPE': 'raw',
                                      'PRODTYPE': 'image'},
                          'params': {'OPS_PREAPPLY_UPDATE': 'YES'}}),
    ('ct13m-andicam', {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                                 hf.addTimeToDATEOBS,
                                 hf.DTCALDATfromDATEOBSchile],
                     'options': {'AAPROPID': 'smarts',
                                 'DTINSTRU': 'andicam',
                                 'DTSITE': 'ct',
                                 'DTTELESC': 'ct13m',
                                 'PROCTYPE': 'raw',
                                 'PRODTYPE': 'image'},
                     'params': {}}),
    ('ct15m-chiron', {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                                  hf.DTCALDATfromDATEOBSchile],
                      'options': {'AAPROPID': 'smarts',
                                  'DTINSTRU': 'chiron',
                                  'DTSITE': 'ct',
                                  'DTTELESC': 'ct15m',
                                  'PROCTYPE': 'raw',
                                  'PRODTYPE': 'image'},
                      'params': {}}),
    ('ct15m-echelle', {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                                   hf.DTCALDATfromDATEOBSchile],
                       'options': {'AAPROPID': 'smarts',
                                   'DTINSTRU': 'echelle',
                                   'DTSITE': 'ct',
                                   'DTTELESC': 'ct15m',
                                   'PROCTYPE': 'raw',
                                   'PRODTYPE': 'image'},
                       'params': {}}),
    ('ct4m-arcoiris', {'calchdr': [hf.DTCALDATfromDATEOBSchile],
                       'options': {'DTINSTRU': 'arcoiris',
                                   'DTSITE': 'ct',
                                   'DTTELESC': 'ct4m',
                                   'PROCTYPE': 'raw',
                                   'PRODTYPE': 'image'},
                       'params': {'OPS_PREAPPLY_UPDATE': 'yes',
                                  'jobid_type': 'obsmicro'}}),
    ('ct4m-cosmos', {'calchdr': [hf.DTCALDATfromDATEOBSchile],
                     'options': {'DTINSTRU': 'cosmos',
                                 'DTSITE': 'ct',
                                 'DTTELESC': 'ct4m',
                                 'PROCTYPE': 'raw',
                                 'PRODTYPE': 'image'},
                     'params': {}}),
    ('ct4m-decam', {'calchdr': [hf.DTCALDATfromDATEOBSchile],
                    'options': {'DTINSTRU': 'decam',
                                'DTSITE': 'ct',
                                'DTTELESC': 'ct4m',
                                'PROCTYPE': 'raw'},
                    'params': {}}),
    ('debug', {'calchdr': [],
               'options': {},
               'params': {'jobid_type': 'seconds', 'source': 'dome'}}),
    ('dry-run', {'calchdr': [],
                 'options': {},
                 'params': {'dry_run': 'yes', 'test_resubmit': 1}}),
    ('kp09m-hdi', {'calchdr': [hf.DTCALDATfromDATEOBStus],
                   'options': {'DTINSTRU': 'hdi',
                               'DTSITE': 'kp',
                               'DTTELESC': 'kp09m',
                               'OBSERVAT': 'KPNO',
                               'PROCTYPE': 'raw',
                               'PRODTYPE': 'image'},
                   'params': {'jobid_type': 'obsmicro'}}),
    ('kp4m-kosmos', {'calchdr': [hf.DTCALDATfromDATEOBStus],
                     'options': {'DTINSTRU': 'kosmos',
                                 'DTSITE': 'kp',
                                 'DTTELESC': 'kp4m',
                                 'PROCTYPE': 'raw',
                                 'PRODTYPE': 'image'},
                     'params': {}}),
    ('kp4m-mosaic3', {'calchdr': [hf.DTCALDATfromDATEOBStus],
                      'options': {'DTINSTRU': 'mosaic3',
                                  'DTSITE': 'kp',
                                  'DTTELESC': 'kp4m',
                                  'PROCTYPE': 'raw',
                                  'PRODTYPE': 'image'},
                      'params': {}}),
    ('kp4m-mosaic_1_1', {'calchdr': [hf.DTCALDATfromDATEOBStus],
                         'options': {'AAPROPID': 'noao',
                                     'DTINSTRU': 'mosaic',
                                     'DTSITE': 'kp',
                                     'DTTELESC': 'kp4m',
                                     'PROCTYPE': 'raw',
                                     'PRODTYPE': 'image'},
                         'params': {}}),
    ('kp4m-newfirm', {'calchdr': [hf.DTCALDATfromDATEOBStus],
                     'options': {'DTINSTRU': 'newfirm',
                                 'DTSITE': 'kp',
                                 'DTTELESC': 'kp4m',
                                 'PROCTYPE': 'raw',
                                 'PRODTYPE': 'image'},
                     'params': {}}),
    ('ops-fakearcoiris', {'calchdr': [hf.DTCALDATfromDATEOBSchile],
                          'options': {'PROCTYPE': 'raw', 'PRODTYPE': 'image'},
                          'params': {'OPS_PREAPPLY_UPDATE': 'yes',
                                     'jobid_type': 'obsmicro'}}),
    ('overwrite', {'calchdr': [],
                   'options': {},
                   'params': {'test_resubmit': 1}}),
    ('pipeline', {'calchdr': [],
                  'options': {'DTSUBMIT': 'Q20160126'},
                  'params': {'source': 'pipeline'}}),
    ('pipeline-90prime', {'calchdr': [],
                          'options': None,
                          'params': {'source': 'pipeline'}}),
    ('pipeline-dec', {'calchdr': [],
                      'options': None,
                      'params': {'source': 'pipeline'}}),
    ('pipeline-mosaic3', {'calchdr': [],
                          'options': None,
                          'params': {'source': 'pipeline'}}),
    ('smoke', {'calchdr': [],
               'options': {},
               'params': {'job_tag': 'TADASMOKE', 'test_resubmit': 2}}),
    ('soar-goodman', {'calchdr': [hf.DTCALDATfromDATEOBSchile, hf.INSTRUMEtoDT],
                      'options': {'AAPROPID': 'soar',
                                  'DTINSTRU': 'goodman',
                                  'DTSITE': 'cp',
                                  'DTTELESC': 'soar',
                                  'OBSERVAT': 'SOAR',
                                  'PROCTYPE': 'raw',
                                  'PRODTYPE': 'image'},
                      'params': {}}),
    ('soar-osiris', {'calchdr': [hf.addTimeToDATEOBS,
                                 hf.IMAGTYPEtoOBSTYPE,
                                 hf.DTCALDATfromDATEOBSchile,
                                 hf.INSTRUMEtoDT],
                     'options': {'AAPROPID': 'soar',
                                 'DTINSTRU': 'osiris',
                                 'DTSITE': 'cp',
                                 'DTTELESC': 'soar',
                                 'OBSERVAT': 'SOAR',
                                 'PROCTYPE': 'raw',
                                 'PRODTYPE': 'image'},
                     'params': {}}),
    ('soar-sami', {'calchdr': [hf.addTimeToDATEOBS,
                               hf.DTCALDATfromDATEOBSchile,
                               hf.INSTRUMEtoDT],
                   'options': {'AAPROPID': 'soar',
                               'DTINSTRU': 'sami',
                               'DTSITE': 'cp',
                               'DTTELESC': 'soar',
                               'PROCTYPE': 'raw',
                               'PRODTYPE': 'image'},
                   'params': {}}),
    ('soar-soi', {'calchdr': [hf.addTimeToDATEOBS,
                              hf.DTCALDATfromDATEOBSchile,
                              hf.INSTRUMEtoDT],
                  'options': {'AAPROPID': 'soar',
                              'DTINSTRU': 'soi',
                              'DTSITE': 'cp',
                              'DTTELESC': 'soar',
                              'PROCTYPE': 'raw',
                              'PRODTYPE': 'image'},
                  'params': {}}),
    ('soar-spartan', {'calchdr': [hf.DTCALDATfromDATEOBSchile,
                                  hf.INSTRUMEtoDT,
                                  hf.DETSERNOtoDTSERNO],
                      'options': {'AAPROPID': 'soar',
                                  'DTINSTRU': 'spartan',
                                  'DTSITE': 'cp',
                                  'DTTELESC': 'soar',
                                  'PROCTYPE': 'raw',
                                  'PRODTYPE': 'image'},
                      'params': {}}),
    ('wiyn-bench', {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                                hf.DTCALDATfromDATEOBStus],
                    'options': {'DTINSTRU': 'bench',
                                'DTSITE': 'kp',
                                'DTTELESC': 'wiyn',
                                'PROCTYPE': 'raw',
                                'PRODTYPE': 'image'},
                    'params': {}}),
    ('wiyn-whirc', {'calchdr': [hf.IMAGTYPEtoOBSTYPE,
                                hf.DTCALDATfromDATEOBStus],
                    'options': {'DTINSTRU': 'whirc',
                                'DTSITE': 'kp',
                                'DTTELESC': 'WIYN',
                                'PROCTYPE': 'raw',
                                'PRODTYPE': 'image'},
                    'params': {}})
] # END personalities

