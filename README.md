# AWS APAC Solutions Architecture Project

# Scalable Hosting Architecture

A cloud solution architecture project that redesigns a traditional single-server web application into a scalable, highly available and fault-tolerant AWS architecture.

---

## 1. Project Overview

This project demonstrates how a simple single-server web application can be redesigned using AWS cloud services to improve:

- Scalability
- Availability
- Performance
- Reliability
- Fault tolerance
- Monitoring
- Operational efficiency

The project includes a working Flask web application that demonstrates the proposed architecture and provides health, status and architecture APIs.

---

## 2. Business Problem

A traditional single-server architecture can become a bottleneck as application traffic increases.

### Main challenges

- Single point of failure
- Limited scalability
- Performance degradation during traffic spikes
- Manual capacity management
- Difficult maintenance
- Limited fault tolerance
- Increased risk of application downtime

The goal is to redesign the system so that application capacity can adapt to changing traffic while reducing dependence on a single server.

---

## 3. Proposed AWS Architecture

The proposed production architecture uses multiple AWS services.

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

Request Flow
Users
  ↓
Amazon Route 53
  ↓
Application Load Balancer
  ↓
Healthy EC2 Instances
  ↓
Auto Scaling
  ↓
Amazon RDS
Amazon S3 provides object storage and Amazon CloudWatch provides monitoring and operational visibility.

##4. AWS Services

AWS Service	Purpose
Amazon Route 53	DNS and routing
Application Load Balancer	Traffic distribution
Amazon EC2	Application compute
Auto Scaling	Automatic capacity management
Amazon RDS	Managed relational database
Amazon S3	Object storage
Amazon CloudWatch	Monitoring, metrics, logs and alarms

##5. Architecture Benefits

Scalability
Auto Scaling can increase or decrease the number of EC2 instances according to application demand.
Availability
Multiple application instances reduce dependence on a single server.
Load Distribution
The Application Load Balancer distributes incoming traffic across healthy application instances.
Fault Tolerance
If one application instance becomes unavailable, the load balancer can stop sending traffic to that instance.
Monitoring
Amazon CloudWatch provides visibility into application and infrastructure performance.
Operational Efficiency
Managed AWS services reduce the amount of infrastructure that must be manually maintained.

##6. Security Architecture

Recommended production security controls include:
HTTPS
IAM least-privilege policies
Security groups
Private subnets
Private RDS database
Encryption at rest
Encryption in transit
Secure secrets management
Database backups
CloudWatch monitoring
The database should not be directly accessible from the public internet.

##7. Performance

The architecture improves the system's ability to handle changing traffic levels.
The Application Load Balancer distributes requests across multiple application instances.
Auto Scaling allows additional instances to be launched when demand increases.
Important performance metrics include:
Response time
Request count
Throughput
CPU utilization
HTTP error rate
Healthy host count
Database latency
Network traffic
Actual performance improvements should be validated using load testing rather than assumed without measurement.

##8. Cost Analysis

The scalable AWS architecture requires more infrastructure than a single-server deployment.
The major cost drivers include:
EC2 instances
Application Load Balancer
Amazon RDS
Amazon S3
Amazon Route 53
Amazon CloudWatch
Data transfer
Cost optimization strategies include:
Right-sizing EC2 instances
Using Auto Scaling
Monitoring resource utilization
Removing unused resources
Using S3 lifecycle policies
Controlling CloudWatch log retention
Reviewing AWS billing
Using the AWS Pricing Calculator
Exact production cost depends on AWS Region, instance types, traffic, storage and workload.

##9. Working Demo

The Flask application is publicly deployed for demonstration purposes.
Public Application
https://aws-scalable-hosting.onrender.com
Application Status
The homepage displays:
Application status
Deployment environment
Instance hostname
Region
Last health check time

10. API Endpoints

Health Check
/health
Returns the health status of the application.
Example:
{
  "status": "healthy",
  "service": "Scalable Hosting Application",
  "hostname": "server",
  "timestamp": "2026-08-15T16:55:37"
}
Application Status
/api/status
Returns application and architecture status information.
Architecture
/api/architecture
Returns the AWS architecture components used in the proposed design.

##11. Demo Deployment vs Production Architecture

An important distinction is made between the working demonstration deployment and the proposed AWS production architecture.
Demonstration Deployment
Internet
   |
   v
Render
   |
   v
Flask Application
The Flask application is hosted on Render to provide a publicly accessible working demonstration.
Proposed Production Architecture
Users
  |
  v
Route 53
  |
  v
Application Load Balancer
  |
  +----------------+
  |                |
  v                v
EC2 Instance 1  EC2 Instance 2
  |                |
  +-------+--------+
          |
    Auto Scaling
          |
          v
      Amazon RDS

Amazon S3
Amazon CloudWatch
The AWS architecture represents the proposed production solution.
No claim is made that the demonstration application is currently running on AWS.
12. Project Structure
aws-scalable-hosting/
│
├── app.py
├── architecture.md
├── cost-analysis.md
├── performance-analysis.md
├── README.md
├── Procfile
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
Important Files
File	Purpose
app.py	Flask application and API endpoints
index.html	Web application interface
architecture.md	Detailed AWS architecture
cost-analysis.md	AWS cost and optimization analysis
performance-analysis.md	Performance and scalability analysis
requirements.txt	Python dependencies
Procfile	Deployment configuration
README.md	Project documentation

##13. Running the Application Locally

Clone the repository
git clone https://github.com/yesajayyy/AWS-scalable-hosting.git
Enter the project directory
cd AWS-scalable-hosting
Create a virtual environment
python3 -m venv venv
Activate the virtual environment
macOS/Linux:
source venv/bin/activate
Install dependencies
pip install -r requirements.txt
Run the application
python3 app.py
If port 5000 is unavailable, another port can be specified:
PORT=5050 python3 app.py
The application can then be accessed through:
http://127.0.0.1:5050

##14. Testing

The deployed application has been tested for:
Homepage availability
Public network accessibility
Flask application health
Application status API
Architecture API
Dynamic timestamp generation
Deployment environment information
Verified APIs
GET /health
GET /api/status
GET /api/architecture
The public health endpoint returns:
status: healthy

##15. Documentation

Detailed project documentation is available in:
architecture.md
cost-analysis.md
performance-analysis.md
These documents explain the proposed architecture, cost considerations, performance characteristics, scalability and operational considerations.

##16. Expected Outcome

The proposed architecture transforms a single-server application into a scalable cloud architecture capable of supporting changing traffic levels.
The design provides:
Improved availability
Horizontal scalability
Automatic capacity management
Traffic distribution
Fault tolerance
Managed database infrastructure
Durable object storage
Centralized monitoring
Improved production readiness

##17. Conclusion

This project demonstrates the process of transforming a simple single-server application into a scalable cloud solution architecture.
The proposed AWS design combines:
Amazon Route 53
Application Load Balancer
Amazon EC2
Auto Scaling
Amazon RDS
Amazon S3
Amazon CloudWatch
to create a more scalable, available and resilient hosting platform.
The working Flask application provides a practical demonstration of the application layer, while the AWS architecture represents the proposed production solution.

Project Status

Application: Operational
Demo Deployment: Render
Production Architecture: AWS
Architecture Documentation: Complete
Cost Analysis: Complete
Performance Analysis: Complete
