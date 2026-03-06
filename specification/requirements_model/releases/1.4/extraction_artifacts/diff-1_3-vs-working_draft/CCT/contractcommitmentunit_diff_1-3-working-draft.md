## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractcommitmentunit.md b/specification/datasets/contract_commitment/columns/contractcommitmentunit.md
index 93cf0eeb..e0cc33ee 100644
--- a/specification/datasets/contract_commitment/columns/contractcommitmentunit.md
+++ b/specification/datasets/contract_commitment/columns/contractcommitmentunit.md
@@ -4,13 +4,12 @@ The Contract Commitment Unit represents a service-provider-specified measurement

## Requirements

ContractCommitmentUnit [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentUnit MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentUnit MUST be of type String.
* ContractCommitmentUnit MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ContractCommitmentUnit SHOULD conform to [-[UnitFormat](#unitformat)-]{+[UnitFormat](#attributes.unitformat)+} requirements.
* ContractCommitmentUnit {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ContractCommitmentUnit MUST be null when ContractCommitmentQuantity is null.
  * ContractCommitmentUnit MUST NOT be null when ContractCommitmentQuantity is not null.

@@ -28,13 +27,14 @@ A service-provider-specified measurement unit for the amount declared in Contrac

## Content Constraints

| Constraint      [-   |-]{+|+} Value                                                {+|+}
{+|:----------------|:-----------------------------------------------------|+}
{+| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |+}
{+| Column type     | Dimension               +}                            [- |-]
[-| :-------------] |[-:----------------------------------]
| {+Feature level+}   | [-Column type-]{+Mandatory    +}  [-| Dimension-]              [-|-]
[-| Feature level | Mandatory-]                        |
| Allows nulls [- |-]{+   |+} True                                [-|-]{+                 |+}
| Data type       | String                              [-|-]{+                 |+}
| Value format    | [Unit [-Format](#unitformat)-]{+Format](#attributes.unitformat)+} recommended    |

## Introduced (version)

