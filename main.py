import streamlit as st
import pandas as pd
import numpy as np

import streamlit.components.v1 as components


from specklepy.api import operations
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account
from specklepy.transports.server import ServerTransport


HOST = "https://speckle.xyz"
STREAM_ID = "c7ecab3889"
COMMIT_ID = "bad53d2d24"  # commit containing objects with materials already added


# create and authenticate a client
client = SpeckleClient(host=HOST)
account = get_default_account()
client.authenticate(token=account.token)

# get the specified commit data
commit = client.commit.get(STREAM_ID, COMMIT_ID)

# create an authenticated server transport from the client and receive the commit obj
transport = ServerTransport(STREAM_ID, client)
res = operations.receive(commit.referencedObject, transport)

# get the list of levels from the received object
# levels = res["data"]

base = res["@data"][0][0][0][0][0]
base

df_values = base["@DF_values"]

df = pd.DataFrame(df_values, columns=['df_values'])

print(df.head())

