# Commitment Program Eligibility Details Object

Commitment Program Eligibility Details consists of a valid JSON object with a top-level property key `CommitmentPrograms` containing an array of objects describing the specific *commitment programs* available for the usage charge.

### Object Requirements

CommitmentProgramEligibilityDetailsObject MUST adhere to the following requirements:

* CommitmentProgramEligibilityDetailsObject MUST conform to the [CommitmentProgramEligibilityDetailsObjectSchema](#schemas.datasets.costandusage.commitmentprogrameligibilitydetailsobjectschema) JSON Schema.
* CommitmentProgramEligibilityDetailsObject.CommitmentPrograms[\*].ProgramType MUST correspond to a *commitment program* type supported by the service provider.
* CommitmentProgramEligibilityDetailsObject.CommitmentPrograms[\*].ProgramType MUST match [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for one object in CommitmentProgramEligibilityDetailsObject.CommitmentPrograms when CommitmentDiscountType is not null.
* CommitmentProgramEligibilityDetailsObject.CommitmentPrograms[\*].ProgramType SHOULD correspond to terminology disclosed by the service provider in public documentation.

### Object Schema Structure

<div class="h7-nonindex">Top-Level Properties</div>

| Property             | Type  | Required | Description                                                                         |
|:----------|:----------|:----------|:---------------------------------------|
| `CommitmentPrograms` | Array | True     | Array of objects identifying *commitment programs* for which the usage is eligible. |

<div class="h7-nonindex">CommitmentPrograms Object</div>

The `CommitmentPrograms` array contains one or more objects, each of which contains the following entries:

| Key         | ValueType                            | Required | Description                                                                                                |
|:-------------|:-------------|:-------------|:------------------------------|
| ProgramType | [String](#attributes.stringhandling) | True     | The specific type of commitment program (e.g., discount or capacity reservation) available for this usage. |

### Object Implementation Guidance

<div class="h7-nonindex">Custom Properties</div>

To facilitate querying data across allocations and across service providers, a data generator may include one or more custom properties. These may be placed at the top level of the object (alongside `CommitmentPrograms`) or nested within the individual `CommitmentPrograms` objects. Custom keys must be prefixed with "x_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

### Object Example

Here is a basic example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:commitmentprogrameligibilitydetails).
* For the JSON schema, please see [Commitment Program Eligibility Details Object Schema](#schemas.datasets.costandusage.commitmentprogrameligibilitydetailsobjectschema).

``` json
{
  "CommitmentPrograms": [
    { "ProgramType": "Flexible Spend Plan" },
    { "ProgramType": "Resource Reservation" },
    { "ProgramType": "Advance Resource Commitment" },
    { "ProgramType": "Zonal Resource Commitment" }
  ]
}
```

### Object ID

CommitmentProgramEligibilityDetailsObject

### Object Display Name

Commitment Program Eligibility Details Object

## Description

The types of *commitment programs* available for a specific usage row.

## Content Constraints

| Constraint    | Value                                                                                                                        |
|:-------------------------------------|:---------------------------------|
| Dataset       | [Cost and Usage](#datasets.costandusage)                                                                                     |
| Column type   | Dimension                                                                                                                    |
| Feature level | Conditional                                                                                                                  |
| Allows nulls  | True                                                                                                                         |
| Data type     | JSON                                                                                                                         |
| Value format  | [JSON Object Format](#attributes.jsonobjectformat)                                                                           |
| Object        | [CommitmentProgramEligibilityDetailsObject](#datasets.costandusage.commitmentprogrameligibilitydetails.commitmentprogrameligibilitydetailsobject) |

## Version Introduced

1.4
