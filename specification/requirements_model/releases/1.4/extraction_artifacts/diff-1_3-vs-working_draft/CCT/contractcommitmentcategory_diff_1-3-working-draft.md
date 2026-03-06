## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractcommitmentcategory.md b/specification/datasets/contract_commitment/columns/contractcommitmentcategory.md
index 9e397ba1..dd9a060c 100644
--- a/specification/datasets/contract_commitment/columns/contractcommitmentcategory.md
+++ b/specification/datasets/contract_commitment/columns/contractcommitmentcategory.md
@@ -4,9 +4,8 @@ Contract Commitment Category represents the highest-level classification of a [*

## Requirements

ContractCommitmentCategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentCategory MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentCategory MUST be of type String.
* ContractCommitmentCategory MUST NOT be null.
* ContractCommitmentCategory MUST be one of the allowed values.
@@ -25,13 +24,14 @@ Represents the highest-level classification of a *contract commitment* based on

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | [-:--------------]{+:----------------------------------------------------|+}
{+| Dataset         | [Contract Commitment](#datasets.contractcommitment)+}  |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

Allowed values:

