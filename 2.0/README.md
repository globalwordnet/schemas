#WordNet-LMF 2.0
#===

This is to equip WordNet with state-of-the-art validation schemas the way FrameNet did. This move is dictated by the following:

- DTD does not provide fine-grained control the way XSD does. The most significant difference between DTDs and XML Schema is the capability to create and use **datatypes**. XSD schemas define datatypes for elements and attributes while DTD doesn't support them. This allows for control on what sort of data (ids, content) is expected. Leveraging datatypes gets errors to bubble up instantly that would otherwise go unnoticed.

- It is desirable to distinguish foreign references from internal ones (more below).

- Incidentally the reference to  Dublin Core schema is erroneous (as mentioned [here](https://github.com/globalwordnet/schemas/issues/5) ) in that the definition of elements is mistakenly applied to attributes. Any real validation against the Dublin Core definitions would fail. Besides, Dublin Core seems superimposed and unnatural and it is doubtful it is of real use here.

####name spaces

References to ILI and PWN have been transferred to their own namespace (ili: and pwn: respectively) as do the meta annotations (meta:). 

It is not desirable to mix **foreign references** (in the sense that they refer to something outside the database, the PWN sensekey is a case in point) with **internal references**. Different namespaces reflect this.

####modules

 The design is modular:
 
***ili.xsd*** and ***pwn.xsd*** for all the ILI and PWN stuff in their own namespaces.
***(ewn-)idtypes(-relax_idrefs).xsd*** for core id types (it defines ID policy).
***(ewn-)wordtypes.xsd*** for word types (it defines word form policy).
***types.xsd*** for core data types.
***pwn.xsd*** for PWN namespace.
***ili.xsd*** for ili namespace.
***meta.xsd*** for meta namespace.
***core-2.0.xsd*** for elements and the core structure.

This allows for different levels of validation to be performed. 

This makes it possible to bring stricter constraints to bear on the same data. But it does not mean the previous level is incompatible with the next.For example the data that satisfies EWN-LMF-2.0.xsd is a subset of data validated by WN-LMF-2.0.xsd (or  WN-LMF-2.0 is a superset of EWN-LMF-2.0). 

Another use is different IDREF validation depending on whether you are attempting at validating merged files or not.

####id types

idtypes-2.0.xsd and ewn-idtypes-2.0.xsd differ in that the latter imposes extra constraints on the **well-formedness** of EWN ids.

####relaxed id types vs strict

This deals with **id reference** validation.

*(ewn-)idtypes-2.0.xsd* and *(ewn-)idtypes-2.0-relax_idrefs.xsd* differ in that the latter allows some **non-local references not to have their target in the same file**. This is necessary in the case of part-of-speech cross-references such as the ones found in derivation relations (adj derived from noun, etc...) or maybe other cases (seealso, etc). The target then resides in a different file. This is useful to validate **pre-merging lexicographer files** while the strict mode must be used **to validate the merged file**, to make sure references are not left dangling.

####some resulting combinations:

WN-LMF-2.0-relax_idrefs.xsd
WN-LMF-2.0.xsd
EWN-LMF-2.0-relax_idrefs.xsd
EWN-LMF-2.0.xsd

####migration

A migration tool (to2.0.xsl) is provided in the form of an XSLT 1.0 transform. It does not change the structure nor the data. Only attributes are transformed to satisfy the new naming and namespaces.

####EWN compatibility with 2.0 schema

The transformed lexicographer files satisfy both:

- WN-LMF-2.0-relax_idrefs.xsd
- EWN-LMF-2.0-relax_idrefs.xsd

The transformed merged file satisfies both:

- WN-LMF-2.0.xsd
- EWN-LMF-2.0.xsd

####Validation tool

[Preferred validation tool](https://github.com/1313ou/ewn-validate2) (based on Saxon, fast and efficient) 
[Basic validation tool](https://github.com/1313ou/ewn-validate) (based on standard validation tools that come with Java8, may be slow) 
