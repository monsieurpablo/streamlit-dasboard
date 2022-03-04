# %%
# import libraries
import os
import pandas as pd
import numpy as np

from specklepy.api import operations
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account
from specklepy.transports.server import ServerTransport

from typing import Any, List

# %%
TOKEN_ID = os.environ.get('SPECKLE_TOKEN')
HOST = "https://speckle.xyz"
# STREAM_ID = "0b7b9e7705"

def get_authenticated_client() -> SpeckleClient:
    """
    This assumes you already have a local account. If you don't already have one, you'll need
    to download the Speckle Manager and add an account for your server (which can be localhost).
    See the docs for more info: https://speckle.guide/user/manager.html
    """
    client = SpeckleClient(host=HOST)
    client.authenticate(token=TOKEN_ID)
    
    # account = get_default_account()
    # client.authenticate(token=TOKEN_ID)

    return client

def get_branches(client: SpeckleClient, stream_id: str) -> Any:
    # get the specified commit data
    stream = client.stream.get(stream_id)
    # create an authenticated server transport from the client and receive the commit obj
    transport = ServerTransport(stream_id, client)
    # get all the branches
    branches = client.branch.list(stream_id=stream_id, branches_limit= 100)
    
    return branches

# def receive_data(client: SpeckleClient, stream_id: str = STREAM_ID, commit_id: str = COMMIT_ID) -> Any:
#     transport = ServerTransport(client, stream_id)

#     commit = client.commit.get(stream_id, commit_id)
#     data = operations.receive(commit.referencedObject, transport)

#     return data["data"]

def speckle_df(branches) -> pd.DataFrame:
    a = [(b.name, b.id) for b in branches]
    
    # create pandas dataframe
    df = pd.DataFrame(a, columns=['branch', 'id'])
    df = df.join(df.branch.str.split('/', expand=True))
    df = df.rename(columns={0:'revision', 1:'topic',2:'metric'}, inplace=False)
    
    # remove main branch
    df = df[df['revision'] != 'main']
    
    return df

# %%
def get_speckle_df(stream_id: str) -> pd.DataFrame:

    # create and authenticate a client
    client = get_authenticated_client()
    branches = get_branches(client = client, stream_id= stream_id )
    df_branches = speckle_df(branches)
    
    return df_branches
    # df_data # TODO 