# Proof-of-Concept for Oracle Advanced Queuing

## Installation

**Prerequisites**

Installing Oracle Thick Client 19.8 libraries under _lib_ (download from https://www.oracle.com/database/technologies/instant-client/downloads.html).

**MacOs specifics**
```shell
podman machine stop || true
podman machine rm || true
podman machine init --cpus=2 --memory=4096 -v $HOME:$HOME -v /private/tmp:/private/tmp -v /var/folders/:/var/folders/
sed -i '' 's/security_model=mapped-xattr/security_model=none/' $(podman machine inspect | jq --raw-output '.[0].ConfigPath.Path')
podman machine start
```

**Pulling an Oracle Database image**

`> podman pull container-registry.oracle.com/database/enterprise:19.3.0.0`

Starting a container:
```shell
podman run -d -it --name oracle -p 1521:1521 --env 'ORACLE_SID=ORCLCDB' container-registry.oracle.com/database/enterprise:19.3.0.0
podman cp ./config oracle:/home/oracle
```

Database setup (**needs the container to be fully up after executing previous command, may take a while**):
```shell
podman exec -it oracle sqlplus / as sysdba @config/setup-oracle.sql

```

Setting up the Oracle AQ queues:

```shell
podman exec -it oracle sqlplus scott/tiger @config/create-queues.sql
```

Stopping and cleaning:
```shell
podman rm -f oracle
```
