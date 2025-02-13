# Playground
A data space playground using FIWARE and ETSI NGSI-LD API

## Execution
Execute the docker compose script to setup FIWARE Orion context broker (used for
storing data space objects) and Mintaka, used for implementing NGSI-LD API temporal
operation,


```
docker compose -f compose/playground.yml  up -d 
```

You can stop the playground by executing 

```
docker compose -f compose/playground.yml  stop
```

## Data space initialization 

Execute the python script `0_Initialize_broker.py`