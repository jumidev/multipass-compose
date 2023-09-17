# TL; DR:

Multipass-compose maps the multipass cli options to a yml file:

The equivalent multipass command:
```
multipass launch --memory 2G --disk 20G --name wassup-dawg
```

Becomes

```
instances:
    wassup-dawg:
        image: lts
        memory: 2G
        disk: 20G

```

Which is launched with

`multipass-compose up`

# Idempotence

`docker-compose up` is an idempotent command, meaning that, whether you run it once or five times, the result is a predictable number of containers running.  This feature prevents unintended side effects and ensures that pre existing conditions do not get in the way of launching the container.

`multipass launch` is **not** idempotent, the number of running instances will match the number of times the command was launched. If the user attempts to run an instance with the same name as another instance, the command will error out.  It is therefore the user's responsability to check pre existing conditions when running this command.

`multipass-compose` implements a philosophy similar to `docker-compose`.  When `multipass-compose up` is run, it checks in the background of the vm is already running and updates it as required, thus ensuring idempotence.


# Reference

|   item        |      cli equivalent      |  description |
|---------------|:------------------------:|:--------------------------------------|
| `image:`      | image                    | image to launch. If omitted, then the default Ubuntu LTS will be used. |
| `name:`       | -n, --name               | optional name of the instance |
| `cpus:`       | -c, --cpus               | Number of CPUs to allocate. Minimum: 1, default: 1. |
| `disk:`       | -d, --disk               | Disk space to allocate. Positive integers, in bytes, or with K, M, G suffix. |
| `memory:`     | -m, --memory             | Amount of memory to allocate. Positive integers, in bytes, or decimals, with K, M, G suffix.  Minimum: 128M, default: 1G. |
| `timeout:`    | --timeout                | Maximum time, in seconds, to wait for the instance to finish launching  |
| `cloud-init:` | --cloud-init             | Path or URL to a user-data cloud-init configuration, or '-' for stdin |
| `mounts:`     | --mount                  | Mount one or more a local directories inside the instance. |
| `networks:`   | --network                | Add one or more network interfaces to the instance |
