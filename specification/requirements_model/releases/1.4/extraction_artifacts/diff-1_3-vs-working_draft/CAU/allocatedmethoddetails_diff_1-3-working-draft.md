## Diff

diff --git a/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md b/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md
index 3522731c..fd7a2935 100644
--- a/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md
+++ b/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md
@@ -16,13 +16,12 @@ In addition to these, a data generator may include one or more custom properties

### Column Requirements

[-The-]AllocatedMethodDetails [-column adheres-]{+MUST adhere+} to the following requirements:

[-* AllocatedMethodDetails SHOULD be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).-]
* AllocatedMethodDetails MUST be of type String.
* AllocatedMethodDetails MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* AllocatedMethodDetails MUST conform to [-[JsonObjectFormat](#jsonobjectformat)-]{+[JsonObjectFormat](#attributes.jsonobjectformat)+} requirements.
* AllocatedMethodDetails {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedMethodDetails MUST be null when a charge is not related to a data generator-calculated split cost allocation.
  * AllocatedMethodDetails SHOULD NOT be null when a charge is related to a data generator-calculated split cost allocation.

@@ -30,11 +29,12 @@ The AllocatedMethodDetails column adheres to the following requirements:

Allocated Method Details consists of a valid JSON object which contains an array of key-value objects describing the one or more factors (allocation properties) that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.

When AllocatedMethodDetails is not null, the JsonObjectFormat for AllocatedMethodDetails [-adheres-]{+MUST adhere+} to the following requirements:

* AllocatedMethodDetails MUST have a top-level key "Elements" which contains an array.
* Each item in "Elements" MUST be an object.
  * Objects inside "Elements" MUST conform to [-[KeyValueFormat](#key-valueformat)-]{+[KeyValueFormat](#attributes.key-valueformat)+} requirements.
    * FOCUS-defined allocation properties {+MUST+} adhere to the following[-additional-] requirements:
      * Allocation property key MUST match the spelling and casing specified for the FOCUS-defined property.
      * Allocation property value MUST be of the type specified for that property.
      * Allocation properties MUST adhere to additional normative requirements specific to that property.
@@ -48,29 +48,29 @@ The following keys are used for allocation properties to facilitate querying dat

<b>Allocated Ratio</b>

Allocated Ratio communicates the percentage of the [*Origin Charge*](#glossary:origin-charge) that this [*Allocated Charge*](#glossary:allocated-charge) derived from the corresponding [Allocated Method [-Id](#allocatedmethodid)-]{+Id](#datasets.costandusage.allocatedmethodid)+} and Usage Unit property.

[-The-]"AllocatedRatio" property [-adheres-]{+MUST adhere+} to the following requirements:

* "AllocatedRatio" MUST be included inside each "Elements" object.
* Values for "AllocatedRatio" MUST be a decimal value compatible with [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} representing the allocated charge's percentage of the origin charge.
* Values for all "AllocatedRatio" properties across all allocated charges related to a single origin charge MUST sum up to 1 (100%).

<b>Usage Unit</b>

Usage Unit communicates the aspect of the documented Allocation Method Id being used to calculate the Allocated Ratio property and what is being measured by Usage Quantity property.

[-The-]"UsageUnit" property [-adheres-]{+MUST adhere+} to the following requirements:

* "UsageUnit" MUST be included inside an "Elements" object if "UsageQuantity" allocation property is included in that "Elements" object, otherwise "UsageUnit" MAY be included in each "Elements" object.
* Values for "UsageUnit" MUST capture the unit or component of data generator's documented [-[AllocationMethod](#allocationmethodid)-]{+[AllocationMethod](#datasets.costandusage.allocatedmethodid)+} that was used to determine the "AllocatedRatio" value.
* Values for "UsageUnit" SHOULD conform to [-[UnitFormat](#unitformat)-]{+[UnitFormat](#attributes.unitformat)+} requirements.

<b>Usage Quantity</b>

Usage Quantity communicates the volume that was consumed or used, denominated in the Usage Unit property value.

[-The-]"UsageQuantity" property [-adheres-]{+MUST adhere+} to the following requirements:

* "UsageQuantity" MAY be included inside an "Elements" object when that "Elements" object contains a "UsageUnit" allocation property.
* Values for "UsageQuantity" MUST be compatible with NumericFormat.
@@ -93,7 +93,7 @@ The `Elements` array contains one or more objects, each of which contains the fo
| Key | ValueType | Required | Description |
| ----- | ---- | ---------- | ----------- |
| AllocatedRatio | Numeric | True | Percentage of overall cost derived from corresponding method and metric. |
| UsageUnit | [-[String](#stringhandling)-]{+[String](#attributes.stringhandling)+} | Conditional | Unit being measured used to calculate allocation. |
| UsageQuantity | Numeric | False | Volume of UsageUnit consumed or used. |

### Example
@@ -134,7 +134,7 @@ The `Elements` array contains one or more objects, each of which contains the fo
}
```

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column, but it should not be considered normative because it cannot accurately describe the normative requirements (above) for AllocatedMethodDetails. Where there are discrepancies, deference will be given to the normative requirements. For example, [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} allows for multiple numeric data types and precisions, but JTD requires both to be specified; other numeric data types and precisions allowable under NumericFormat are considered valid.

## Example Scenarios

@@ -154,6 +154,7 @@ When only a single "UsageUnit" is used to calculate the allocation.
  ]
}
```

### Scenario 2: Multiple "UsageUnit" values used for allocation

When multiple "UsageUnit" values are used to calculate the allocation, another object is added to the "Elements" collection.
@@ -174,6 +175,7 @@ When multiple "UsageUnit" values are used to calculate the allocation, another o
  ]
}
```

### Scenario 3: Data generator omits keys that are not required

This data generator does not wish to supply the "UsageUnit" or "UsageQuantity" keys but still provides cost allocation with some additional allocation method details. In this case, "UsageUnit" and "UsageQuantity" are omitted, and only the "AllocatedRatio" is supplied.
@@ -186,6 +188,7 @@ This data generator does not wish to supply the "UsageUnit" or "UsageQuantity" k
  ]
}
```

### Scenario 4: Additional non-FOCUS specified properties

A data generator can add additional properties if they feel more context is helpful or necessary to the practitioner. In this scenario, the data generator is supplying additional context that shows only 0.5 of a unit was used. However, since 1 unit was requested by the service this allocation represents, the allocation is being charged at 1 regardless.
@@ -204,6 +207,7 @@ A data generator can add additional properties if they feel more context is help
  ]
}
```

## Column ID

AllocatedMethodDetails
@@ -218,13 +222,14 @@ A set of properties describing how resources are allocated in data generator-def

## Content Constraints

| Constraint      | Value                                                |
[-|:----------------|:----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Recommended                                          |
| Allows nulls    | True                                                 |
| Data type       | JSON                                                 |
| Value format    | [JSON Object [-Format](#jsonobjectformat)-]{+Format](#attributes.jsonobjectformat)+}   |

## Introduced (version)

