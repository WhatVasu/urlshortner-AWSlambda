# Serverless URL Shortener

A serverless URL shortening application built on AWS that allows users to convert long URLs into short, shareable links. The application uses AWS managed services to provide scalability, reliability, and cost efficiency without managing servers.

## Features

* Shorten long URLs
* Redirect users to original URLs
* Generate unique short codes
* REST API architecture
* Serverless deployment
* Cloud-based data storage
* Logging and monitoring support

## Architecture

```text
Client (Browser)
        |
        v
API Gateway
    /       \
   v         v
Create URL  Redirect URL
 Lambda      Lambda
      \      /
       \    /
       DynamoDB
```

## AWS Services Used

### AWS Lambda

* Serverless compute for backend logic
* URL creation functionality
* Redirect handling
* Event-driven execution

### Amazon API Gateway

* REST API management
* Route handling
* Request and response processing
* Lambda integration

### Amazon DynamoDB

* NoSQL database
* URL mapping storage
* High availability and scalability
* Low-latency lookups

## Skills Demonstrated

### Cloud Computing

* Serverless Architecture
* Event-Driven Systems
* Managed Cloud Services
* Cloud Resource Configuration

### Database Management

* NoSQL Data Modeling
* DynamoDB Operations
* Data Persistence
* Key-Based Retrieval

### AWS Development

* Lambda Function Development
* API Gateway Configuration
* DynamoDB Integration
* IAM Role Management




## API Endpoints

### Create Short URL

```http
POST /shorten
```

Request:

```json
{
  "url": "https://example.com"
}
```

Response:

```json
{
  "short_code": "abc123"
}
```

### Redirect

```http
GET /{short_code}
```

