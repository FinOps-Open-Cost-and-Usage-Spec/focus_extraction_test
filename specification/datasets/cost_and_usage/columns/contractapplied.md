# Contract Applied

Contract Applied is a set of properties that associate a [*charge*](#glossary:charge) with one or more [*contract commitments*](#glossary:contract-commitment), denoted as key-value pairs in a JSON object. Contract Applied allows the practitioner to track the progress of the commitments to which they have agreed with a service provider.

## Requirements

### Column Requirements

ContractApplied MUST adhere to the following requirements:

* ContractApplied MUST be of type JSON Object (serialized as a String where necessary).
* ContractApplied MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractApplied MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* ContractApplied MUST NOT be null when one or more *contract commitments* are applied to the *charge*.
* ContractApplied MUST conform to [ContractAppliedObject](#datasets.costandusage.contractapplied.contractappliedobject) requirements when ContractApplied is not null.

## Column ID

ContractApplied

## Display Name

Contract Applied

## Description

A set of properties that associate a *charge* with one or more *contract commitments*.

## Content Constraints

| Constraint | Value |
| :--- | :--- |
| Dataset | [Cost and Usage](#datasets.costandusage) |
| Column type | Dimension / Metric |
| Feature level | Conditional |
| Allows nulls | True |
| Data type | JSON |
| Value format | [JSON Object Format](#attributes.jsonobjectformat) |
| Object | [ContractAppliedObject](#datasets.costandusage.contractapplied.contractappliedobject) |

## Version Introduced

1.3
