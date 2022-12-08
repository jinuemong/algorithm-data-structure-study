#출처 : https://www.acmicpc.net/problem/10930

import hashlib
data = input()
encoded_data = data.encode()
print(hashlib.sha256(encoded_data).hexdigest())