# personality

## Overview
Personalities are a way of allowing NATICA to be general within the
context of new and changing inputs (FITS Files) from telescope
domes. Mainly, it allows details that are required and when a new
Instrument comes online to be encoded outside of the NATICA code
space.  See "Changes OPS May Wish To Make" section below for details
of the encoding.

A "Personality" stores information needed to bring specific raw/dome
FITS files into compliance with NATICA. Generally, each Personality
corresponds to a distinct Instrument on a specific Telescope. Most of
the information in a Personality represents modifications that should
be done to the FITS before ingesting. Some of the info contains
instrument specific parameters to use when modifying or ingesting FITS
files.


## Personality Content
Personalities contain three sections: "options", "calchdr", and "params":
1. OPTIONS are name/value pairs to be added to HDU[0]
2. CALCHDR contain an order list of /hdrfunc/ that should be applied
   to the Dome header to get an Archive header.
3. PARAMS are specialized controls used by ingest.  Mostly not used.


## How a Personality is Applied to a FITS File Header
The application of Personality is different under NATICA than
TADA/LSA.  Here the Personality.make_update_dict() method does extra
bookkeeping to track which HDU contains the first occurance of all
important (those used by any personalities, including their hdrfuncs)
FITS keywords. The method insures that keyword values are updated in
the same HDU in which they are first found.  If the keyword doesn't
exist in any HDU, then HDU-0 is used.

## Changes OPS May Wish To Make
Operations may need to change the FITS Ingest process in response to
new (or changed) FITS header content coming from the Domes.  There are
two files OPS is intended to modify:

1. `hdr_funcs.py`
2. `personalities.py`

Each of these files contains comments describing how they should be
changed. Generally, OPS will only add a section to `personalities.py`
(and maybe to `hdr_funcs.py` as well).  The `personalities.py` file
contains a list of named personalities.   The `hdr_funcs.py` file
contains all the _hdrfuncs_ that are allowed to be used in
personalities. There are decorators before each _hdrfunc_ that specify
which FITS keywords each function reads and which ones it
writes. These are used at run-time to make sure the keyword
prerequisites for each _hdrfunc_ is met by the FITS header it is
operating on.
