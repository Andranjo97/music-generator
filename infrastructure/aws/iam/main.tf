# Create Role
resource "aws_iam_role" "iam_for_lambda" {
  name = var.iam_name

  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
  })
}

#Created Policy for IAM Role
resource "aws_iam_policy" "music_generator_lambda_iam_policy" {
  name = var.lambda_iam_policy_name
  description = "Policy to read and write to s3"

  policy = jsonencode(
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
              "logs:*"
          ],
          "Resource": "arn:aws:logs:*:*:*"
        },
        {
          "Effect": "Allow",
          "Action": [
              "s3:*",
              "s3:*",
              "s3-object-lambda:*"
          ],
          "Resource": "arn:aws:s3:::*"
        }
      ]
    } 
  )
}

# Attach Policy to Role
resource "aws_iam_role_policy_attachment" "music_generator_policy_attachment" {
  role = aws_iam_role.iam_for_lambda.name
  policy_arn = aws_iam_policy.music_generator_lambda_iam_policy.arn
}

output "iam_arn" {
  value = aws_iam_role.iam_for_lambda.arn
}
