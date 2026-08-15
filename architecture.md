# AWS Scalable Hosting Architecture

## 1. Objective

The objective is to redesign a single-server web hosting architecture into a scalable and highly available AWS architecture.

## 2. Existing Problem

The original architecture uses a single application server.

Problems:

- Single point of failure
- Limited scalability
- Performance degradation during traffic spikes
- Manual capacity management
- Difficult maintenance
- Limited fault tolerance

## 3. Proposed Architecture

Users access the application through Amazon Route 53.

Traffic is forwarded to an Application Load Balancer.

The load balancer distributes requests across multiple Amazon EC2 instances.

AWS Elastic Beanstalk manages the application environment.

Auto Scaling adjusts the number of EC2 instances according to demand.

Amazon RDS provides managed relational database capabilities.

Amazon S3 provides object storage.

Amazon CloudWatch provides monitoring and operational visibility.

## 4. AWS Components

### Amazon Route 53

Provides DNS routing for the application.

### Application Load Balancer

Distributes incoming HTTP/HTTPS traffic across healthy application instances.

### AWS Elastic Beanstalk

Provides application deployment and environment management.

### Amazon EC2

Runs the web application.

### Auto Scaling

Adjusts application capacity according to demand.

### Amazon RDS

Provides managed relational database infrastructure.

### Amazon S3

Provides durable object storage.

### Amazon CloudWatch

Provides monitoring, metrics, alarms and logs.

## 5. Scalability

When traffic increases, additional application instances can be launched.

When traffic decreases, unnecessary instances can be removed.

This reduces the need for manual capacity planning.

## 6. Availability

Multiple application instances reduce the dependency on a single server.

The load balancer can distribute requests to healthy instances.

## 7. Security Considerations

Recommended production configuration:

- HTTPS
- IAM least-privilege policies
- Private database subnet
- Security groups
- Encryption
- Secrets management
- CloudWatch monitoring
- Regular backups

## 8. Design Decision

AWS Elastic Beanstalk was selected because it simplifies application deployment and infrastructure management while still allowing the underlying AWS resources to be configured.

## 9. Expected Result

The redesigned architecture provides:

- Better scalability
- Improved availability
- Better traffic distribution
- Easier deployment
- Improved monitoring
- Reduced operational complexity
