# Proof-of-Concept for Oracle Advanced Queuing

## Installation

Pulling an Oracle Database image first:

`> podman pull container-registry.oracle.com/database/enterprise:19.3.0.0`

Starting a container:

`> podman run -d -it --name oracle -p 1521:1521 container-registry.oracle.com/database/enterprise:19.3.0.0`

Starting a shell within the container:

`podman exec -it 49c5cab40014 /bin/bash`
