## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractcommitmenttype.md b/specification/datasets/contract_commitment/columns/contractcommitmenttype.md
index 997fc433..d19cb6f2 100644
--- a/specification/datasets/contract_commitment/columns/contractcommitmenttype.md
+++ b/specification/datasets/contract_commitment/columns/contractcommitmenttype.md
@@ -4,11 +4,10 @@ Contract Commitment Type is a service-provider-assigned name to identify the typ

## Requirements

ContractCommitmentType [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentType MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentType MUST be of type String.
* ContractCommitmentType MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ContractCommitmentType MUST NOT be null.
* ContractCommitmentType MUST be a consistent, readable display value.

@@ -26,13 +25,14 @@ A service-provider-assigned name to identify the type of *contract commitment*.

## Content Constraints

| Constraint      | Value                                                |
{+|:----------------|:-----------------------------------------------------|+}
| [-:---------------]{+Dataset+}         | [-:----------------]{+[Contract Commitment](#datasets.contractcommitment)+}  |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

