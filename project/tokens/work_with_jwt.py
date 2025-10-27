from encodings.utf_16 import decode

import jwt
import datetime
from time import sleep

JWT_SECRET = 'MyJWTSecret'

#payload_1000s = {
 #   'user_name': "Саша",
 #   "age": 14,
  #  "city": "Одеса",
   # "iat": datetime.datetime.now(datetime.timezone.utc),
 #   "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=1000)
#}

#encode_jwt_1000s = jwt.encode(payload=payload_1000s, key=JWT_SECRET, algorithm='HS256')
#print(encode_jwt_1000s)

#decode_1000s = jwt.decode(
 #   jwt=encode_jwt_1000s,
  #  key=JWT_SECRET,
  #  algorithms=['HS256']
#)
#print(decode_1000s)


# = {
  #  "iat": datetime.datetime.now(datetime.timezone.utc),
  #  "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=10),
  #  'user_name': "Саша"
#}

#encode_jwt_expired = jwt.encode(payload=payload_expired, key=JWT_SECRET, algorithm='HS256')
#(encode_jwt_expired)
#sleep(15)

#decode_expired = jwt.decode(
   # jwt=encode_jwt_expired,
 #   key=JWT_SECRET,
  #  algorithms=['HS256']
#)

payload_wrong_key = {
    "iat": datetime.datetime.now(datetime.timezone.utc),
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=500),
    "user_name": "Саша"
}

encode_jwt_wrong_key = jwt.encode(payload=payload_wrong_key, key=JWT_SECRET, algorithm='HS256')

WRONG_SECRET = 'MyWrongJWTSecret'

decode_wrong_key = jwt.decode(
    jwt=encode_jwt_wrong_key,
    key=WRONG_SECRET,
    algorithms=['HS256']
)
