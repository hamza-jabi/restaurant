pipeline {
  agent any

  environment {
    APP_NAME = "restaurant-app"
    IMAGE    = "restaurant-app:latest"
    PORT     = "5000"          // change if your app uses another port
    HOSTPORT = "5000"            // external port for clients
    DATA_DIR = "$PWD/data"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }


    stage('Docker Build') {
      steps {
        sh '''
          set -e
          docker build -t "$IMAGE" .
        '''
      }
    }

    stage('Deploy') {
      steps {
        sh '''
            set -e
            mkdir -p "$DATA_DIR"

            docker stop "$APP_NAME" 2>/dev/null || true
            docker rm "$APP_NAME" 2>/dev/null || true

            docker run -d --name "$APP_NAME" --restart unless-stopped -p "$HOSTPORT:$PORT" -v "$DATA_DIR":/app/data "$IMAGE"

            docker ps --filter "name=$APP_NAME"
        '''
      }
    }
  }

  post {
    always {
      sh 'docker image prune -f || true'
    }
  }
}
