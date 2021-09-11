# Quick test of using FastAPI
- Writes to SqliteDB


Run using
$ uvicorn main:api --reload

on Ec2 run it using, so that it binds correctly:
$ uvicorn main:api --host 0.0.0.0


"if some process listens on 0.0.0.0, it will be reachable at IP adresses of all the machine’s network interfaces which include the currently configured address of the loop back interface. But if the process listens only on a port <portNumber> of a loopback address, e.g. 127.0.0.1, and then the process is only reachable from the same machine by targeting exactly 127.0.0.1:<portNumber>”

