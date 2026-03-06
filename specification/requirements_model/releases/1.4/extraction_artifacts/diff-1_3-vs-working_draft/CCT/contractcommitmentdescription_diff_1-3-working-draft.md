## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractcommitmentdescription.md b/specification/datasets/contract_commitment/columns/contractcommitmentdescription.md
index 65b3cf48..4b4d51b2 100644
--- a/specification/datasets/contract_commitment/columns/contractcommitmentdescription.md
+++ b/specification/datasets/contract_commitment/columns/contractcommitmentdescription.md
@@ -4,11 +4,10 @@ Contract Commitment Description provides a high-level context of a [*contract co

## Requirements

ContractCommitmentDescription [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentDescription MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentDescription MUST be of type String.
* ContractCommitmentDescription MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ContractCommitmentDescription SHOULD NOT be null.
* ContractCommitmentDescription maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

@@ -26,13 +25,14 @@ The self-contained summary of the *contract commitment's* terms.

## Content Constraints

|    Constraint   |      Value                                           |
[-|:----------------|:-----------------|-]{+|:----------------|:-----------------------------------------------------|+}
{+| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |+}
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

