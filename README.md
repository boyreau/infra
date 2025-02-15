### This project aims to deploy the infrastructure described below with Ansible

```mermaid
architecture-beta
    group safe(database)[safe]
    group internal(server)[internal]
    group external(internet)[external]

        service mysql (database)[mysql] in safe

        service gitea (disk)[gitea] in internal
        service action_runner (server)[action_runner] in internal

        service nginx (internet)[nginx] in external

    gitea:R --> L:mysql
    nginx:R --> L:gitea
    action_runner:B --> T:gitea
```

### My final pipeline should look like this

```mermaid
---
title: My C devops pipeline
---
flowchart LR
    Develop[Vim,  Git]
    Build[Gitea/Github/Gitlab Actions, LLVM Toolchain, GNU Make]
    Test[LLVM Toolchain, GNU Make]
    Deploy[Ansible, Docker]
    Monitor[Prometheus, Grafana]

    Develop --> Build --> Test --> Deploy --> Monitor
```


To use this repo, you need to deploy the ssh servers provided in the directory *containers* (using docker)
You should then put the path to the private key in the inventory.yaml

