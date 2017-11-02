import math

def collision_free(n, r):
  logList = [math.log(i) for i in range(n - r + 1, n+1)]
  logResult = sum(logList) - r * math.log(n)
  result = math.exp(logResult)
  return result

def collision_free_hash_digits(digits, commits):
  # Ideally xstep = 1 for a smooth graph.  Making it
  # larger speeds the computation (fewer x-points).
  xstep = commits / 1024
  n = 2 ** (4 * digits)     # 4 bits in a hex digit
  xs = range(2, commits, xstep)
  ys = [100 - collision_free(n, r) * 100 for r in xs]
  return xs, ys


commits = 250000
xs, y6 = collision_free_hash_digits(6, commits)
xs, y7 = collision_free_hash_digits(7, commits)
xs, y8 = collision_free_hash_digits(8, commits)
xs, y9 = collision_free_hash_digits(9, commits)
xs, y10 = collision_free_hash_digits(10, commits)


from matplotlib import pyplot as plt
#plt.plot(xs, y4, 'g-', label='4 hex digits')
plt.plot(xs, y6, 'b-', label='6 hex digits')
plt.plot(xs, y7, 'm-', label='7 hex digits')
plt.plot(xs, y8, 'r-', label='8 hex digits')
plt.plot(xs, y9, 'm-', label='9 hex digits')
plt.plot(xs, y10, 'c-', label='10 hex digits')

plt.xlabel('Commits')
plt.ylabel('Probability (%)')
plt.grid(True)
plt.title('Collision Probability')
# Depending on how the curves are positioned, this
# can be changed to 'upper left' or 'upper right'.
plt.legend(loc='upper center')
plt.savefig('collisions.png')
