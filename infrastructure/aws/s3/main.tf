resource "aws_s3_bucket" "rugged_buckets" {
  count = length(var.s3_bucket_names)
  bucket = var.s3_bucket_names[count.index]
  acl = "private"
  region = var.AWS_DEFAULT_REGION
  force_destroy = true
}
