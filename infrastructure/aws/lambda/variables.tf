variable "image_uri" {
  default = ""
}

variable "image_tag" {
  default = ""
}

variable "iam_arn" {
  default = ""
}


variable "function_name" {
  default = "music_generator"
}

variable "env_variables" {
  default = []
}

variable "ENV" {
  default = ""
  sensitive = true
}

variable "OPENAI_API_KEY" {
  default = ""
  sensitive = true
}

variable "OPENAI_MODEL" {
  default = ""
  sensitive = true
}

variable "AUDIO_FILES_URL" {
  default = ""
  sensitive = true
}

variable "PROGRESSIONS_URL" {
  default = ""
  sensitive = true
}

variable "timeout" {
  type    = number
  default = 10
  description = "Lambda timeout"
}

variable "memory_size" {
  type    = number
  default = 256
  description = "Lambda memory size"
}
