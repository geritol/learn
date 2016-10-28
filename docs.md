[//]: <> ( # header)
[//]: <> (dubble space line break)
[//]: <> ([cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

**Questions**
- WorkParty: Required, vs Visible on Entry


---
**Explore data model:** App -> _run a search on its name_ -> Data model -> Property

---
## <a name="data-transform"/> /stub Data Transform
Data Transform is an option for copying and manipulating data.

**Creation:** App -> _right click a case_ -> +Create -> Data Transform  
_or_ click crosshair next to a Data transform input (eg.: at Work Parties)

**Usage:**
- Call from a flow action rule
- call from a connector
- [pyDefault](#data-transform-pyDefault)

### <a name="data-transform-pyDefault"/> pyDefault
pyDefault is called whenever a new case is created, and allows you to set properties on creation.



## <a name="activity"/> Activity

An Activity is an automated procedure, structured as a series of steps that execute in sequence.

**Creation:** +Create -> Technical -> Activity  
**Adding to a process:**
Select process -> open process -> + -> Utility

**Page context:**
- Primary page: provides data context for the whole Activity
- Step page: context during execution of a specific step, if not defined, Primary page becomes the Step page
- Parameter page: contains activity parameters, which can be modified by the activity itself too

**Best Practice:**

look for standard options or out of the box activities where possible.  
Replacements:
- data manipulation: [Data Transforms](#data-transform)
- data calculations: Declare Expressions
- external DB query: Report Definitions

More info [here](https://pdn.pega.com/nine-tactics-reduce-your-need-custom-activities-prpc-62-sp2) on reducing need of custom activities

### Standard API activities:

**Access:** Designer Studio -> Processes and Rules -> APIs

## <a name="work-party"/>Work party
A Pega way of defining user groups and roles such as Customer or Manager.

 **Access:** App -> _select case type_ -> Process -> Work Parties -> pyCaseManagmentDefault  
 _or_ Case Designer -> _select a case_ -> Settings -> Parties

```
Party label: unique name
Role: auto populated from Party label, identifies the group on the clipboard
Party class: must be the Data-Party class or one of its descendants
 Party Prompt: additional label info to distinguish different parties
 Data transform: can be used to define initial values. The data transform must be in the party class or a parent class.
 VOE?: Visible on Entry if checked, the users are prompted to add this party every time a case is created
 Required?: if true, this work party must be present in every new case
```

 The role identifies the party on the clipboard. Each work party is a page within the WorkParty page group, and the role is used as the page index. For example, a work party with the role Customer is identified on the clipboard as **WorkParty(Customer)**.

 ## <a name="sla"/>SLAs

Advanced SLAs using rules: Case Designer -> _select a case_ -> _select assignment_ -> Goal & Deadline -> Use existing



Aviable config using SLA rules:

Assignment ready
- Immediately (default)
- Dinamically defined on Property: delay until specific time
- Timed delay: delay with specific amount of time

Calculate service levels
- Intervall from when assigment is ready
- Set to value of property

Service level definitions
- goal interval
- deadline interval
- passed deadline interval repeats (can be for a fixed amount of time or indefinitely until the user completes the assignment)

**.pxUrgencyWork** contains the default urgency value (defaults to 10)  
**.pxUrgencyAssignSLA** contains the current urgency  
**.pyUrgencyAssignAdjust** adds option for manual addjustments via actions

## Routing assignments
Routing identifies who will work on an assignment as a case moves through a life cycle.

**Worklist** is a list of all open assignments for specific users  
**Workbasket** when assignments are queued for a team of users, the assignments are stored in workbaskets. A team associated with a workbasket is called a _work group_.



s
