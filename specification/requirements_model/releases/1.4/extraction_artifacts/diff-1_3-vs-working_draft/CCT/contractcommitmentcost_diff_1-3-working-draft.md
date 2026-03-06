## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractcommitmentcost.md b/specification/datasets/contract_commitment/columns/contractcommitmentcost.md
index e6347fcf..38ee8e5c 100644
--- a/specification/datasets/contract_commitment/columns/contractcommitmentcost.md
+++ b/specification/datasets/contract_commitment/columns/contractcommitmentcost.md
@@ -4,16 +4,15 @@ Contract Commitment Cost represents the monetary value of the [*contract commitm

## Requirements

ContractCommitmentCost [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentCost MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentCost MUST be of type Decimal.
* ContractCommitmentCost MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* ContractCommitmentCost {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ContractCommitmentCost MUST NOT be null when [-[ContractCommitmentCategory](#contractcommitmentcategory)-]{+[ContractCommitmentCategory](#datasets.contractcommitment.contractcommitmentcategory)+} is "Spend".
  * ContractCommitmentCost MAY be null when ContractCommitmentCategory is "Usage".
* ContractCommitmentCost MUST be a valid decimal value.
* ContractCommitmentCost MUST be denominated in the [-[BillingCurrency](#billingcurrency-1).-]{+[BillingCurrency](#datasets.contractcommitment.billingcurrency).+}

## Column ID

@@ -29,14 +28,15 @@ The monetary value of the *contract commitment*.

## Content Constraints

| Constraint    | Value                             {+                 +}  |
| :------------ | [-:----------------------------------]{+:--------------------------------------------------- |+}
{+| Dataset       | [Contract Commitment](#datasets.contractcommitment)+}  |
| Column type   | Metric                              {+                +} |
| Feature level | Mandatory                         {+                 +}  |
| Allows nulls  | True                               {+                 +} |
| Data type     | Decimal                             {+                +} |
| Value format  | [Numeric [-Format](#numericformat)-]{+Format](#attributes.numericformat)         +} |
| Number range  | Any valid decimal value            {+                +}  |

## Introduced (version)

