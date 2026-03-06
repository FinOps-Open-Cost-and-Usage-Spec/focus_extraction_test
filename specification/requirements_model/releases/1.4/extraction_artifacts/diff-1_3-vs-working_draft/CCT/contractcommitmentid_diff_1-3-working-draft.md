## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractcommitmentid.md b/specification/datasets/contract_commitment/columns/contractcommitmentid.md
index 3f5c74e8..314a29f3 100644
--- a/specification/datasets/contract_commitment/columns/contractcommitmentid.md
+++ b/specification/datasets/contract_commitment/columns/contractcommitmentid.md
@@ -4,16 +4,14 @@ Contract Commitment ID is a service-provider-assigned identifier describing a si

## Requirements

ContractCommitmentId [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentId MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentId MUST be of type String.
* ContractCommitmentId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ContractCommitmentId MUST NOT be null.
*[-When ContractCommitmentId is not null, ContractCommitmentId adheres to the following additional requirements:-]
[-  *-] ContractCommitmentId MUST be a unique identifier within the service provider.
* ContractCommitmentId SHOULD be a fully-qualified identifier.
* ContractCommitmentId MUST have one and only one parent [-[ContractId](#contractid).-]{+[ContractId](#datasets.contractcommitment.contractid).+}
* ContractCommitmentId MAY be equal to ContractId.
* ContractCommitmentId MUST be unique across the Contract Commitment dataset.

@@ -31,13 +29,14 @@ A service-provider-assigned identifier describing a single contract term agreed

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

