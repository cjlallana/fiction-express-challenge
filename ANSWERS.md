# Answers to Microservices and Non-relational Databases

##  Write a brief overview of how you would redesign the blog system using a microservices architecture.

In a microservices architecture, each service is a small, independent application that communicates with other services over a network. Each service could be scaled independently based on its own needs. Here’s how I would redesign the blog system:

- User Service: This service would handle user registration, login, and management. It would store user data (profile information, preferences, etc) and provide an API for other services to validate user credentials and roles.

- Blog Post Service: This service would handle creating, reading, updating, and deleting blog posts. It would store blog post data and provide an API for other services to interact with this data.

- Frontend Service: This service would handle rendering the user interface and communicating with the other services. It would retrieve data from the User Service and Blog Post Service and display it to the user.

- API Gateway: This would act as the single entry point for all client requests. It would route requests to the appropriate service and aggregate responses from multiple services.

- Identity and Access Management (IAM) Service: This service would handle authentication and authorization. It would issue tokens to authenticated users and validate these tokens on each request to ensure the user has permission to perform the requested operation.

- Database: Each service would have its own dedicated database to ensure loose coupling and high cohesion. The User Service might use a SQL database to store user data, while the Blog Post Service might use a NoSQL database to store blog posts for scalability.

- Message Queue: A message queue service could be used to handle communication between services asynchronously. This would help to decouple the services further and allow them to handle large volumes of requests (for example, a lot of comments on an specific post).

- Search Service: To provide fast search results, a separate service using an indexing and search platform like Elasticsearch could be used. The Blog Post Service would update the index whenever a blog post is created, updated, or deleted, and the Search Service would query this index to return search results.

The great advantage is that each of these services would be small, independent applications that could be deployed, upgraded, scaled, and restarted independently. This would allow the blog system to handle a vast amount of traffic and data efficiently.

## How would you incorporate non-relational databases into this architecture, if necessary? Provide a simple schema and the motivation to implement it

Incorporating non-relational databases like MongoDB or DynamoDB into the microservices architecture can be beneficial for services that require flexible schema, high write loads, or where horizontal scaling is necessary.

For instance, the Blog Post Service could benefit from a NoSQL database like MongoDB. Blog posts can have varying structures - some might have images, others might have videos, and some might just be text. A NoSQL database would allow us to store this varied data more efficiently.

Here’s a simple MongoDB schema for the Blog Post Service:

```
{
  "_id": "ObjectId",
  "title": "String",
  "content": "String",
  "date_posted": "Date",
  "author_id": "ObjectId",
  "media": [
    {
      "type": "String",
      "url": "String"
    }
  ]
}
```

This schema allows us to store blog posts with varying structures and is more flexible than a relational database schema. It can also handle high write loads efficiently, which is beneficial if the Blog Post Service needs to create a large number of blog posts in a short amount of time.

Note that using a NoSQL database might not always be the best choice, and the decision should be based on the specific requirements of the application.
