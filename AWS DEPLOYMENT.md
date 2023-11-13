# AWS and Deployment

### Provide some high-level documentation on how to deploy the Django application on an AWS service of your choice

As I'm most familiar with GCP and Google App Engine, I'll choose its AWS relative, [Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html), which is a Platform as a Service (PaaS) that simplifies the deployment process:

1. Create a new Elastic Beanstalk environment:

- Go to the AWS Management Console, open the Elastic Beanstalk console, and click on “Create a new environment”.
- Select “Web server environment”, then click “Select”.
- In the “Environment information” section, provide a name and description for the environment.
- In the “Platform” section, select “Python” as the platform and choose the latest version.

2. Upload the Django application:

- In the “Application code” section, select “Upload your code”, then click “Upload”.
- Click “Choose file”, then select the ZIP file of the Django application. The application must include a requirements.txt file at the root level to install the necessary dependencies, and a .ebextensions/django.config file to configure the WSGI path.
- Click “Upload”, then “Create environment”. AWS Elastic Beanstalk will then start creating the environment, which may take a few minutes.

3. Configure the environment:

- Once the environment is ready, click on its name in the Elastic Beanstalk console to view its details.
- Click on “Configuration” in the sidebar, then “Edit” in the “Software” section.
- In the “Environment properties” section, we can add environment variables like DJANGO_SETTINGS_MODULE and SECRET_KEY.
- Click “Apply” to save the changes.

4. Access the deployed application:

- After the environment is set up and the application is deployed, we can access it via the URL provided in the “Environment details” page.

Also, we should take into account setting up a database for the application, as Elastic Beanstalk does not provide one by default. We could use AWS RDS for this purpose.
