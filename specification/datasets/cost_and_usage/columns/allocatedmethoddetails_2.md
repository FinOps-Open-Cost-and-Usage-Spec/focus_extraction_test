# Allocated Method Details

Allocated Method Details provides information about how resources are allocated when usage records are split to support cost allocation requirements.

Allocated Method Details consists of a valid JSON object which contains an array consisting of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.

The FOCUS-defined properties are:

* `Allocated Ratio`: The ratio of a [*charge*](#glossary:charge) that this allocation represents.
* `Usage Unit`: Unit being measured used to calculate this allocation.
* `Usage Quantity`: The quantity of units used denominated by the defined usage unit.

In addition to these, a data generator may include one or more custom properties, also denoted as key-value pairs.

## Requirements

### Column Requirements

The AllocatedMethodDetails column MUST adhere to the following requirements:

* AllocatedMethodDetails MUST be of type String.
* AllocatedMethodDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* AllocatedMethodDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* AllocatedMethodDetails MUST adhere to the following nullability requirements:
  * AllocatedMethodDetails MUST be null when a charge is not related to a data generator-calculated split cost allocation.
  * AllocatedMethodDetails SHOULD NOT be null when a charge is related to a data generator-calculated split cost allocation.

### Object Schema Requirements

Allocated Method Details consists of a valid JSON object which contains an array of key-value objects describing the one or more factors (allocation properties) that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.

When AllocatedMethodDetails is not null, the JsonObjectFormat for AllocatedMethodDetails adheres to the following requirements:

* AllocatedMethodDetails MUST have a top-level key "Elements" which contains an array.
* Each item in "Elements" MUST be an object.
  * Objects inside "Elements" MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
    * FOCUS-defined allocation properties adhere to the following additional requirements:
      * Allocation property key MUST match the spelling and casing specified for the FOCUS-defined property.
      * Allocation property value MUST be of the type specified for that property.
      * Allocation properties MUST adhere to additional normative requirements specific to that property.
    * Data generator-defined allocation properties MAY be included in "Elements".
      * Allocation property keys MUST begin with the string "x_" unless it is a FOCUS-defined allocation property.
* AllocatedMethodDetails root object MAY contain additional data generator-defined items, in addition to "Elements".
