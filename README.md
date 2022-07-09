# Comparison Filter

|              |                                                                  |
| ------------ | ---------------------------------------------------------------- |
| name         | Comparison Filter                                                |
| version      | v1.0.0                                                           |
| GitHub       | [comparison-filter](https://github.com/weeve-modules/comparison-filter) |
| DockerHub    | [weevenetwork/comparison-filter](https://hub.docker.com/r/weevenetwork/comparison-filter)     |
| authors      | Jakub Grzelak, Paul Gaiduk                                       |

***
## Table of Content

- [Comparison Filter](#comparison-filter)
  - [Table of Content](#table-of-content)
  - [Description](#description)
  - [Module Variables](#module-variables)
  - [Module Testing](#module-testing)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
***

## Description

This module is responsible for filtering the data based on an algebraic comparisons : <, >, <=, >=, ==, !=.

## Module Variables

The following module configurations can be provided in a data service designer section on weeve platform:

| Environment Variables | type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| INPUT_LABEL           | string | The input label on which anomaly is detected |
| CONDITION             | string | Condition for filtering data                 |
| COMPARE_VALUE         | string | The value to compare with                    |
| MODULE_NAME           | string | Name of the module                                |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)    |
| LOG_LEVEL             | string | Allowed log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Refer to `logging` package documentation. |
| INGRESS_HOST          | string | Host to which data will be received               |
| INGRESS_PORT          | string | Port to which data will be received               |
| EGRESS_URLS           | string | HTTP ReST endpoint for the next module            |

## Module Testing

To test module navigate to `test` directory. In `test/assets` edit both .json file to provide input for the module and expected output. During a test, data received from the listeners are compared against expected output data. You can run tests with `make run_test`.

## Dependencies

The following are module dependencies:

* bottle
* requests

The following are developer dependencies:

* pytest
* flake8
* black

## Input

Input to this module is JSON body single object:

Example of single object:

```json
{
  temperature: 15
}
```


## Output
Output of this module is JSON body the same as input data if chosen comparison condition is satisfied:

```json
{
  temperature: 15
}
```
