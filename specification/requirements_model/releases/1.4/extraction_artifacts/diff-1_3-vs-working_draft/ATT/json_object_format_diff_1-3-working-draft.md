## Diff

diff --git a/specification/attributes/json_object_format.md b/specification/attributes/json_object_format.md
index 9409507b..73d5fc5d 100644
--- a/specification/attributes/json_object_format.md
+++ b/specification/attributes/json_object_format.md
@@ -1,6 +1,6 @@
# JSON Object Format

JSON Objects extend the [Key-Value [-Format](#keyvalueformat)-]{+Format](#attributes.key-valueformat)+} to add support for complex data types like arrays and nested key-value pairs. This format is used when the Key-Value Format is insufficient to represent the complexity, such as when multiple sets of key-value pairs apply to the same charge record. JSON Objects are also referred to as maps, trees, or hashtables.

All complex JSON Object columns defined in the FOCUS specification MUST follow the object formatting requirements listed below.

@@ -19,10 +19,10 @@ Rules and formatting requirements for columns appearing in a [*FOCUS dataset*](#
## Requirements

* JsonObjectFormat columns MUST contain a serialized JSON string, consistent with the [ECMA 404](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf) definition of an object.
* Objects used within JsonObjectFormat {+MUST+} adhere to the following[-additional-] requirements:
  * Object keys MUST be unique within an object.
  * Object values MUST be one of the following types: number, string, `true`, `false`, array, object, or `null`.
* Arrays used within JsonObjectFormat {+MUST+} adhere to the following[-additional-] requirements:
  * Array elements MUST all use the same, consistent type.
  * Array elements MUST NOT be repeated.
  * Array elements MUST NOT be null.
