import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.set('key01', 'aaaa')
r.setnx('key01', 'bbbb')

v = r.get('key01')
v_str = v.decode()
print(v_str)

r.setnx('key02', 'bbbb')
v = r.get('key02')
v_str = v.decode()
print(v_str)

r.delete('key01')