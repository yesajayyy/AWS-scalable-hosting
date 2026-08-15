# AWS Scalable Hosting Architecture — Performance Analysis

## 1. Objective

The objective of this performance analysis is to compare the original single-server architecture with the proposed scalable AWS architecture.

The analysis focuses on application responsiveness, scalability, availability, resource utilization and operational monitoring.

---

## 2. Existing Architecture

The original system uses a single application server.

The basic request flow is:

```text
Users
   |
   v
Single Application Server
   |
   v
Application
This can create resource bottlenecks.
Potential Problems
CPU saturation
Memory pressure
Increased response time
Increased request queue length
Application instability
Application downtime
Poor user experience
Limited ability to handle sudden traffic spikes
The single-server architecture also creates a single point of failure.
3. Proposed AWS Architecture
The proposed architecture distributes application traffic across multiple EC2 instances.
Users
   |
   v
Amazon Route 53
   |
   v
Application Load Balancer
   |
   +------------------+
   |                  |
   v                  v
EC2 Instance 1     EC2 Instance 2
   |                  |
   +--------+---------+
            |
      Auto Scaling
            |
            v
        Amazon RDS
Supporting services:
Amazon S3
Amazon CloudWatch
The Application Load Balancer distributes incoming requests across healthy application instances.
Auto Scaling can add or remove instances based on demand.
4. Performance Improvements
4.1 Traffic Distribution
In the original architecture, a single server handles all application requests.
In the proposed architecture, the Application Load Balancer distributes requests across multiple EC2 instances.
Original:

Users
  |
  v
Single Server
  |
  v
Resource Bottleneck
Proposed:

             +--> EC2 Instance 1
Users --> ALB|
             +--> EC2 Instance 2
This reduces the amount of traffic handled by any single application server.
5. Horizontal Scaling
The architecture uses horizontal scaling instead of relying only on a larger server.
Scale-Out
When traffic increases:
Traffic Increase
      |
      v
CloudWatch Metrics
      |
      v
Auto Scaling Policy
      |
      v
Additional EC2 Instance
      |
      v
ALB Adds Healthy Instance
This increases the application's processing capacity.
Scale-In
When traffic decreases:
Traffic Decrease
      |
      v
Lower Resource Utilization
      |
      v
Auto Scaling Policy
      |
      v
Unnecessary Instance Removed
This helps maintain efficient resource utilization.
6. Availability and Performance
Performance and availability are closely related.
If one EC2 instance fails, the Application Load Balancer can detect the unhealthy instance through health checks.
Traffic can then continue to healthy instances.
EC2 Instance 1
     X
  Unhealthy
     |
     v
ALB Health Check
     |
     v
Traffic Removed
     |
     v
Healthy EC2 Instance 2
This prevents a single application instance failure from necessarily causing complete application downtime.
For production deployment, instances should be distributed across multiple Availability Zones.
7. Database Performance
Amazon RDS provides managed relational database infrastructure.
The application instances communicate with the database through the private network.
EC2 Application Servers
          |
          v
     Amazon RDS
Production database considerations include:
Appropriate database instance sizing
Connection management
Index optimization
Query optimization
Automated backups
Monitoring
Multi-AZ deployment where required
The database should be designed to handle the expected application workload.
8. Object Storage Performance
Amazon S3 can be used for object storage instead of storing large files directly on application servers.
Possible objects include:
User uploads
Documents
Reports
Static assets
Backups
This reduces the dependency on local application-server storage.
Application
     |
     v
Amazon S3
     |
     v
Object Storage
9. Monitoring
Amazon CloudWatch provides visibility into infrastructure and application behavior.
Important metrics include:
EC2 Metrics
CPU utilization
Network traffic
Instance health
Disk utilization where applicable
Application Load Balancer Metrics
Request count
Response time
HTTP 4xx errors
HTTP 5xx errors
Healthy host count
Unhealthy host count
Auto Scaling Metrics
Desired capacity
Current capacity
Minimum capacity
Maximum capacity
Scaling activities
RDS Metrics
CPU utilization
Database connections
Storage usage
Read/write operations
Database latency
Monitoring these metrics helps identify performance bottlenecks.
10. Performance Metrics
The following metrics can be used to evaluate the system:
Metric	Purpose
Response Time	Measures application responsiveness
Throughput	Measures requests processed over time
CPU Utilization	Measures compute resource usage
Memory Utilization	Identifies memory pressure
Request Count	Measures application traffic
HTTP Error Rate	Identifies application failures
Healthy Host Count	Measures available application instances
Database Latency	Measures database responsiveness
Network Traffic	Measures network utilization
These metrics can be collected during load testing and normal application operation.
11. Load Testing Approach
A performance test can compare the original and proposed architectures.
Test 1 — Low Traffic
Measure:
Response time
CPU utilization
Error rate
Test 2 — Moderate Traffic
Increase the number of concurrent users and observe:
Response time
Throughput
CPU utilization
Application errors
Test 3 — High Traffic
Generate a larger traffic load and observe:
Auto Scaling behavior
Number of EC2 instances
ALB request distribution
Response time
Error rate
Test 4 — Instance Failure
Stop or terminate one test EC2 instance and observe:
ALB health checks
Traffic redistribution
Auto Scaling replacement
Application availability
12. Expected Results
The proposed architecture is expected to provide:
Better Scalability
The application can increase compute capacity by adding EC2 instances.
Better Availability
Multiple instances reduce dependence on a single application server.
Better Traffic Distribution
The Application Load Balancer distributes requests across healthy instances.
Improved Fault Tolerance
Failure of one application instance does not necessarily result in complete application downtime.
Better Monitoring
CloudWatch provides centralized visibility into infrastructure performance.
Better Resource Utilization
Auto Scaling can adjust compute capacity based on demand.
13. Performance Trade-offs
The scalable architecture introduces additional network and infrastructure components.
These include:
Application Load Balancer
Multiple EC2 instances
Auto Scaling
RDS
CloudWatch
These services introduce additional configuration and operational complexity.
However, the benefits become more important as application traffic and availability requirements increase.
14. Performance Optimization Recommendations
Recommended practices include:
Right-size EC2 instances.
Configure appropriate Auto Scaling policies.
Use ALB health checks.
Monitor application response time.
Optimize database queries.
Use database indexes where appropriate.
Store large objects in Amazon S3.
Monitor CloudWatch metrics.
Configure appropriate log retention.
Perform regular load testing.
Distribute production instances across Availability Zones.
Review performance metrics regularly.
15. Demo Application
The working Flask application is deployed on Render for demonstration purposes.
The public deployment demonstrates the functionality of the application and its APIs.
The AWS architecture represents the proposed production architecture that can be used to provide scalable and highly available hosting.
No AWS performance benchmark is claimed from the Render demonstration deployment.
16. Conclusion
The proposed AWS architecture provides a more scalable and resilient hosting platform than the original single-server design.
The combination of:
Amazon Route 53
Application Load Balancer
Amazon EC2
Auto Scaling
Amazon RDS
Amazon S3
Amazon CloudWatch
creates a foundation for handling changing traffic levels while improving availability, monitoring and operational reliability.
Actual performance improvements should be validated through load testing and production monitoring rather than assumed without measurement.