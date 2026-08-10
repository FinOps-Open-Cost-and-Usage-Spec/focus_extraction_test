# Contract Commitment Applicability

Contract Commitment Applicability is a structured definition of the specific entities eligible for coverage under a [*contract commitment*](#glossary:contract-commitment). This column details inclusionary and exclusionary logic, as well as the specific portion of eligible cost or usage that is applicable.

## Requirements

### Column Requirements

ContractCommitmentApplicability MUST adhere to the following requirements:

* ContractCommitmentApplicability MUST be of type JSON Object (serialized as a String where necessary).
* ContractCommitmentApplicability MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractCommitmentApplicability MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* ContractCommitmentApplicability MUST conform to [ContractCommitmentApplicabilityObject](#datasets.contractcommitment.contractcommitmentapplicability.contractcommitmentapplicabilityobject) requirements.
* ContractCommitmentApplicability MUST NOT be null.

## Column ID

ContractCommitmentApplicability

## Display Name

Contract Commitment Applicability

## Description

A structured definition of the specific entities to which a contract commitment applies, including inclusion/exclusion logic and applicability percentages.

## Content Constraints

| Constraint | Value |
| :--- | :--- |
| Dataset | [Contract Commitment](#datasets.contractcommitment) |
| Column type | Dimension |
| Feature level | Mandatory |
| Allows nulls | False |
| Data type | JSON |
| Value format | [JSON Object Format](#attributes.jsonobjectformat) |
| Object          | [ContractCommitmentApplicabilityObject](#datasets.contractcommitment.contractcommitmentapplicability.contractcommitmentapplicabilityobject) |

## Introduced (version)

1.4
