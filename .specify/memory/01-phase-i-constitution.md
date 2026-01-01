## **Phase I — In-Memory Console Application**

### ***Foundation of Spec-Driven Thinking***

### **Objective**

Prove mastery of **Spec-Driven Development** without framework noise.

### **Architectural Rules**

* Single-process, in-memory state only

* No persistence, no auth, no networking

* Deterministic CLI behavior

### **Allowed Stack**

* Python ≥ 3.13

* UV

* Claude Code

* Spec-Kit Plus

### **Mandatory Features**

* Add task

* Update task

* Delete task

* List tasks

* Toggle completion

### **Design Constraints**

* Tasks identified by ID

* Clear separation: models, logic, CLI

* Zero global mutable state leakage

### **Success Criteria**

Claude Code can regenerate the entire app from specs alone.