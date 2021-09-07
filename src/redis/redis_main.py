import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.set('key01', 'aaaa')

v = r.get('key01')

v_str = v.decode()

r.delete('key01')