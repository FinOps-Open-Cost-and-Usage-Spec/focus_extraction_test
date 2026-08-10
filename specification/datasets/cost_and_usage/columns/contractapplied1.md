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

### Column Requirements

The ContractApplied column MUST adhere to the following requirements:

* ContractApplied MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* ContractApplied MUST NOT be null when one or more *contract commitments* are applied to the *charge*.

### Object Schema Requirements

Contract Applied consists of a valid JSON object which contains an array of key-value objects describing the one or more contract commitments applied to the charge. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the contract application.

* If ContractApplied is not null, ContractApplied MUST adhere to the following requirements:
  * ContractApplied MUST have a top-level key "Elements" which contains an array.
  * ContractApplied root object MAY contain custom objects, in addition to "Elements".
  * Each item in "Elements" MUST be an object.
  * "Elements" objects MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
  * "Elements" objects MUST contain key-value pairs (contract application properties).
  * Contract application property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
  * "Elements" objects MUST contain four key-value pairs, representing "ContractCommitmentID", "ContractCommitmentAppliedCost", "ContractCommitmentAppliedQuantity", and "ContractCommitmentAppliedUnit".
  * "Elements" objects MAY contain custom key-value pairs, representing additional datapoints provided by the data generator.
  * When custom key-value pairs within "Elements" objects are present:
    * Contract application property custom key-value pairs MUST be prefixed with a consistent `x_` prefix to identify them as external, custom columns and distinguish them from FOCUS columns to avoid conflicts in future releases.
    * Contract application property custom key-value pairs MUST be documented by the data generator.
    * Contract application property custom key-value pairs MUST NOT be nested.
  * FOCUS-defined contract application properties MUST adhere to the following requirements:
    * Contract application property key MUST match the spelling and casing specified for the FOCUS-defined property.
    * Contract application property value MUST be of the type specified for that property.
    * Contract application property MUST adhere to additional normative requirements specific to that property.
  * Contract application property keys MUST begin with the string "x_" unless it is a FOCUS-defined allocation property.

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
