# coding: utf-8

import json
from pycti import OpenCTIApiClient

# Variables
api_url = 'https://demo.opencti.io'
api_token = 'c2d944bb-aea6-4bd6-b3d7-6c10451e2256'

# OpenCTI initialization
opencti_api_client = OpenCTIApiClient(api_url, api_token)

# Get the intrusion set APT28
intrusion_set = opencti_api_client.intrusion_set.read(filters=[{'key': 'name', 'values': ['APT28']}])

# Create the bundle
bundle = opencti_api_client.stix2.export_entity('campaign', '0d31f298-da86-4330-8c0a-4fcfa44f6ae0', 'full')
json_bundle = json.dumps(bundle, indent=4)

# Write the bundle
f = open('APT28_STIX2.json', 'w')
f.write(json_bundle)
f.close()