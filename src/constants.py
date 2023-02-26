from cachetools import TTLCache

# Config
__version__ = "0.1.0"

# Rate Limit Ip/N_Request/Time
ip_cache = TTLCache(maxsize=1000, ttl=60)
TIME = 1000000

# Max Number Files
MAX = 99

