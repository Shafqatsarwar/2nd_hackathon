# Data Model Specification: Phase II
### The Evolution of Todo — Persistent Storage

---

### 1. Context
This specification defines the database schema and relationship structure for the persistent version of the Todo application, using SQLModel and Neon PostgreSQL.

---

### 2. Objective
Establish a secure, relational data structure that supports multi-tenant task management (tasks isolated by user).

---

### 3. Entities

#### A. User Model
| Field | Type | Constraint | Description |
| :--- | :--- | :--- | :--- |
| `id` | `UUID` (or String) | Primary Key | Linked to Better Auth ID |
| `email` | `String` | Unique, Required | User email address |
| `full_name` | `String` | Optional | User's display name |

#### B. Task Model
| Field | Type | Constraint | Description |
| :--- | :--- | :--- | :--- |
| `id` | `Integer` | Primary Key, Auto-inc | Task identifier |
| `title` | `String` | Required | Task title (max 255 chars) |
| `description` | `String` | Optional | Detailed task notes |
| `completed` | `Boolean` | Default: False | Completion status |
| `user_id` | `UUID` (or String) | Foreign Key | Link to User entity |

---

### 4. Relationships
- **One-to-Many**: A `User` can have multiple `Tasks`.
- **Ownership**: Every `Task` must belong to exactly one `User`.

---

### 5. Technical Constraints
- **ORM**: SQLModel (SQLAlchemy 2.0+ compatible).
- **Naming Convention**: use `snake_case` for fields.
- **Security**: Database level `user_id` indexing for fast filtering.

---

### 6. Acceptance Criteria
- Models successfully created in Python.
- Database tables initialized in Neon PostgreSQL via SQLModel metadata.
- CRUD operations function correctly with user-specific isolation.
