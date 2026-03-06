## Diff

diff --git a/specification/datasets/cost_and_usage/columns/invoiceissuername.md b/specification/datasets/cost_and_usage/columns/invoiceissuername.md
index cd9345a0..b0b2e4a2 100644
--- a/specification/datasets/cost_and_usage/columns/invoiceissuername.md
+++ b/specification/datasets/cost_and_usage/columns/invoiceissuername.md
@@ -4,14 +4,13 @@ Invoice Issuer Name is the name of the entity responsible for issuing payable in

## Requirements

InvoiceIssuerName [-adheres-]{+MUST adhere+} to the following requirements:

[-* InvoiceIssuerName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* InvoiceIssuerName MUST be of type String.
* InvoiceIssuerName MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* InvoiceIssuerName MUST NOT be null.

See [Appendix: Participating Entity Identification [-Examples](#participatingentityidentificationexamples)-]{+Examples](#appendix.examples:participatingentityidentification)+} section for examples of Invoice Issuer Name values across various use case scenarios.

## Column ID

@@ -27,13 +26,14 @@ The name of the entity responsible for invoicing for the *resources* or *service

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

