# DOCUMENTATION
"""
### To use it, copy these lines of code:

from problemdata.py import *
(V, E, R, C, X, K, endpoint_data, cache_connections, requests) = import_data("kittens.in")


### Explanation of data structures:

endpoint_data[i][ENDP_LATENCY] - latency of video requeset from data center to this endpoint (miliseconds)
endpoint_data[i][ENDP_NUM_OF_CACHES] - the number of cache servers that this endpoint is connected to

cache_connections[CACHE_ID] - the ID of the cache server
cache_connections[CONNECTION_LATENCY] - the latency of serving a video request from this cache server to this endpoint (miliseconds)

requests[VIDEO_ID] - the ID of the requested video
requests[ENDPOINT_ID] -  the ID of the endpoint from which the requests are coming from
requests[NUM_OF_REQUESTS] - the number of requests

"""


# CONSTANTS
ENDP_LATENCY = 0
ENDP_NUM_OF_CACHES = 1

CACHE_ID = 0
CONNECTION_LATENCY = 1

VIDEO_ID = 0
ENDPOINT_ID = 1
NUM_OF_REQUESTS = 2


def import_data(fname):
    f = open("kittens.in" , "r")

    # First line

    (V, E, R, C, X) = [int(p) for p in f.readline().split()]
    K = C*E

    vid_sizes = [int(p) for p in f.readline().split()]

    endpoint_data = []

    for i in range(E):
        endp = [int(p) for p in f.readline().split()]
        endpoint_data.append(endp)

    cache_connections = []

    for i in range(K):
        c = [int(p) for p in f.readline().split()]
        cache_connections.append(c)

    requests = []

    for i in range(R):
        r = [int(p) for p in f.readline().split()]
        requests.append(r)

    data = (V, E, R, C, X, K, endpoint_data, cache_connections, requests)
