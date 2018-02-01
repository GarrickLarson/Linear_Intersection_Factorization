import math
import time

# Garrick Larson
# 2018/2/1 0121 hrs
# prime factors were downloaded from http://www.primos.mat.br/
# doesn't seem to work in Python 2. Works in my version of Python 3

f1 = 999999999959
f2 = 999875882263
cp = f1 * f2

print(' Factor 1: ' + str(f1))
print(' Factor 2: ' + str(f2))
print('Composite: ' + str(cp))


# -x intercept method
print()
print('(((Linear Intersection Method)))')
print()
start_time = time.time()
count = 0
d = math.floor(math.sqrt(cp)*2)+1

while True:
    # count += 1  # comment out count to increase speed
    interceptor = math.floor(.5 * (d - math.sqrt(d**2 - 4*cp)))
    if cp % interceptor == 0:
        break
    d += 1

print("Iterations: " + str(count))
t0 = time.time() - start_time
print("--- %s seconds ---" % (t0))
print('Factors: ' + str(interceptor) + ', ' + str(cp/interceptor))



# brute force 
print()
print('(((Brute Force Method)))')
print()
start_time = time.time()
count = 0
b = math.floor(math.sqrt(cp))

while cp % b != 0:
    b -= 1
    # count += 1  # comment out count to increase speed
t1 = time.time() - start_time
print(b)
print("Iterations: " + str(count))
print("--- %s seconds ---" % (t1))
print('Factors: ' + str(b) + ', ' + str(cp/b))
print()
print('Ratio: ' + str(t1/t0) + ' times faster than brute force')
