import os
import sys
sys.path.insert(0, "/home/lukas/docs/dev/google/google-hash-code")


from problemdata import *

def calc_scores(fname):

    (V, E, R, C, X, K, vid_sizes, endpoint_data, cache_connections, requests) = import_data(fname)

    # Calculate video to caches

    video_to_caches = []

    for v in range(V):
        video_to_caches.append(set())

    for r in requests:
        caches = [p[CACHE_ID] for p in cache_connections[r[ENDPOINT_ID]]]

        for c in caches:
            video_to_caches[r[VIDEO_ID]].add(c)

    # Find the largest video size
    max_vid_size = max(vid_sizes)

    def scoringtype(cache_id, video_id):
        pass

    def size_defect(cache_id, video_id):
        return -float(vid_sizes[video_id])/max_vid_size

    def num_of_endpoints(cache_id, video_id):
        pass

    def num_of_video_requests():
        pass

    def is_connected(cache_id, video_id):
        if not cache_id in video_to_caches[video_id]:
            return -100
        else:
            return 0

    scoretypes = [(size_defect, 1), (is_connected, 1)] # (function, weight)

    cache_vids = []

    for c in range(C):
        vid_scores = []

        for v in range(V):

            score = 0

            for scoring_function, weight in scoretypes:
                score += scoring_function(c, v)*weight

            vid_scores.append((score, v))

        vid_scores.sort()
        vid_scores.reverse()

        mem = 0
        i = 0
        size = 0
        vidlist = []
        while mem <= X:
            size =  vid_sizes[vid_scores[i][1]]
            mem += size
            vidlist.append(vid_scores[i][1])

            i += 1

        if mem > X:
            mem -= size
            vidlist.pop()

        cache_vids.append(vidlist)

    f = open(fname + "_scores", "w")

    f.write(str(len(cache_vids)))
    f.write("\n")
    for c in cache_vids:
        f.write(" ".join(map(str, c)))
        f.write("\n")

calc_scores("kittens.in")
calc_scores("me_at_the_zoo.in")
calc_scores("trending_today.in")
calc_scores("videos_worth_spreading.in")
