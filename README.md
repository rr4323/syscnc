
# SYSCNC

## Activate the virtual environment for gateway,serv1,serv3
```
python3 -m venv syscnc_env
```
## install required package or install it from requirements.txt
  ```
  pip install --upgrade setuptools
  pip install django channels
  pip install daphne
  pip install websockets
  pip install http2
  pip install twisted[http2,tls]
  ```
## Gateway serv2
```
  cd ~/<git_repo_path>/serv2/wserv
  daphne -p 8001 wserv.asgi:application
```
## server1 serv3
```
  cd ~/<git_repo_path>/serv3/wserv
  daphne -p 8003 wserv.asgi:application
```

## server2 serv1
```
cd ~/<git_repo_path>/serv1/wserv
daphne -p 8000 wserv.asgi:application
```

