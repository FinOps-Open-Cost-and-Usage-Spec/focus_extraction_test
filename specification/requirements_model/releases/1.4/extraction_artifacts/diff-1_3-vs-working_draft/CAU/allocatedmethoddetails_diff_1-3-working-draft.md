## Diff

diff --git a/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md b/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md
index 3522731c..44c128e4 100644
--- a/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md
+++ b/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md
@@ -2,101 +2,65 @@

Allocated Method Details provides information about how resources are allocated when usage records are split to support cost allocation requirements.

Allocated Method Details consists of a valid JSON object which contains an array consisting of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined {+property+} keys but can be extended to provide additional details about the allocation.[-The FOCUS-defined properties are:-]

[-* `Allocated Ratio`: The ratio of a [*charge*](#glossary:charge) that this allocation represents.-]
[-* `Usage Unit`: Unit being measured used to calculate this allocation.-]
[-* `Usage Quantity`: The quantity of units used denominated by the defined usage unit.-]

[-In addition to these, a data generator may include one or more custom properties, also denoted as key-value pairs.-]

## Requirements

### Column Requirements

[-The-]AllocatedMethodDetails [-column adheres-]{+MUST adhere+} to the following requirements:

* AllocatedMethodDetails[-SHOULD be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).-]
[-* AllocatedMethodDetails-] MUST be of type [-String.-]{+JSON Object (serialized as a String where necessary).+}
* AllocatedMethodDetails MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* AllocatedMethodDetails MUST conform to [-[JsonObjectFormat](#jsonobjectformat)-]{+[JsonObjectFormat](#attributes.jsonobjectformat)+} requirements.
* AllocatedMethodDetails {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedMethodDetails MUST be null when a charge is not related to a data generator-calculated split cost allocation.
  * AllocatedMethodDetails SHOULD NOT be null when a charge is related to a data generator-calculated split cost allocation.
{+* AllocatedMethodDetails MUST conform to [AllocatedMethodDetailsObject](#datasets.costandusage.allocatedmethoddetails.allocatedmethoddetailsobject) requirements when AllocatedMethodDetails is not null.+}

[-### Object Schema Requirements-]{+##+} Allocated Method Details [-consists of a valid JSON object which contains an array of key-value objects describing the one or more factors (allocation properties) that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.-]

[-When AllocatedMethodDetails is not null, the JsonObjectFormat for AllocatedMethodDetails adheres to the following requirements:-]
[-* AllocatedMethodDetails MUST have a top-level key "Elements" which contains an array.-]
[-* Each item in "Elements" MUST be an object.-]
[-  * Objects inside "Elements" MUST conform to [KeyValueFormat](#key-valueformat) requirements.-]
[-    * FOCUS-defined allocation properties adhere to the following additional requirements:-]
[-      * Allocation property key MUST match the spelling and casing specified for the FOCUS-defined property.-]
[-      * Allocation property value MUST be of the type specified for that property.-]
[-      * Allocation properties MUST adhere to additional normative requirements specific to that property.-]
[-    * Data generator-defined allocation properties MAY be included in "Elements".-]
[-      * Allocation property keys MUST begin with the string "x_" unless it is a FOCUS-defined allocation property.-]
[-* AllocatedMethodDetails root object MAY contain additional data generator-defined items, in addition to "Elements".-]

[-### Content Requirements-]

[-The following keys are used for allocation properties to facilitate querying data across allocations and across data generators. Focus-defined keys will appear in the list below and data generator-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.-]

[-<b>Allocated Ratio</b>-]

[-Allocated Ratio communicates the percentage of the [*Origin Charge*](#glossary:origin-charge) that this [*Allocated Charge*](#glossary:allocated-charge) derived from the corresponding [Allocated Method Id](#allocatedmethodid) and Usage Unit property.-]

[-The "AllocatedRatio" property adheres to the following requirements:-]

[-* "AllocatedRatio" MUST be included inside each "Elements" object.-]
[-* Values for "AllocatedRatio" MUST be a decimal value compatible with [NumericFormat](#numericformat) representing the allocated charge's percentage of the origin charge.-]
[-* Values for all "AllocatedRatio" properties across all allocated charges related to a single origin charge MUST sum up to 1 (100%).-]{+Object+}

[-<b>Usage Unit</b>-]{+Allocated Method Details consists of a valid JSON object with a top level key of Elements containing an Array of entry objects. Each entry object consists of FOCUS-defined property keys but can be extended to provide additional details about the allocation.+}

[-Usage Unit communicates-]{+The following section details+} the [-aspect-]{+normative requirements for the AllocatedMethodDetailsObject and its nested properties. For a logical overview+} of the [-documented Allocation Method Id being used to calculate-]{+expected content, see+} the [-Allocated Ratio property-]{+[Schema Structure](#datasets.costandusage.allocatedmethoddetails.schemastructure)+} and [-what is being measured by Usage Quantity property.-]{+[Object Example](#datasets.costandusage.allocatedmethoddetails.objectexample) sections.+}

[-The "UsageUnit" property adheres to the following requirements:-]{+### Object Requirements+}

[-* "UsageUnit"-]{+The AllocatedMethodDetailsObject+} MUST [-be included inside an "Elements" object if "UsageQuantity" allocation property is included in that "Elements" object, otherwise "UsageUnit" MAY be included in each "Elements" object.-]
[-* Values for "UsageUnit" MUST capture the unit or component of data generator's documented [AllocationMethod](#allocationmethodid) that was used-]{+adhere+} to[-determine-] the [-"AllocatedRatio" value.-]
[-* Values for "UsageUnit" SHOULD conform to [UnitFormat](#unitformat) requirements.-]{+following requirements:+}

[-<b>Usage Quantity</b>-]{+* AllocatedMethodDetailsObject MUST conform to the [AllocatedMethodDetailsObjectSchema](#schemas.datasets.costandusage.allocatedmethoddetailsobjectschema) JSON Schema.+}
{+* AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio MUST represent the allocated charge's percentage of the origin charge.+}
{+* Values for all AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio properties across all allocated charges related to a single origin charge MUST sum up to 1 (100%).+}
{+* AllocatedMethodDetailsObject.Elements[\*].UsageUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.+}
{+* AllocatedMethodDetailsObject.Elements[\*].UsageUnit MUST represent the unit or component of data generator's documented [AllocationMethod](#datasets.costandusage.allocatedmethodid) which was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.+}
{+* AllocatedMethodDetailsObject.Elements[\*].UsageQuantity SHOULD capture the quantity or volume of the AllocatedMethodDetailsObject.Elements[\*].UsageUnit measured by the data generator that was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.+}

[-Usage Quantity communicates the volume that was consumed or used, denominated in the Usage Unit property value.-]{+## Schema Structure+}

[-The "UsageQuantity" property adheres to-]{+AllocatedMethodDetails contains a structured JSON object defining+} the [-following requirements:-]{+allocation properties used to calculate a split cost allocation.+}

[-* "UsageQuantity" MAY be included inside an "Elements" object when that "Elements" object contains a "UsageUnit" allocation property.-]
[-* Values for "UsageQuantity" MUST be compatible with NumericFormat.-]
[-* Values for "UsageQuantity" SHOULD capture the quantity or volume of the "UsageUnit" measured by the data generator that was used to determine the "AllocatedRatio" value.-]{+### Top-Level Properties+}

[-## Overview-]{+| Property | Type | Required | Description |+}
{+| :--- | :--- | :--- | :--- |+}
{+| `Elements` | Array | True | The parent array containing one or more objects which communicate information about how an allocated record was calculated. |+}

### [-Array of Objects-]{+Elements Object+}

The[-parent array is called-] `Elements`[-and contains one or more objects which communicate information about how an allocated record was calculated.-]

[-| Key | ValueType | Required | Description |-]
[-| ----- | ---- | ---------- | ----------- |-]
[-| Elements | Array | True | The parent-] array [-containing-]{+contains+} one or more [-objects-]{+objects, each of+} which [-communicate information about how an allocated record was calculated. |-]{+contains the following entries:+}

[-### Object Entries-]{+| Key | Type | Required | Description |+}
{+| :--- | :--- | :--- | :--- |+}
{+| `AllocatedRatio` | Numeric | True | Communicates the percentage of the [*Origin Charge*](#glossary:origin-charge) that this [*Allocated Charge*](#glossary:allocated-charge) derived from the corresponding [Allocated Method Id](#datasets.costandusage.allocatedmethodid) and Usage Unit property. |+}
{+| `UsageUnit` | String | Conditional | Communicates the aspect of the documented Allocation Method Id being used to calculate the Allocated Ratio property and what is being measured by Usage Quantity property. <br><br>**Condition:** must be present if Usage Quantity is provided. |+}
{+| `UsageQuantity` | Numeric | False | Communicates the volume that was consumed or used, denominated in the Usage Unit property value. |+}

[-The `Elements` array contains one or more objects, each of which contains the following entries:-]{+## Object Example+}

[-| Key | ValueType | Required | Description |-]
[-| ----- | ---- | ---------- | ----------- |-]
[-| AllocatedRatio | Numeric | True | Percentage-]{+Here is a basic example+} of [-overall cost derived from corresponding method and metric. |-]
[-| UsageUnit | [String](#stringhandling) | Conditional | Unit being measured used to calculate allocation. |-]
[-| UsageQuantity | Numeric | False | Volume of UsageUnit consumed or used. |-]{+the object format.+}

[-### Example-]{+* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:allocatedmethoddetails).+}
{+* For the JSON schema, please see [Allocated Method Details Object Schema](#schemas.datasets.costandusage.allocatedmethoddetailsobjectschema).+}

```json
{
@@ -112,98 +76,20 @@ The `Elements` array contains one or more objects, each of which contains the fo
}
```

[-### JSON Type Definition-]{+## Implementation Guidance+}

[-```json-]
[-{-]
[-  "properties": {-]
[-    "Elements": {-]
[-      "elements": {-]
[-        "properties": {-]
[-          "AllocatedRatio": { "type": "float64" }-]
[-        },-]
[-        "optionalProperties": {-]
[-          "UsageUnit": { "type": "string" },-]
[-          "UsageQuantity": { "type": "float64" }-]
[-        },-]
[-        "additionalProperties": true-]
[-      }-]
[-    }-]
[-  },-]
[-  "additionalProperties": true-]
[-}-]
[-```-]{+### Custom Properties+}

[-NOTE: The above JSON Type Definition (JTD) is an approximation of-]{+To facilitate querying data across allocations and across data generators, a data generator may include one or more custom properties. These may be placed at+} the [-expected contents-]{+top level+} of[-this column, but it should not be considered normative because it cannot accurately describe-] the [-normative requirements (above) for AllocatedMethodDetails. Where there are discrepancies, deference will-]{+object (alongside `Elements`) or nested within the individual `Elements` objects. Custom keys must+} be [-given-]{+prefixed with "x_" followed by PascalCase format (e.g., `x_MyCustomKey`)+} to [-the normative requirements. For example, [NumericFormat](#numericformat) allows for multiple numeric data types and precisions, but JTD requires both-]{+make them easy+} to [-be specified; other numeric data types and precisions allowable under NumericFormat are considered valid.-]{+identify as well as prevent collisions with FOCUS-defined keys.+}

[-## Example Scenarios-]{+### Object ID+}

[-The JSON samples in the scenarios below each represent a single allocated record out of the multiple records derived from an origin record for that scenario. The sum AllocatedRatio will add up to 1 (100%) across all allocated records for an origin record, with the AllocatedRatio (or sum of AllocatedRatio) representing the allocated record's portion of the overall origin record.-]{+AllocatedMethodDetailsObject+}

### [-Scenario 1: Single "UsageUnit" value used for allocation-]{+Object Display Name+}

[-When only a single "UsageUnit" is used to calculate the allocation.-]{+Allocated Method Details Object+}

[-```json-]
[-{-]
[-  "Elements" : [ {-]
[-    "AllocatedRatio" : 0.1,-]
[-    "UsageUnit" : "Hours",-]
[-    "UsageQuantity" : 300-]
[-    }-]
[-  ]-]
[-}-]
[-```-]
[-### Scenario 2: Multiple "UsageUnit" values used for allocation-]

[-When multiple "UsageUnit" values are used to calculate the allocation, another object is added to the "Elements" collection.-]

[-```json-]
[-{-]
[-  "Elements": [-]
[-    {-]
[-      "AllocatedRatio": 0.05,-]
[-      "UsageUnit": "CPU",-]
[-      "UsageQuantity": 0.5-]
[-    },-]
[-    {-]
[-      "AllocatedRatio": 0.1,-]
[-      "UsageUnit": "Memory",-]
[-      "UsageQuantity": 4-]
[-    }-]
[-  ]-]
[-}-]
[-```-]
[-### Scenario 3: Data generator omits keys that are not required-]

[-This data generator does not wish to supply the "UsageUnit" or "UsageQuantity" keys but still provides cost allocation with some additional allocation method details. In this case, "UsageUnit" and "UsageQuantity" are omitted, and only the "AllocatedRatio" is supplied.-]

[-```json-]
[-{-]
[-  "Elements" : [ {-]
[-    "AllocatedRatio" : 0.45-]
[-    }-]
[-  ]-]
[-}-]
[-```-]
[-### Scenario 4: Additional non-FOCUS specified properties-]

[-A data generator can add additional properties if they feel more context is helpful or necessary to the practitioner. In this scenario, the data generator is supplying additional context that shows only 0.5 of a unit was used. However, since 1 unit was requested by the service this allocation represents, the allocation is being charged at 1 regardless.-]

[-```json-]
[-{-]
[-  "Elements": [-]
[-    {-]
[-      "AllocatedRatio": 0.6,-]
[-      "UsageUnit": "vCPU",-]
[-      "UsageQuantity": 1,-]
[-      "x_ReservedVCPU": 1,-]
[-      "x_UsedVCPU": 0.5,-]
[-      "x_AllocatedVCPU": 1-]
[-    }-]
[-  ]-]
[-}-]
[-```-]
## Column ID

AllocatedMethodDetails
@@ -218,13 +104,15 @@ A set of properties describing how resources are allocated in data generator-def

## Content Constraints

| Constraint | Value |
[-|:----------------|:----------------|-]{+| :--- | :--- |+}
{+| Dataset | [Cost and Usage](#datasets.costandusage) |+}
| Column type | Dimension |
| Feature level | Recommended |
| Allows nulls | True |
| Data type | JSON |
| Value format | [JSON Object [-Format](#jsonobjectformat)-]{+Format](#attributes.jsonobjectformat) |+}
{+| Object | [AllocatedMethodDetailsObject](#datasets.costandusage.allocatedmethoddetails.allocatedmethoddetailsobject)+} |

## Introduced (version)

