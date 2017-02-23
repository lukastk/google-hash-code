from problemdata import ENDP_LATENCY, ENDP_NUM_OF_CACHES, CACHE_ID, CONNECTION_LATENCY, VIDEO_ID, ENDPOINT_ID, NUM_OF_REQUESTS
# implement 
VIDEO_IDS = 0
def score(requests, cache_servers, cache_connections, endpoint_data):
	score = 0
	for request in requests:
		V_ID = request[VIDEO_ID]
		endpoint_ID = request[ENDPOINT_ID]
		num_requests = request[NUM_OF_REQUESTS]
		end_point = endpoint_data[endpoint_ID]
		data_center_latency = end_point[ENDP_LATENCY]
		cache_server_latencies = (connected_cache_server[CONNECTION_LATENCY] for connected_cache_server in cache_connections[endpoint_ID] if V_ID in cache_servers[connected_cache_server[CACHE_ID]][VIDEO_IDS])
		score += (data_center_latency - min(cache_server_latencies)) * num_requests
	score /= len(requests)
	return score