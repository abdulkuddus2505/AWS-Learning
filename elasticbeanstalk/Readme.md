Create VPC + RDS

aws cloudformation create-stack \
  --stack-name flask-infra \
  --template-body file:///home/abdulk/AWS_Learning/elasticbeanstalk/cloudformation/infra.yml \
  --capabilities CAPABILITY_NAMED_IAM


eb init -p python flask-age-app --region us-east-1
