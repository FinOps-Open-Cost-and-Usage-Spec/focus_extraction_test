## Diff

diff --git a/specification/datasets/cost_and_usage/columns/capacityreservationid.md b/specification/datasets/cost_and_usage/columns/capacityreservationid.md
index 48b2a56f..6bc08806 100644
--- a/specification/datasets/cost_and_usage/columns/capacityreservationid.md
+++ b/specification/datasets/cost_and_usage/columns/capacityreservationid.md
@@ -4,16 +4,15 @@ A Capacity Reservation ID is the identifier assigned to a [*capacity reservation

## Requirements

CapacityReservationId [-adheres-]{+MUST adhere+} to the following requirements:

[-* CapacityReservationId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *capacity reservations*.-]
* CapacityReservationId MUST be of type String.
* CapacityReservationId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* CapacityReservationId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CapacityReservationId MUST be null when a *charge* is not related to a *capacity reservation*.
  * CapacityReservationId MUST NOT be null when a *charge* represents the unused portion of a *capacity reservation*.
  * CapacityReservationId SHOULD NOT be null when a *charge* is related to a capacity reservation.
* When CapacityReservationId is not null, CapacityReservationId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CapacityReservationId MUST be a unique identifier within the service provider.
  * CapacityReservationId SHOULD be a fully-qualified identifier.

@@ -31,13 +30,14 @@ The identifier assigned to a *capacity reservation* by the service provider.

## Content constraints

| Constraint      | Value                                                |
[-|:----------------|:-----------------|-]{+| :-------------- | :--------------------------------------------------- |+}
{+| Dataset         | [Cost and Usage](#datasets.costandusage)             |+}
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

