## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractid.md b/specification/datasets/contract_commitment/columns/contractid.md
index 6beac777..d8a50d83 100644
--- a/specification/datasets/contract_commitment/columns/contractid.md
+++ b/specification/datasets/contract_commitment/columns/contractid.md
@@ -4,13 +4,12 @@ Contract ID is a service-provider-assigned identifier for a contract describing

## Requirements

ContractId [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractId MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractId MUST be of type String.
* ContractId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ContractId MUST NOT be null.
* When ContractId is not null, ContractId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ContractId MUST be a unique identifier within the service provider.
  * ContractId SHOULD be a fully-qualified identifier.

@@ -28,13 +27,14 @@ A service-provider-assigned identifier for a contract describing the agreed term

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+|:----------------|:-----------------------------------------------------|+}
{+| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |+}
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

