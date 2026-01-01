## **Phase III — AI-Powered Todo Chatbot**

### ***Natural Language as an Interface***

### **Objective**

Replace UI-driven CRUD with **AI-mediated intent**.

### **Architectural Rules**

* Stateless backend

* AI agents never access DB directly

* All actions go through MCP tools

### **Allowed Stack**

* OpenAI ChatKit (UI)

* OpenAI Agents SDK

* Official MCP SDK

* FastAPI + SQLModel

* Neon PostgreSQL

### **Mandatory Capabilities**

* Natural language task management

* Conversation persistence

* MCP tool invocation

* Action confirmation messages

### **Design Constraints**

* Single chat endpoint

* Tools must be idempotent where possible

* Conversation state stored in DB

### **Success Criteria**

"Reschedule my tasks" results in correct MCP tool calls without ambiguity.