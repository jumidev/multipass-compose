# multipass-compose
Deploy multipass vms using the same philosophy and ease as docker-compose

# setup
- install [multipass](https://multipass.run/)
  - if on linux, you might want to use lxd as the backend for better networking: \
    `snap install lxd` then `multipass set local.driver=lxd`
- python3 and pip, then
- `pip install multipass-compose`

