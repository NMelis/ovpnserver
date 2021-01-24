# Auto creater OpenVpn server in Digital Ocean

This script auto creaded openvpn server in our Digital Ocean and download opvn client file

## install
```
pip install openvpn-server-do
```
or download the project via git clone and run the following:
```
pip install -r requirements.txt
```

## usages
```shell
$ ovpnserver --help
OpenVPN creator

optional arguments:
  -h, --help            show this help message and exit
  --token TOKEN [TOKEN ...]
                        token from Digital Ocean with permission create droplet
  --tag TAG [TAG ...]   Droplet tags
  --local-path LOCAL_PATH [LOCAL_PATH ...]
                        local path where file will save: /home/username/Documents/

$ ovpnserver --token <YOUR TOKEN>
```
Or You can save your token in home directory to file .do_token and start script without argument --token