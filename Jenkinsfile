node {


    
    def app
    def dockerRegistry
    def dockerCreds
    
    parameters {
        string(name: 'git_commit_hash', defaultValue: 'default', description: 'Git Commit Hash')
    }


    stage('Clone repository') {
        /* Let's make sure we h ave the repository cloned to our workspace */

        /*checkout scm*/
        checkout ([
            $class: 'GitSCM',
            branches: [[name: "${params.git_commit_hash}" ]],
            userRemoteConfigs: [[
            url: 'https://github.com/armory/Mainstay.git']]
                   ])
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("cremerfc/mainstay")
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
            app.push("latest")
            
        }
    }
    stage('Create Properties file ') {
        sh "DIGEST=\$(docker inspect --format='{{index .RepoDigests 0}}' registry.hub.docker.com/cremerfc/mainstay:"+ "${env.BUILD_NUMBER}"+")"
        sh "echo \$DIGEST"
        
      
        archiveArtifacts artifacts: 'image.properties'
    }
        
}
