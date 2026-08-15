# AWS Scalable Hosting Architecture — Cost Analysis

## 1. Objective

The objective of this cost analysis is to compare a simple single-server hosting model with the proposed scalable AWS architecture.

The analysis focuses on the main AWS services required for production deployment and the trade-off between infrastructure cost, availability, scalability and operational reliability.

---

## 2. Architecture Options

### Option 1 — Single EC2 Instance

A basic deployment can use a single Amazon EC2 instance running the application.

### Advantages

- Simple architecture
- Low infrastructure complexity
- Lower initial cost
- Easy to deploy
- Suitable for small applications
- Minimal configuration

### Disadvantages

- Single point of failure
- Limited scalability
- Manual capacity management
- No automatic failover
- Performance can degrade during traffic spikes
- Application availability depends on one server

This architecture may be suitable for development, testing or very small applications with predictable traffic.

---

## 3. Option 2 — Scalable AWS Architecture

The proposed production architecture uses:

- Amazon Route 53
- Application Load Balancer
- Amazon EC2
- Auto Scaling
- Amazon RDS
- Amazon S3
- Amazon CloudWatch

### Advantages

- Multiple application instances
- Automatic scaling
- Load balancing
- Improved availability
- Better fault tolerance
- Managed database infrastructure
- Centralized monitoring
- Better support for unpredictable traffic

### Disadvantages

- Higher infrastructure cost
- More AWS services to configure
- Greater architectural complexity
- Additional monitoring and operational requirements

---

## 4. Main Cost Drivers

The overall AWS cost depends on application traffic and resource utilization.

### Amazon EC2

EC2 cost depends on:

- Instance type
- Number of instances
- Running hours
- Operating system
- Region
- Compute utilization

Auto Scaling can reduce unnecessary compute capacity during periods of low traffic.

### Application Load Balancer

The Application Load Balancer introduces additional cost based on usage.

Cost is influenced by:

- Number of load balancers
- Hours of operation
- Traffic processed
- Load Balancer Capacity Units

The benefit is improved traffic distribution and application availability.

### Amazon RDS

RDS cost depends on:

- Database instance type
- Database storage
- Running hours
- Backup storage
- Availability configuration
- Database workload

A development environment can use a smaller configuration, while production workloads may require a larger instance or Multi-AZ deployment.

### Amazon S3

S3 costs depend primarily on:

- Amount of data stored
- Number of requests
- Data transfer
- Storage class

S3 lifecycle policies can automatically move older data to lower-cost storage classes when appropriate.

### Amazon Route 53

Route 53 costs are associated with DNS hosted zones and DNS queries.

The actual cost depends on the number of hosted zones and query volume.

### Amazon CloudWatch

CloudWatch costs depend on:

- Metrics
- Log ingestion
- Log storage
- Alarms
- Monitoring features

Monitoring should be configured according to the application's operational requirements to avoid unnecessary logging costs.

---

## 5. Cost Comparison

| Feature | Single EC2 | Scalable AWS Architecture |
|---|---|---|
| Compute | Single EC2 | Multiple EC2 instances |
| Load Balancing | No | Application Load Balancer |
| Auto Scaling | No | Yes |
| Database | Self-managed or local | Amazon RDS |
| Object Storage | Local storage | Amazon S3 |
| Monitoring | Basic | Amazon CloudWatch |
| Availability | Low to moderate | High |
| Scalability | Limited | High |
| Infrastructure Cost | Lower | Higher |
| Operational Complexity | Low | Moderate |
| Fault Tolerance | Low | High |

---

## 6. Cost vs Reliability Trade-off

The scalable architecture costs more than a single-server deployment.

However, the additional cost provides:

- Higher availability
- Automatic scaling
- Better traffic distribution
- Reduced single points of failure
- Managed database infrastructure
- Improved monitoring
- Better production readiness

Therefore, infrastructure cost should not be evaluated independently from application reliability.

For business-critical applications, the additional infrastructure cost can be justified by the reduction in downtime risk and improved scalability.

---

## 7. Cost Optimization Strategies

The following practices can help control AWS infrastructure costs.

### 1. Right-size EC2 Instances

Select EC2 instance types based on actual CPU, memory and network requirements.

Avoid using unnecessarily large instances.

### 2. Use Auto Scaling

Automatically increase capacity during high demand and reduce capacity when demand decreases.

### 3. Monitor Resource Utilization

Use CloudWatch to identify underutilized resources.

### 4. Use Appropriate RDS Capacity

Select the smallest database configuration that can reliably support the workload.

Scale the database when application requirements increase.

### 5. Optimize S3 Storage

Use S3 lifecycle policies to transition older objects to appropriate storage classes.

### 6. Remove Unused Resources

Regularly identify and remove unused:

- EC2 instances
- Load balancers
- EBS volumes
- Snapshots
- Elastic IP addresses
- Test environments

### 7. Control CloudWatch Logs

Set appropriate log retention periods instead of keeping all logs indefinitely.

### 8. Review AWS Billing

Monitor monthly AWS spending and investigate unexpected increases.

### 9. Use AWS Pricing Calculator

Before production deployment, estimate the expected monthly cost using the AWS Pricing Calculator.

---

## 8. Development vs Production

A development environment does not necessarily require the complete production architecture.

### Development

A development environment may use:

    Developer
        |
        v
    Single EC2 Instance
        |
        v
    Development Database

### Production

The production environment can use:

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

This provides a stronger balance between availability, scalability and operational reliability.

---

## 9. AWS Pricing Considerations

AWS pricing varies depending on:

- AWS Region
- Instance type
- Number of running instances
- Application traffic
- Database configuration
- Storage requirements
- Backup requirements
- Monitoring requirements
- Data transfer

Therefore, exact monthly pricing should be calculated using the AWS Pricing Calculator with the actual production requirements.

The values used for a final production estimate should be reviewed before deployment because AWS pricing can change over time.

---

## 10. Demo Deployment Cost

The working demonstration application for this project is deployed on Render.

The Render deployment is used to demonstrate the Flask application publicly.

The proposed AWS architecture represents the production design and would incur AWS infrastructure costs if deployed.

This distinction keeps the project documentation technically accurate.

---

## 11. Final Cost Assessment

The single-server architecture provides the lowest infrastructure complexity and cost, but it has limited scalability and availability.

The proposed AWS architecture requires additional services and therefore has higher infrastructure costs.

However, it provides:

- High availability
- Automatic scaling
- Load balancing
- Managed database infrastructure
- Durable storage
- Monitoring
- Better fault tolerance
- Improved production readiness

For applications where availability and scalability are important, the additional infrastructure cost can be justified.

For small applications with predictable traffic, a simpler architecture may remain more economical.

The final architecture should therefore be selected based on:

- Business requirements
- Expected traffic
- Availability targets
- Performance requirements
- Operational requirements
- Budget

---

## Project Cost Summary

| Architecture | Cost Level | Scalability | Availability | Complexity |
|---|---|---|---|---|
| Single EC2 | Low | Low | Low to Moderate | Low |
| Scalable AWS Architecture | Higher | High | High | Moderate |

The scalable architecture represents a higher initial infrastructure cost but provides significantly stronger scalability, availability, fault tolerance and operational capabilities.