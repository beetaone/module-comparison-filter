# Filter

|                |                               |
| -------------- | ----------------------------- |
| Name           | Filter                        |
| Version        | v0.0.2                        |
| Dockerhub Link | weevenetwork/weeve-filter     |
| authors        | Jakub Grzelak                 |



- [Filter](#filter)
  - [Description](#description)
  - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
  - [Docker Compose Example](#docker-compose-example)



## Description

This module is responsible for filtering the data based on an algebraic comparisons : <, >, <=, >=, ==, !=

## Features

* Equal to
* Not Equal to
* Less Than
* Greater Than
* Less than or equal to
* Greater than or equal to

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:


| Name          | Environment Variables | type   | Description                                  |
| ------------- | --------------------- | ------ | -------------------------------------------- |
| Input Label   | INPUT_LABEL           | string | The input label on which anomaly is detected |
| Output Label  | OUTPUT_LABEL          | string | The output label as which data is dispatched |
| Output Unit   | OUTPUT_UNIT           | string | The output unit in which data is dispatched  |
| Condition     | CONDITION             | string | Condition for filtering data                 |
| Compare Value | COMPARE_VALUE         | string | The value to compare with                    |

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (INGRESS, PROCESS, EGRESS)  |
| EGRESS_SCHEME         | string | URL Scheme                                     |
| EGRESS_HOST           | string | URL target host                                |
| EGRESS_PORT           | string | URL target port                                |
| EGRESS_PATH           | string | URL target path                                |
| EGRESS_URL            | string | HTTP ReST endpoint for the next module         |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |
| INGRESS_PATH          | string | Path to which data will be received            |


## Dependencies

```txt
Flask==1.1.1
requests
python-dotenv
```

## Input

Input to this module is JSON body single object:

Example of single object:

```node
{
  temperature: 15,
}
```


## Output
Output of this module is JSON body:

```node
{
    "<OUTPUT_LABEL>": <Processed data>,
    "output_unit": <OUTPUT_UNIT>,
    "<MODULE_NAME>Time": timestamp
}
```
 
* Here `OUTPUT_LABEL` and `OUTPUT_UNIT` are specified at the module creation and `Processed data` is data processed by Module Main function.

## Docker Compose Example

```yml
version: "3"
services:
  filter:
    image: weevenetwork/weeve-filter
    environment:
      MODULE_NAME: filter
      MODULE_TYPE: PROCESS
      EGRESS_URL: https://hookb.in/DrrdzwQwXgIdNNEwggLo
      INGRESS_PORT: 80
      INPUT_LABEL: "temperature"
      OUTPUT_LABEL: "temp"
      OUTPUT_UNIT: "Celsius"
      CONDITION: "<="
      COMPARE_VALUE: "15.4"
    ports:
      - 5000:80
```
