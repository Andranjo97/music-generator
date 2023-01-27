variable "api_gateway_name" {
  default = ""
}

variable "lambda_arn" {
  default = ""
}

variable "lambda_invoke_arn" {
  default = ""
}

variable "stage_name" {
  type        = string
  default     = "$default"
  description = "Api gateway stage name"
}

variable "api_gw_record_name" {
  type        = string
  description = "Api gateway record Name"
}

variable "domain_name" {
  description = "Domain Name resource"
}
