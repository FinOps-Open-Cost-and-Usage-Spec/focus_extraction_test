## Diff

diff --git a/specification/datasets/cost_and_usage/columns/skupricedetails.md b/specification/datasets/cost_and_usage/columns/skupricedetails.md
index aeaf8799..ea6fadbd 100644
--- a/specification/datasets/cost_and_usage/columns/skupricedetails.md
+++ b/specification/datasets/cost_and_usage/columns/skupricedetails.md
@@ -1,6 +1,6 @@
# SKU Price Details

SKU Price Details represent a list of [*SKU Price*](#glossary:sku-price) properties (key-value pairs) associated with a specific [SKU Price [-ID](#skupriceid).-]{+ID](#datasets.costandusage.skupriceid).+} These properties include qualitative and quantitative properties of a [*SKUs*](#glossary:sku) (e.g., functionality and technical specifications), along with core stable pricing properties (e.g., pricing [*periods*](#glossary:period), tiers, etc.), excluding dynamic or negotiable pricing elements such as unit price amounts, currency (and related exchange rates), temporal validity (e.g., effective dates), and contract- or negotiation-specific factors (e.g., contract or account identifiers, and negotiable discounts).

The composition of properties associated with a specific *SKU Price* may differ across service providers and across *SKUs* within the same service provider. However, the exclusion of dynamic or negotiable pricing properties should ensure that all [*charges*](#glossary:charge) with the same SKU Price ID share the same SKU Price Details, i.e., that SKU Price Details remains consistent across different [*billing periods*](#glossary:billing-period) and [*billing accounts*](#glossary:billing-account) within a service provider.

@@ -8,29 +8,28 @@ SKU Price Details helps practitioners understand and distinguish *SKU Prices*, e

## Requirements

SkuPriceDetails [-adheres-]{+MUST adhere+} to the following requirements:

* SkuPriceDetails MUST[-be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.-]
[-* SkuPriceDetails MUST-] conform to [-[KeyValueFormat](#key-valueformat)-]{+[KeyValueFormat](#attributes.key-valueformat)+} requirements.
* SkuPriceDetails property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* SkuPriceDetails {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SkuPriceDetails MUST be null when SkuPriceId is null.
  * SkuPriceDetails MAY be null when SkuPriceId is not null.
* When SkuPriceDetails is not null, SkuPriceDetails [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * SkuPriceDetails MUST be associated with a given SkuPriceId.
  * SkuPriceDetails MUST include the FOCUS-defined SKU Price property when an equivalent property is included as a custom property.
  * SkuPriceDetails MUST NOT include properties that are not applicable to the corresponding SkuPriceId.
  * SkuPriceDetails SHOULD include all FOCUS-defined SKU Price properties listed below that are applicable to the corresponding SkuPriceId.
  * SkuPriceDetails SHOULD include all custom SKU Price properties that are applicable to the corresponding SkuPriceId when there is no equivalent FOCUS-defined property.
  * SkuPriceDetails MAY include properties that are already captured in other dedicated columns.
  * SkuPriceDetails properties for a given SkuPriceId {+MUST+} adhere to the following[-additional-] requirements:
    * Existing SkuPriceDetails properties SHOULD remain consistent over time.
    * Existing SkuPriceDetails properties SHOULD NOT be removed.
    * Additional SkuPriceDetails properties MAY be added over time.
  * Property key SHOULD remain consistent across comparable *SKUs* having that property, and the values for this key SHOULD remain in a consistent format.
  * Property key MUST begin with the string "x_" unless it is a FOCUS-defined property.
  * Property value MUST represent the value for a single [-[PricingUnit](#pricingunit)-]{+[PricingUnit](#datasets.costandusage.pricingunit)+} when the property holds a numeric value.
* FOCUS-defined SKU Price properties {+MUST+} adhere to the following[-additional-] requirements:
  * Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  * Property value MUST be of the type specified for that property.
  * Property value MUST represent the value for a single PricingUnit, denominated in the unit of measure specified for that property when the property holds a numeric value.
@@ -59,13 +58,14 @@ A set of properties of a SKU Price ID which are meaningful and common to all ins

## Content Constraints

| Constraint      | Value                                                |
| [-:-------------]{+:--------------+} | [-:------------------------------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | JSON                                                 |
| Value format    | [Key-Value [-Format](#key-valueformat)-]{+Format](#attributes.key-valueformat)+}      |

### FOCUS-Defined Properties

