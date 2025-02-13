import os

#SERVICE_DID = os.environ.get('SERVICE_DID', None)
#HOSTNAME = os.environ.get('HOSTNAME', None)
HOSTNAME = 'nativesky.preeya.rocks'

if HOSTNAME is None:
    raise RuntimeError('You should set "HOSTNAME" environment variable first.')

#if SERVICE_DID is None:
SERVICE_DID = f'did:web:{HOSTNAME}'


#WHATS_ALF_URI = os.environ.get('WHATS_ALF_URI')
WHATS_ALF_URI = 'at://did:plc:amuxij7yxqdhv4w5arycjvrs/app.bsky.feed.generator/nativesky'
if WHATS_ALF_URI is None:
    raise RuntimeError('Publish your feed first (run publish_feed.py) to obtain Feed URI. '
                       'Set this URI to "WHATS_ALF_URI" environment variable.')
