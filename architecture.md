# AWS Scalable Hosting Architecture

## 1. Objective

The objective of this project is to redesign a single-server web application into a scalable, highly available and fault-tolerant AWS cloud architecture.

The proposed architecture separates DNS management, traffic distribution, application compute, database services, object storage and monitoring.

---

## 2. Existing Problem

The original application architecture uses a single application server.

This creates several challenges:

- Single point of failure
- Limited scalability
- Performance degradation during traffic spikes
- Manual capacity management
- Difficult maintenance
- Limited fault tolerance
- Increased risk of application downtime

A single server may work for low traffic, but it becomes difficult to maintain reliable performance as the number of users increases.

---

## 3. Proposed AWS Architecture

The proposed architecture uses multiple AWS services working together.

### Request Flow

Users access the application through Amazon Route 53.

Route 53 provides DNS resolution and directs users toward the application endpoint.

The Application Load Balancer receives incoming HTTP/HTTPS requests and distributes traffic across healthy Amazon EC2 instances.

The EC2 instances run the web application.

An Auto Scaling Group automatically increases or decreases the number of EC2 instances based on application demand.

Amazon RDS provides the managed relational database.

Amazon S3 provides durable object storage for application files and assets.

Amazon CloudWatch provides monitoring, metrics, logs and alarms.

### High-Level Architecture

```text
                         Internet Users
                               |
                               v
                     +-------------------+
                     |   Amazon Route 53 |
                     |        DNS        |
                     +-------------------+
                               |
                               v
                  +------------------------+
                  | Application Load       |
                  | Balancer (ALB)        |
                  +------------------------+
                       /              \
                      /                \
                     v                  v
            +---------------+    +---------------+
            |   EC2        |    |   EC2        |
            | Application  |    | Application  |
            |   Server 1   |    |   Server 2   |
            +---------------+    +---------------+
                     \                /
                      \              /
                       +------------+
                             |
                     Auto Scaling Group
                             |
                             v
                    +------------------+
                    |   Amazon RDS     |
                    |    Database      |
                    +------------------+

                    +------------------+
                    |    Amazon S3     |
                    | Object Storage   |
                    +------------------+

                    +------------------+
                    | Amazon CloudWatch|
                    | Monitoring       |
                    +------------------+
4. AWS Components
Amazon Route 53
Amazon Route 53 provides DNS services for the application.
Responsibilities:
Domain name resolution
Routing users to the application
DNS health checking
Reliable DNS infrastructure
Application Load Balancer
The Application Load Balancer distributes incoming application traffic across multiple healthy EC2 instances.
Responsibilities:
Traffic distribution
Health checks
HTTP/HTTPS request handling
Preventing traffic from being concentrated on a single server
Amazon EC2
Amazon EC2 provides the compute capacity required to run the web application.
Multiple EC2 instances are used so that the application does not depend on a single server.
Responsibilities:
Running the Flask/web application
Processing user requests
Providing application compute capacity
Auto Scaling
An Auto Scaling Group manages the number of EC2 instances.
When application demand increases:
Higher Traffic
      ↓
More Compute Capacity Required
      ↓
Additional EC2 Instances
      ↓
Improved Application Capacity
When demand decreases, unnecessary instances can be removed.
This improves resource utilization and reduces the need for manual capacity management.
Amazon RDS
Amazon RDS provides managed relational database infrastructure.
Benefits include:
Managed database operations
Automated backups
Monitoring
Easier maintenance
Improved reliability
Reduced database administration effort
For production workloads, the database should be placed in private subnets and should not be directly accessible from the public internet.
Amazon S3
Amazon S3 provides durable object storage.
Possible uses include:
User-uploaded files
Static assets
Application documents
Backups
Generated reports
S3 separates object storage from application compute resources.
Amazon CloudWatch
Amazon CloudWatch provides monitoring and operational visibility.
It can monitor:
EC2 CPU utilization
Application performance
Load balancer metrics
Request counts
Error rates
Logs
Alarms
CloudWatch alarms can be used to trigger operational actions and support Auto Scaling decisions.
5. Scalability
The architecture is designed to scale horizontally.
Instead of increasing the capacity of a single server, additional EC2 instances can be added.
Scale-Out
Traffic Increases
       ↓
Auto Scaling Detects Demand
       ↓
New EC2 Instance Launched
       ↓
ALB Adds Healthy Instance
       ↓
Traffic Distributed Across Instances
Scale-In
Traffic Decreases
       ↓
Lower Compute Requirement
       ↓
Auto Scaling Removes Unnecessary Instance
       ↓
Reduced Resource Usage
This approach allows the application to respond to changing traffic conditions.
6. High Availability
The architecture improves availability by using multiple application instances.
If one EC2 instance becomes unavailable:
EC2 Instance 1
      X
   Unhealthy
      ↓
ALB Health Check
      ↓
Traffic Removed From Instance 1
      ↓
Traffic Continues Through Healthy Instance 2
This reduces the impact of individual server failures.
For a production deployment, EC2 instances should be distributed across multiple Availability Zones.
7. Security Architecture
Recommended production security controls include:
HTTPS for encrypted communication
IAM least-privilege policies
Security groups controlling network traffic
Private subnets for database resources
Encryption at rest
Encryption in transit
Secure secrets management
Database access restricted to application servers
Regular database backups
CloudWatch monitoring and alarms
The database should not be directly exposed to internet users.
A typical security flow is:
Internet
   |
   v
Application Load Balancer
   |
   v
EC2 Application Servers
   |
   v
Private RDS Database
Only the required communication paths should be allowed.
8. Fault Tolerance
The architecture reduces single points of failure.
Potential failure scenarios include:
EC2 Instance Failure
The ALB detects an unhealthy instance and stops sending traffic to it.
Auto Scaling can launch a replacement instance.
Traffic Spike
Auto Scaling can increase the number of application instances.
The ALB distributes the additional traffic across healthy instances.
Database Failure
Amazon RDS provides managed database capabilities and backup mechanisms.
Production deployments can use Multi-AZ configurations for improved database availability.
9. Monitoring and Operations
Amazon CloudWatch provides visibility into application and infrastructure performance.
Important metrics include:
EC2 CPU utilization
Network traffic
Application load balancer request count
HTTP error rates
Response latency
Auto Scaling activity
Application logs
CloudWatch alarms can notify administrators when important thresholds are exceeded.
10. Design Decisions
The architecture uses direct AWS services to clearly demonstrate the responsibilities of each infrastructure component.
The main design decisions are:
Requirement	AWS Service
DNS	Amazon Route 53
Traffic Distribution	Application Load Balancer
Application Compute	Amazon EC2
Automatic Scaling	Auto Scaling
Relational Database	Amazon RDS
Object Storage	Amazon S3
Monitoring	Amazon CloudWatch
This design provides greater architectural visibility and makes the responsibilities of individual AWS services clear.
11. Expected Benefits
The redesigned architecture provides:
Higher availability
Horizontal scalability
Automatic capacity management
Better traffic distribution
Improved fault tolerance
Managed database infrastructure
Durable object storage
Centralized monitoring
Reduced operational complexity
Better production readiness
12. Demo Deployment
The Flask application used for this project is deployed on Render for demonstration purposes.
The Render deployment provides the publicly accessible working application.
The AWS architecture described in this document represents the proposed production architecture.
This separation allows the project to demonstrate both:
A working cloud-hosted web application
A scalable AWS solution architecture
13. Final Architecture Summary
The proposed solution transforms a single-server application into a scalable cloud architecture:
Users
  |
  v
Route 53
  |
  v
Application Load Balancer
  |
  +-------------------+
  |                   |
  v                   v
EC2 Instance 1     EC2 Instance 2
  |                   |
  +---------+---------+
            |
      Auto Scaling
            |
            v
        Amazon RDS

Supporting Services:

Amazon S3
Amazon CloudWatch
The architecture is designed to provide scalability, availability, fault tolerance, monitoring and operational efficiency while allowing the application to handle changing traffic demands.