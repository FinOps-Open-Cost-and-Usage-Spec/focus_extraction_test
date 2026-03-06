## Diff

diff --git a/specification/datasets/contract_commitment/columns/contractcommitmentquantity.md b/specification/datasets/contract_commitment/columns/contractcommitmentquantity.md
index d5b80983..c2eba855 100644
--- a/specification/datasets/contract_commitment/columns/contractcommitmentquantity.md
+++ b/specification/datasets/contract_commitment/columns/contractcommitmentquantity.md
@@ -1,16 +1,15 @@
# Contract Commitment Quantity

Contract Commitment Quantity represents the amount associated with the [*contract commitment*](#glossary:contract-commitment), denominated in a service-provider-defined [Contract Commitment [-Unit](#contractcommitmentunit).-]{+Unit](#datasets.contractcommitment.contractcommitmentunit).+}  Contract Commitment Quantity is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a provider and a customer.

## Requirements

ContractCommitmentQuantity [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentQuantity MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentQuantity MUST be of type Decimal.
* ContractCommitmentQuantity MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* ContractCommitmentQuantity {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ContractCommitmentQuantity MUST NOT be null when [-[ContractCommitmentCategory](#contractcommitmentcategory)-]{+[ContractCommitmentCategory](#datasets.contractcommitment.contractcommitmentcategory)+} is "Usage".
  * ContractCommitmentQuantity MAY be null when ContractCommitmentCategory is "Spend".
* ContractCommitmentQuantity MUST be a valid decimal value.

@@ -28,14 +27,15 @@ The amount associated with the *contract commitment*.

## Content Constraints

| Constraint      [-   |-]{+|+} Value                                                {+|+}
{+|:----------------|:-----------------------------------------------------|+}
{+| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |+}
{+| Column type+}     {+| Metric+}                           {+  +}       {+  +}       [-   |-]
[-| :------------ | :----------------------------------]{+  |+}
| {+Feature level+}   | [-Column type   | Metric-]{+Mandatory+}                [-|-]
[-| Feature level | Mandatory-]                 {+  +}       [- |-]{+  |+}
| Allows nulls [- |-]{+   |+} True                                [-|-]{+                 |+}
| Data type       | Decimal                             [-|-]{+                 |+}
| Value format    | [Numeric [-Format](#numericformat)-]{+Format](#attributes.numericformat)         +} |
| Number range    | Any valid decimal value             [-|-]{+                 |+}

## Introduced (version)

