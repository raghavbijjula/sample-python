#!/usr/bin/env python

from __future__ import print_function

import base64
import hashlib
import hmac
import json
import struct
#import urllib2


def main():
    #access_key_id, secret_access_key = get_access_creds()
    username, password = get_smtp_creds('97xXS6aLf9WfRvHr', 'CM9CC6bmxZqQjcCgMj2qT75At3')

    print('SMTP Username: %s' % username)
    print('SMTP Password: %s' % password)



def get_smtp_creds(access_key_id, secret_access_key):
    message = 'SendRawEmail'
    version = 0x02

    sig= hmac.new(
        secret_access_key,
        msg=message,
        digestmod=hashlib.sha256)
    sig_bytes = sig.digest()
    sig_and_version_bytes = (struct.pack('B', version) + sig_bytes)
    smtp_password = base64.b64encode(sig_and_version_bytes)

    return access_key_id, smtp_password

if __name__ == '__main__':
    main()
