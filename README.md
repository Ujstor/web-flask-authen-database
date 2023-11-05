# Notes - WebApp in Flask

<pre>
username: test@mail.com
password: vAYAtdqww2Mjjwn
</pre>

![expected output](https://i.imgur.com/NnkwjdM.png)

![expected output](https://i.imgur.com/HAAwOoX.png)

![expected output](https://i.imgur.com/9rFOYze.png)
<br/>

## Running The App

```bash
python main.py
```

## Viewing The App

Go to:
`http://127.0.0.1:5010`

## Docker

To build the Docker image from the code, run:

```
docker compose -f .\docker-compose-dev.yml up
```

If you want to pull the image from the Docker repository instead, use:

```
docker compose -f .\docker-compose-prod.yml up
```

image is automatically built and deployed through the Jenkins pipeline.
Application deployment can be achieved using docker-compose and hosting on the cloud self-hosting service provided by [Collify](https://coolify.io/). An open-source & self-hostable Heroku / Netlify alternative.

<br/>

![](https://i.imgur.com/WVvnWzi.png)

# Jenkins Pipeline

This Jenkins pipeline is designed to automate the continuous integration and deployment process. It consists of various stages that are executed based on specific conditions, primarily targeting the `master` branch. Here's a brief overview of the pipeline:

1. **Agent Configuration**: The pipeline is configured to run on any available Jenkins agent.

2. **Environment Variables**: Several environment variables are defined, including the Docker Hub username, Docker repository name, version part (e.g., Patch, Minor, Major), and an empty TAG variable for Docker image tagging.

3. **Stages**:

   - **Checkout Code**: This stage fetches the source code from a GitHub repository, specific to the `BRANCH_NAME`.

   - **Generate Docker Image Tag**: This stage generates a Docker image tag based on the `BRANCH_NAME` and `VERSION_PART` when the branch is `master`. It executes a shell script and sets the generated tag to the `TAG` environment variable.

   - **Build**: When the branch is `master`, this stage builds a Docker image with the previously generated tag.

   - **Deploy**: Also targeting the `master` branch, this stage pushes the Docker image to the Docker Hub repository using the tag generated earlier.

   - **Environment Cleanup**: This stage cleans up the Docker image with the generated tag after a successful deployment.

4. **Post Actions**: After the pipeline is completed successfully, it prints a success message indicating the successful execution of the pipeline.

This pipeline facilitates the automation of building, tagging, and deploying a Docker image on the `master` branch. It's a part of a CI/CD process, ensuring that code changes are deployed consistently and reliably.
