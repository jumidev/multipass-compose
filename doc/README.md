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

`multipass launch` is not idempotent, the number of running instances will match the number of times the command was launched. If the user attempts to run an instance with the same name as another instance, the command will error out.  It is the user's responsability to check pre existing conditions in advance

`multipass-compose` implements a philosophy similar to `docker-compose`.  When `multipass-compose up` is run, it checks in the background of the vm is already running and updates it as required, thus ensuring idempotence


