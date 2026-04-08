## Diff

diff --git a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_wxe65szz_from.md b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_y76fzsyc_to.md
index 8ae7c671..c8512554 100644
--- a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_wxe65szz_from.md
+++ b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_y76fzsyc_to.md
@@ -1,16 +1,15 @@
# Charge Class

Charge Class indicates whether [-the *row*-]{+a *charge*+} represents a [-correction-]{+*correction*+} to a previously [-invoiced *billing-]{+*closed billing+} period*. Charge Class is commonly used to differentiate [-*corrections*-]{+such corrections+} from {+all other charges, including both+} regularly incurred [-*charges*.-]{+*charges* and *corrections* to *open billing periods*.+}

## Requirements

ChargeClass [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargeClass MUST be present in a Cost and Usage *FOCUS dataset*.-]
* ChargeClass MUST be of type String.
* ChargeClass {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ChargeClass MUST be null when the [-*row*-]{+*charge*+} does not represent a correction [-or when it represents-]{+to+} a [-correction within the current *billing-]{+previously *closed billing+} period*.
  * ChargeClass MUST NOT be null when the [-*row*-]{+*charge*+} represents a correction to a previously [-invoiced *billing-]{+*closed billing+} period*.
* ChargeClass MUST be "Correction" when ChargeClass is not null.

## Column ID
@@ -23,25 +22,25 @@ Charge Class

## Description

Indicates whether [-the *row*-]{+a *charge*+} represents a correction to a previously [-invoiced *billing-]{+*closed billing+} period*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | [-:--------------]{+:--------------------------------------------------- |+}
{+| Dataset         | Cost and Usage+}             |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

Allowed values:

| Value      | Description                                                                                    |
| :--------- | :----------------------------------------------------------------------------------------------|
| Correction | Correction to a previously [-invoiced *billing-]{+*closed billing+} period* (e.g., refunds and credit modifications). |

## Introduced (version)

1.0

