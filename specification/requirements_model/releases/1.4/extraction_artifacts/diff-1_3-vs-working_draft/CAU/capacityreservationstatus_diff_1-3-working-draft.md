## Diff

diff --git a/specification/datasets/cost_and_usage/columns/capacityreservationstatus.md b/specification/datasets/cost_and_usage/columns/capacityreservationstatus.md
index 06686df8..6d3e2eec 100644
--- a/specification/datasets/cost_and_usage/columns/capacityreservationstatus.md
+++ b/specification/datasets/cost_and_usage/columns/capacityreservationstatus.md
@@ -4,14 +4,13 @@ Capacity Reservation Status indicates whether the [*charge*](#glossary:charge) r

## Requirements

CapacityReservationStatus [-adheres-]{+MUST adhere+} to the following requirements:

[-* CapacityReservationStatus MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *capacity reservations*.-]
* CapacityReservationStatus MUST be of type String.
* CapacityReservationStatus {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CapacityReservationStatus MUST be null when CapacityReservationId is null.
  * CapacityReservationStatus MUST NOT be null when CapacityReservationId is not null and [-[ChargeCategory](#chargecategory)-]{+[ChargeCategory](#datasets.costandusage.chargecategory)+} is "Usage".
* When CapacityReservationStatus is not null, CapacityReservationStatus [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CapacityReservationStatus MUST be one of the allowed values.
  * CapacityReservationStatus MUST be "Unused" when the *charge* represents the unused portion of a *capacity reservation*.
  * CapacityReservationStatus MUST be "Used" when the *charge* represents the used portion of a *capacity reservation*.
@@ -30,13 +29,14 @@ Indicates whether the *charge* represents either the consumption of a *capacity

## Content constraints

| Constraint      | Value                                                |
| :-------------- | [-:--------------]{+:--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)+}             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | Allowed Values                                       |

Allowed values:

