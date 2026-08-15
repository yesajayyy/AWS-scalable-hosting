from flask import Flask, render_template, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        environment=os.getenv("EB_ENVIRONMENT", "AWS Elastic Beanstalk"),
        region=os.getenv("AWS_REGION", "Configured AWS Region"),
        current_time=datetime.now().strftime("%d %b %Y, %I:%M:%S %p")
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "Scalable Hosting Application",
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().isoformat()
    })


@app.route("/api/status")
def status():
    return jsonify({
        "application": "AWS Scalable Hosting Architecture",
        "status": "operational",
        "deployment": "AWS Elastic Beanstalk",
        "load_balancing": "Application Load Balancer",
        "scaling": "Auto Scaling",
        "monitoring": "Amazon CloudWatch",
        "storage": "Amazon S3",
        "database": "Amazon RDS"
    })


@app.route("/api/architecture")
def architecture():
    return jsonify({
        "users": "Internet Users",
        "dns": "Amazon Route 53",
        "load_balancer": "Application Load Balancer",
        "compute": "Amazon EC2",
        "orchestration": "AWS Elastic Beanstalk",
        "scaling": "Auto Scaling Group",
        "storage": "Amazon S3",
        "database": "Amazon RDS",
        "monitoring": "Amazon CloudWatch"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
