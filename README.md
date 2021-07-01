# Filter

|                |                               |
| -------------- | ----------------------------- |
| Name           | Filter                        |
| Version        | v0.0.1                        |
| Dockerhub Link | weevenetwork/weeve-filter     |
| authors        | Jakub Grzelak                 |



- [Filter](#filter)
  - [Description](#description)
  - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Output](#output)



## Description

This module is responsible for filtering the data basing on an algebraic condition: <, >, <=, >=, ==, !=

## Features

* Flask ReST client
* Request - sends HTTP Request to the next module

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:


| Name         | Environment Variables | type   | Description                                  |
| ------------ | --------------------- | ------ | -------------------------------------------- |
| Input Label  | INPUT_LABEL           | string | The input label on which anomaly is detected |
| Output Label | OUTPUT_LABEL          | string | The output label as which data is dispatched |
| Output Unit  | OUTPUT_UNIT           | string | The output unit in which data is dispatched  |
| Condition    | CONDITION             | string | Condition for filtering data                 |

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                            |
| --------------------- | ------ | -------------------------------------- |
| EGRESS_API_HOST       | string | HTTP ReST endpoint for the next module |
| MODULE_NAME           | string | Name of the module                     |



## Dependencies

```txt
Flask==1.1.1
requests
python-dotenv
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
