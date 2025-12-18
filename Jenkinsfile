pipeline {
  agent any

  environment {
    APP_NAME = "restaurant-app"
    IMAGE    = "restaurant-app:latest"
    PORT     = "5000"          // change if your app uses another port
    HOSTPORT = "5000"            // external port for clients
    DATA_DIR = "$PWD/data:/app/data"
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
            sudo mkdir -p "$DATA_DIR"
            sudo chown -R $(id -u):$(id -g) "$DATA_DIR"

            docker stop "$APP_NAME" 2>/dev/null || true
            docker rm "$APP_NAME" 2>/dev/null || true

            docker run -d --name "$APP_NAME" --restart unless-stopped -p "$HOSTPORT:$PORT" -v "$DATA_DIR":/app/data -v "$IMAGE"

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
