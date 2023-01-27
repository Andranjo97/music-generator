resource "aws_lambda_function" "music_generator_lambda" {
  image_uri = "${var.image_uri}@${var.image_tag}"
  package_type = "Image"
  memory_size  = var.memory_size
  timeout      = var.timeout
  architectures = ["x86_64"]
  function_name = var.function_name
  role = var.iam_arn
  environment {
    variables = {
      env = var.ENV
      openai_api_key = var.OPENAI_API_KEY
      openai_model = var.OPENAI_MODEL
      audio_files_url = var.AUDIO_FILES_URL
      progressions_url = var.PROGRESSIONS_URL
    }
  }
}

output "lambda_id" {
  value = aws_lambda_function.music_generator_lambda.id
}

output "lambda_arn" {
  value = aws_lambda_function.music_generator_lambda.arn
}

output "lambda_invoke_arn" {
  value = aws_lambda_function.music_generator_lambda.invoke_arn
}
