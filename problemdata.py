#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DOCUMENTATION
"""
### To use it, copy these lines of code:

from problemdata import *
(V, E, R, C, X, K, endpoint_data, cache_connections, requests) = import_data("kittens.in")

### Explanation of data structures:

vid_sizes[i] - Size of video i

endpoint_data[i][ENDP_NUM_OF_CACHES] - the number of cache servers that this endpoint is connected to
endpoint_data[i][DATA_CONNECTION_LATENCY] - latency of video requeset from data center to this endpoint (miliseconds)

cache_connections[i] - List of connections from endpoint i
cache_connections[i][j] - The jth connection form endpoint i
cache_connections[i][j][CACHE_ID] - The cache that endpoint i is connected to
cache_connections[i][j][CONNECTION_LATENCY] - The latency of the connection.

requests[i][VIDEO_ID] - the ID of the requested video
requests[i][ENDPOINT_ID] -  the ID of the endpoint from which the requests are coming from
requests[i][NUM_OF_REQUESTS] - the number of requests

"""

# CONSTANTS
ENDP_NUM_OF_CACHES = 1
DATA_CONNECTION_LATENCY = 0

CACHE_ID = 0
CONNECTION_LATENCY = 1

VIDEO_ID = 0
ENDPOINT_ID = 1
NUM_OF_REQUESTS = 2


def import_data(fname):
    f = open(fname , "r")

    # First line

    (V, E, R, C, X) = [int(p) for p in f.readline().split()]

    vid_sizes = tuple([int(p) for p in f.readline().split()])

    endpoint_data = []
    cache_connections = []

    for i in range(E):
        endp = tuple([int(p) for p in f.readline().split()])
        endpoint_data.append(endp)

        K = endp[ENDP_NUM_OF_CACHES]
        conn = []

        for j in range(K):
            c = tuple([int(p) for p in f.readline().split()])
            conn.append(c)

        cache_connections.append(conn)

    requests = []

    for i in range(R):
        r = [int(p) for p in f.readline().split()]
        requests.append(r)

    return (V, E, R, C, X, K, endpoint_data, cache_connections, requests)
