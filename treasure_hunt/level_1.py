# 1) pick (6,6)(p1), and get distance (d1)
# 2a) If distance is even, pick one of (x+D/2, y+D/2), (x+D/2, y-D/2), (x-D/2, y+D/2), (x-D/2, y-D/2), where x = 6 and y = 6
# 2b) If distance is odd, let x = ceiling(D/2), y = floor(D/2), and pick one of (x+D/2, y+D/2), (x+D/2, y-D/2), (x-D/2, y+D/2), (x-D/2, y-D/2), where x = 6 and y = 6
# At this point, we will either find the treasure or we will get a second distance (d2) to guide us to where the treasure is
# 3a) If d2 is even, follow 2a), only now x and y is the point selected at 2a), (p2)
# 3b) If d2 is odd, follow 2a), only now x and y is the point selected at 2b), (p2)
# 4) Calculate a point that satisfies both p2 + d2 and p1 + d1
# 5) If we still dont have our answer, repeat from step 2