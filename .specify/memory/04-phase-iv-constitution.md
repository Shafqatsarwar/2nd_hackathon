## **Phase IV — Local Kubernetes Deployment**

### ***Operational Maturity***

### **Objective**

Prove the system is **cloud-native**, not cloud-hosted.

### **Architectural Rules**

* Containers are immutable

* Config via environment variables

* Infrastructure defined declaratively

### **Allowed Stack**

* Docker

* Minikube

* Helm Charts

* kubectl-ai

* kagent

### **Mandatory Additions**

* Dockerized frontend & backend

* Helm charts for deployment

* Multi-replica readiness

* Local cluster deployment

### **Design Constraints**

* No hardcoded service URLs

* No local filesystem dependencies

* Kubernetes is source of truth

### **Success Criteria**

System survives pod restarts with zero data loss.