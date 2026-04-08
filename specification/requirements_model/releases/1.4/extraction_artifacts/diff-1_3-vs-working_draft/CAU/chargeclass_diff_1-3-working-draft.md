## Diff

diff --git a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff__e93o21q_from.md b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_ge0cfmr8_to.md
index 2434df00..4ed46301 100644
--- a/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff__e93o21q_from.md
+++ b/var/folders/h3/3pbbsg0s01760nzc6wsgc6f40000gn/T/focus_diff_ge0cfmr8_to.md
@@ -1,10 +1,9 @@
## Requirements

ChargeClass [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargeClass MUST be present in a Cost and Usage *FOCUS dataset*.-]
* ChargeClass MUST be of type String.
* ChargeClass {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ChargeClass MUST be null when the [-*row*-]{+*charge*+} does not represent a correction [-or when it represents-]{+to+} a [-correction within the current *billing-]{+previously *closed billing+} period*.
  * ChargeClass MUST NOT be null when the [-*row*-]{+*charge*+} represents a correction to a previously [-invoiced *billing-]{+*closed billing+} period*.
* ChargeClass MUST be "Correction" when ChargeClass is not null.
