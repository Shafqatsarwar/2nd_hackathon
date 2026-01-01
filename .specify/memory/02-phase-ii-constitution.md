## **Phase II — Full-Stack Web Application**

### ***From Script to System***

### **Objective**

Introduce **multi-user**, **persistent**, **authenticated** architecture.

### **Architectural Rules**

* Frontend and backend are isolated services

* Backend is the system of record

* Frontend never directly accesses database

### **Allowed Stack**

* Frontend: Next.js ≥ 16 (App Router)

* Backend: FastAPI + SQLModel

* Database: Neon Serverless PostgreSQL

* Auth: Better Auth (JWT)

### **Mandatory Additions**

* RESTful API

* JWT-based authentication

* User-scoped data isolation

* Persistent storage

### **Design Constraints**

* All endpoints require JWT

* user_id from token must match resource access

* SQLModel only (no raw SQL)

### **Success Criteria**

Any authenticated user can only see and mutate their own tasks.