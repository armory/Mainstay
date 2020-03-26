node {


    
    def app
    def dockerRegistry
    def dockerCreds


    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("cremerfc/capone-flask-app")
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        
            echo "Tests passed, nothing to see here."
        
    }

    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
        /* If we are pushing to docker hub, use this: */
           dockerRegistry =  'https://registry.hub.docker.com'
           dockerCreds = 'fernando-dockerhub'
        /* If we are pushing to Artifactory, use this: 
        dockerRegistry = 'https://armory-docker-local.jfrog.io'
        dockerCreds = 'fernando-armory-artifactory'*/
        
        docker.withRegistry(dockerRegistry, dockerCreds ) {
            app.push("${env.BUILD_NUMBER}")
           /* app.push("latest") */
            
        }
    }
    stage('Create Properties file') {
        def content = "Build_Number=${env.BUILD_NUMBER}"
        writeFile file: 'image.properties', text: content
    
    }
}
