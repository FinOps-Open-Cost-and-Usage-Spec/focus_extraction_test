# Contract Applied

Contract Applied is a set of properties that associate a charge with one or more [*contract commitments*](#glossary:contract-commitment), denoted as key-value pairs in a JSON object.  Contract Applied allows the practitioner to track the progress of the commitments to which they have agreed with a service provider.

The FOCUS-defined properties are:

* `Contract ID`: The unique identifier representing a single contract.
* `Contract Commitment ID`: The unique identifier representing a single contract term.
* `Contract Commitment Applied Cost`: The value of the charge applied to a single contract term.
* `Contract Commitment Applied Quantity`: The usage of the charge applied to a single contract term.
* `Contract Commitment Applied Unit`: The unit of measure for the usage of the charge applied to a single contract term.

In addition to these, a data generator may include one or more custom properties, also denoted as key-value pairs.

## Requirements

### Content Requirements

<b>Contract Commitment Applied Quantity</b>

Contract Commitment Applied Quantity represents the quantity of the charge applied to the contract line item.  Contract Commitment Applied Quantity is associated with the contract line item via Contract Commitment ID.  Contract Commitment Applied Quantity is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a service provider and a customer.

"ContractCommitmentAppliedQuantity" property MUST adhere to the following requirements:

* "ContractCommitmentAppliedQuantity" MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider associates the *charge's* quantity with one or more *contract commitments*.
* "ContractCommitmentAppliedQuantity" MUST be of type Decimal.
* "ContractCommitmentAppliedQuantity" MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* "ContractCommitmentAppliedQuantity" MUST adhere to the following nullability requirements:
  * "ContractCommitmentAppliedQuantity" MUST NOT be null when "ContractCommitmentAppliedCost" is null.
  * "ContractCommitmentAppliedQuantity" MAY be null in all other cases.
* "ContractCommitmentAppliedQuantity" MUST be a valid decimal value.
* "ContractCommitmentAppliedQuantity" MUST be denominated in the "ContractCommitmentAppliedUnit".

<b>Contract Commitment Applied Unit</b>

The Contract Commitment Applied Unit represents a service-provider-specified measurement unit for the usage declared in Contract Commitment Applied Quantity. Contract Commitment Applied Unit complements the Contract Commitment Applied Quantity metric.

The "ContractCommitmentAppliedUnit" property adheres to the following requirements:

* "ContractCommitmentAppliedUnit" MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider associates the *charge's* quantity with one or more *contract commitments*.
* "ContractCommitmentAppliedUnit" MUST be of type String.
* "ContractCommitmentAppliedUnit" MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* "ContractCommitmentAppliedUnit" SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.
* "ContractCommitmentAppliedUnit" nullability is defined as follows:
  * "ContractCommitmentAppliedUnit" MUST be null when "ContractCommitmentAppliedQuantity" is null.
  * "ContractCommitmentAppliedUnit" MUST NOT be null when "ContractCommitmentAppliedQuantity" is not null.

## Overview

### Array of Objects

The parent array is called `Elements` and contains one or more objects which communicate information about how an allocated record was calculated.

| Key | ValueType | Required | Description |
| ----- | ---- | ---------- | ----------- |
| Elements | Array | True | The parent array containing one or more objects which communicate information about how contract commitments were applied to the charge. |

### Object Entries

The `Elements` array contains one or more objects, each of which contains the following entries:

| Key                               | Key Type    | Feature Level | Allows Nulls | Data Type |
| --------------------------------- | ----------- | ------------- | ------------ | --------- |
| ContractID                        | Dimension   | Conditional   | False        | String    |
| ContractCommitmentID              | Dimension   | Conditional   | False        | String    |
| ContractCommitmentAppliedCost     | Dimension   | Conditional   | True         | Numeric   |
| ContractCommitmentAppliedQuantity | Dimension   | Conditional   | True         | Numeric   |
| ContractCommitmentAppliedUnit     | Dimension   | Conditional   | True         | String    |

### Example

```json
{
  "Elements" : [ {
    "ContractID" : "12345",
    "ContractCommitmentID" : "23456",
    "ContractCommitmentAppliedCost" : 500000.00
  }, {
    "ContractID" : "12345",
    "ContractCommitmentID" : "34567",
    "ContractCommitmentAppliedQuantity" : 10000.00,
    "ContractCommitmentAppliedUnit" : "compute_hours"
  } ]
}
```

### JSON Type Definition

```json
{
  "properties": {
    "Elements": {
      "elements": {
        "properties": {
          "ContractID": { "type": "string" },
          "ContractCommitmentID": { "type": "string" }
        },
        "optionalProperties": {
          "ContractCommitmentAppliedCost": { "type": "float64" },
          "ContractCommitmentAppliedQuantity": { "type": "float64" },
          "ContractCommitmentAppliedUnit": { "type": "float64" }
        },
        "additionalProperties": true
      }
    }
  },
  "additionalProperties": true
}
```

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column, but it should not be considered normative because it cannot accurately describe the normative requirements (above) for ContractApplied. Where there are discrepancies, deference will be given to the normative requirements. For example, [NumericFormat](#attributes.numericformat) allows for multiple numeric data types and precisions, but JTD requires both to be specified; other numeric data types and precisions allowable under NumericFormat are considered valid.

## Example Scenarios

### Scenario 1: Initial contract commitment

A single Cost and Usage charge represents the values stated on a contract and its three contract commitments agreed between a service provider and a customer:

1) 12345: Spend $500k overall.  (This is the value of the contract, and thus ContractID = ContractCommitmentID.)
2) 23456: Spend $25k on a particular service.
3) 34567: Consume 100k compute hours on a particular resource type.

The Charge Category is denoted as Purchase, and the Contract ID, Resource ID, and Contract Commitment ID are all denoted as 12345.

```json
{
  "ResourceID": "12345",
  "ChargeCategory": "Purchase",
  "BilledCost": 500000.00,
  "EffectiveCost": 0.00,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractID": "12345",
        "ContractCommitmentID": "12345",
        "ContractCommitmentAppliedCost": 500000.00
      }, {
        "ContractID": "12345",
        "ContractCommitmentID": "23456",
        "ContractCommitmentAppliedCost": 25000.00
      }, {
        "ContractID": "12345",
        "ContractCommitmentID": "34567",
        "ContractCommitmentAppliedQuantity": 100000.00,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
```

### Scenario 2: Contract commitment usage with no custom columns

Assume the contract commitment as described in Scenario 1.  Assume that only 50% of cost and usage gets applied to the contract commitments, per the contract terms.

A single Cost and Usage charge for `myResource1` carries Effective Cost of 30 (denominated in USD) and Consumed Quantity of 1 (denominated in compute hours).  The Charge Category is denoted as Usage.

This applies to the contract commitments in the following manner:

```json
{
  "ResourceID": "myResource1",
  "ChargeCategory": "Usage",
  "BilledCost": 0.00,
  "EffectiveCost": 30.00,
  "ConsumedQuantity": 1,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractID": "12345",
        "ContractCommitmentID": "12345",
        "ContractCommitmentAppliedCost": 15.00
      }, {
        "ContractID": "12345",
        "ContractCommitmentID": "23456",
        "ContractCommitmentAppliedCost": 15.00
      }, {
        "ContractID": "12345",
        "ContractCommitmentID": "34567",
        "ContractCommitmentAppliedQuantity": 0.50,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
```

### Scenario 3: Contract commitment usage with custom columns

The same as Scenario 2, except a custom key-value pair `x_ContractCommitmentCostBalance` is provided by the data generator.   This datapoint represents the value remaining on a given contract commitment.

```json
{
  "ResourceID": "myResource1",
  "ChargeCategory": "Usage",
  "BilledCost": 0.00,
  "EffectiveCost": 30.00,
  "ConsumedQuantity": 1,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractID": "12345",
        "ContractCommitmentID": "12345",
        "ContractCommitmentAppliedCost": 15.00,
        "x_ContractCommitmentCostBalance": 499985.00
      }, {
        "ContractID": "12345",
        "ContractCommitmentID": "23456",
        "ContractCommitmentAppliedCost": 15.00,
        "x_ContractCommitmentCostBalance": 24985.00
      }, {
        "ContractID": "12345",
        "ContractCommitmentID": "34567",
        "ContractCommitmentAppliedQuantity": 0.50,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
```

## Column ID

ContractApplied

## Display Name

Contract Applied

## Description

A set of properties that associate a charge with one or more [*contract commitments*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :----------------------------------------------------|
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension and Metric                                 |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | JSON                                                 |
| Value format    | [JSON Object Format](#attributes.jsonobjectformat)   |

## Introduced (version)

1.3
