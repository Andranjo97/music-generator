variable "iam_name" {
  default = ""
  sensitive = true
}

variable "lambda_iam_policy_name" {
  default = "music_generator_lambda_iam_policy"
}
