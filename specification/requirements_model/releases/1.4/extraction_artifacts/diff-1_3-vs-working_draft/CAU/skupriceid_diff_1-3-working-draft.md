## Diff

diff --git a/specification/datasets/cost_and_usage/columns/skupriceid.md b/specification/datasets/cost_and_usage/columns/skupriceid.md
index 2167f78c..ee020f2b 100644
--- a/specification/datasets/cost_and_usage/columns/skupriceid.md
+++ b/specification/datasets/cost_and_usage/columns/skupriceid.md
@@ -6,26 +6,25 @@ The composition of properties associated with the SKU Price ID may differ across

## Requirements

SkuPriceId [-adheres-]{+MUST adhere+} to the following requirements:

[-* SkuPriceId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.-]
* SkuPriceId MUST be of type String.
* SkuPriceId MUST conform to [String [-Handling](#stringhandling)-]{+Handling](#attributes.stringhandling)+} requirements.
* SkuPriceId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SkuPriceId MUST be null when [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Tax".
  * SkuPriceId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [-[ChargeClass](#chargeclass)-]{+[ChargeClass](#datasets.costandusage.chargeclass)+} is not "Correction".
  * SkuPriceId MAY be null in all other cases.
* When SkuPriceId is not null, SkuPriceId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * SkuPriceId MUST have one and only one parent [-[SkuId](#skuid).-]{+[SkuId](#datasets.costandusage.skuid).+}
  * SkuPriceId MUST remain consistent over time.
  * SkuPriceId MUST remain consistent across [*billing accounts*](#glossary:billing-account) or contracts.
  * SkuPriceId MAY equal SkuId.
  * SkuPriceId MUST be associated with a given [*resource*](#glossary:resource) or [*service*](#glossary:service) when ChargeCategory is "Usage" or "Purchase".
  * SkuPriceId MUST reference a *SKU Price* in a service-provider-supplied *price list*, enabling the lookup of detailed information about the *SKU Price*.
  * SkuPriceId MUST support the lookup of the [-[ListUnitPrice](#listunitprice)-]{+[ListUnitPrice](#datasets.costandusage.listunitprice)+} when the service provider publishes unit prices exclusive of discounts.
  * SkuPriceId MUST support the verification of the given [-[ContractedUnitPrice](#contractedunitprice)-]{+[ContractedUnitPrice](#datasets.costandusage.contractedunitprice)+} when the service provider supports negotiated pricing concepts.

See [Examples: Commitment Discount [-Flexibility](#commitmentdiscountflexibility)-]{+Flexibility](#appendix.examples:commitmentdiscountflexibility)+} for more details around *commitment discount flexibility*.

## Column ID

@@ -41,13 +40,14 @@ A service-provider-specified unique identifier that represents a specific *SKU P

## Content constraints

| Constraint      | Value                                                |
| [-:----------------]{+:--------------+} | [-:--------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

