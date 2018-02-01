import math
import time

# Garrick Larson
# 2018/2/1 0121 hrs

f1 = 999999999959
f2 = 999939472397

cp = f1 * f2
print(f1)
print(f2)
print(cp)


# -x intercept method
start_time = time.time()
count = 0
d = math.floor(math.sqrt(cp)*2)+1

while True:
    count += 1
    # loop_time = time.time()
    interceptor = math.floor(.5 * (d - math.sqrt(d**2 - 4*cp)))
    if cp % interceptor == 0:
        break
    d += 1
    # print(loop_time-time.time())

print("Iterations: " + str(count))
t0 = time.time() - start_time
print("--- %s seconds ---" % (t0))
print(interceptor)
print(cp/interceptor)



# brute force 
b = math.floor(math.sqrt(cp))
start_time = time.time()
while cp % b != 0:
    b -= 1
t1 = time.time() - start_time
print(b)
print("--- %s seconds ---" % (t1))

print('Ratio: ' + str(t1/t0))
