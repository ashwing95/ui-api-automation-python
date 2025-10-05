pipeline {
  agent any

  environment {
    APP_NAME = "my-sample-app"
  }

  stages {
    stage('Checkout') {
      steps {
        echo "Checking out code from ${env.GIT_URL}"
        checkout scm
      }
    }

    stage('Build') {
      steps {
        echo "Starting build process..."
        sh '''
          echo "Running build commands..."
          # Add your actual build steps here, for example:
          # npm install
          # mvn clean package
          ls -la
        '''
      }
    }

    stage('Test') {
      steps {
        echo "Running tests..."
        sh '''
          echo "Pretend we’re testing..."
          # ./run-tests.sh
        '''
      }
    }

    stage('Deploy') {
      when {
        branch 'main'  // Only deploy from main
      }
      steps {
        echo "Deploying application..."
        sh '''
          echo "Here you’d run deploy commands"
          # ./deploy.sh
        '''
      }
    }
  }

  post {
    always {
      echo "Cleaning up workspace..."
      sh 'rm -rf * || true'
    }
    success {
      echo "✅ Build completed successfully!"
    }
    failure {
      echo "❌ Build failed. Check logs for errors."
    }
  }
}
